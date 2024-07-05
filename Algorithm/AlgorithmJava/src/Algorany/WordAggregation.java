package Algorany;

import java.io.*;
import java.util.*;

public class WordAggregation {
    static int n;
    static String[] words;
    static String result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            n = Integer.parseInt(br.readLine());
            if (n == 0) {
                return;
            }
            words = new String[n];
            for (int i = 0; i < n - 1; i++) {
                words[i] = br.readLine();
            }
            result = br.readLine();
            // System.out.println(result);
            int i = solution(words, result);
            System.out.println(i);
        }
    }

    private static int solution(String[] words, String result) {
        Set<Character> uniqueChars = new HashSet<>();
        for (String word : words) {
            for (char c : word.toCharArray()) {
                uniqueChars.add(c);
            }
        }
        for (char c : result.toCharArray()) {
            uniqueChars.add(c);
        }

        if (uniqueChars.size() > 10) {
            return 0;
        }

        List<Character> charList = new ArrayList<>(uniqueChars);
        String allDigits = "0123456789";
        List<String> permutations = generatePermutations(allDigits, charList.size());

        int validSolutions = 0;
        for (String perm : permutations) {
            Map<Character, Character> mapping = new HashMap<>();
            for (int i = 0; i < charList.size(); i++) {
                mapping.put(charList.get(i), perm.charAt(i));
            }
            if (isValidSolution(words, result, mapping)) {
                validSolutions++;
            }
        }

        return validSolutions;
    }

    private static List<String> generatePermutations(String str, int length) {
        List<String> result = new ArrayList<>();
        permute(str.toCharArray(), 0, length, result);
        return result;
    }

    private static void permute(char[] arr, int l, int length, List<String> result) {
        if (l == length) {
            result.add(new String(arr, 0, length));
        } else {
            for (int i = l; i < arr.length; i++) {
                swap(arr, l, i);
                permute(arr, l + 1, length, result);
                swap(arr, l, i); // backtrack
            }
        }
    }

    private static void swap(char[] arr, int i, int j) {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    private static boolean isValidSolution(String[] words, String result, Map<Character, Character> mapping) {
        // Convert words and result according to the current mapping
        List<Long> mappedWords = new ArrayList<>();
        for (String word : words) {
            long mappedWord = mapWord(word, mapping);
            if (mappedWord == -1) {
                return false;
            }
            mappedWords.add(mappedWord);
        }
        long mappedResult = mapWord(result, mapping);
        if (mappedResult == -1) {
            return false;
        }

        // Calculate the sum of the words
        long wordsSum = 0;
        for (long word : mappedWords) {
            wordsSum += word;
        }

        // Check if the sum of the words equals the result
        return wordsSum == mappedResult;
    }

    private static long mapWord(String word, Map<Character, Character> mapping) {
        if (mapping.get(word.charAt(0)) == '0') {
            return -1;  // Leading zero condition
        }

        StringBuilder sb = new StringBuilder();
        for (char c : word.toCharArray()) {
            sb.append(mapping.get(c));
        }
        return Long.parseLong(sb.toString());
    }
}
