package com.example;

import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

public class ZhWord implements Comparable<ZhWord> {
    private String name;//词语名
    private Set<String> pinyin = new HashSet<>();//保存拼音
    private int count;

    public ZhWord(String name, String pinyin1, String pinyin2) {
        this.name = name;
        this.pinyin.add(pinyin1);
        this.pinyin.add(pinyin2);
    }

    public String getName() {
        return name;
    }

    public Set<String> getPinyin() {
        return pinyin;
    }

    public int getCount() {
        return count;
    }

    public void addCount() {
        count++;
    }

    @Override
    public int compareTo(ZhWord other) {
        return other.count - this.count;
    }

    public void clearCount() {
        count = 0;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        if (other == null || getClass() != other.getClass()) return false;
        ZhWord zhWord = (ZhWord) other;
        return Objects.equals(name, zhWord.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name);
    }
}