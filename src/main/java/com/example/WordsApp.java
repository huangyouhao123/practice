package com.example;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.StringTokenizer;

/**
 * Words App
 */
public class WordsApp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("please enter pinyin , Q to exit , A to add");
            System.out.print(">");
            String input = sc.nextLine();
            if (input.toUpperCase().equals("Q")) {
                break;
            }
            if (input.toUpperCase().equals("A")) {
                System.out.println("please enter word,pingin1,pinyin2:");
                String s = sc.nextLine();
                StringTokenizer t = new StringTokenizer(s, ",");
                String name = t.nextToken();
                String pinyin1 = t.nextToken();
                String pinyin2 = t.nextToken();
                ZhWord myWord = new ZhWord(name, pinyin1, pinyin2);
                WordsRepository.addZhWord(myWord);
                System.out.println("already added!!!");
                continue;
            }
            List<String> result = new ArrayList<>();
            List<String> words = WordsRepository.getWordsFromPinyin(input);

            int j = 1;
            for (String word : words) {
                result.add(j + "-" + word);
                j++;
            }
            if (result.size() > 0) {
                System.out.println(result);
                System.out.print("please enter digit to choice>");
                int choice = sc.nextInt();
                sc.nextLine();

                if (choice <= words.size() && choice > 0) {
                    String selectedWord = words.get(choice - 1);
                    System.out.println(selectedWord);
                    WordsRepository.addUsageCount(selectedWord);
                }
            } else {
                System.out.println("no word!!!");
            }
        }
    }
}
