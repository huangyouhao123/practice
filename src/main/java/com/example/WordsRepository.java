package com.example;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class WordsRepository {
    //保存词库
    static List<ZhWord> ciku = new ArrayList<>();

    static {
        ciku.addAll(Arrays.asList(
                new ZhWord("华为技术", "hwjs", "huaweijishu"),
                new ZhWord("采访", "cf", "caifang"),//简拼相同
                new ZhWord("财富", "cf", "caifu"),
                new ZhWord("厨房", "cf", "chufang"),
                new ZhWord("春风", "cf", "chunfeng"),
                new ZhWord("赤峰", "cf", "chifeng"),
                new ZhWord("深圳", "sz", "shenzhen"),
                new ZhWord("华为", "hw", "huawei"),
                new ZhWord("技术", "js", "jishu"),
                new ZhWord("南京", "nj", "nanjing"),
                new ZhWord("雨花台", "yht", "yuhuatai"),
                new ZhWord("新闻", "xw", "xinwen"),
                new ZhWord("大厦", "ds", "dasha"),
                new ZhWord("高楼", "gl", "gaolou"),
                new ZhWord("高校", "gx", "gaoxiao"),//全拼、简拼都相同
                new ZhWord("高效", "gx", "gaoxiao"),
                new ZhWord("高小", "gx", "gaoxiao"),
                new ZhWord("美丽", "ml", "meili"),
                new ZhWord("上下", "sx", "shangxiao"),
                new ZhWord("南宁", "nl", "nanling")//错误拼音
        ));
    }

    public static List<String> getWordsFromPinyin(String pinyin) {
        List<ZhWord> zhWordsResult = getZhWordsFromPinyin(pinyin);

        //按使用频率排序，常用的词排在前面
        Collections.sort(zhWordsResult);

        return getStringWords(zhWordsResult);
    }

    private static List<String> getStringWords(List<ZhWord> zhWordsResult) {
        List<String> words = new ArrayList<>();

        for (ZhWord zhWord : zhWordsResult) {
            words.add(zhWord.getName());
        }

        return words;
    }

    private static List<ZhWord> getZhWordsFromPinyin(String pinyin) {
        List<ZhWord> zhWordsResult = new ArrayList<>();
        for (ZhWord zhWord : ciku) {
            if (zhWord.getPinyin().contains(pinyin)) {
                zhWordsResult.add(zhWord);
            }
        }
        return zhWordsResult;
    }

    public static ZhWord getZhWordByName(String name) {
        for (ZhWord zhWord : ciku) {
            if (zhWord.getName().equals(name)) {
                return zhWord;
            }
        }
        return null;
    }


    public static void addUsageCount(String name) {
        getZhWordByName(name).addCount();
    }

    public static void clearCount() {
        for (ZhWord zhWord : ciku) {
            zhWord.clearCount();
        }
    }

    public static void addZhWord(ZhWord zhWord) {
        ciku.remove(zhWord);
        ciku.add(zhWord);
    }
}
