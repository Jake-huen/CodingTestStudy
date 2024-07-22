package Algorany.BackTracking;

import java.io.*;
import java.util.*;

public class MakePassword {
    static int l, c;
    static StringTokenizer str;
    static String[] graph;
    static char[] vowel = {'a', 'e', 'i', 'o', 'u'};
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = new StringTokenizer(br.readLine());
        l = Integer.parseInt(str.nextToken()); // 암호 길이
        c = Integer.parseInt(str.nextToken()); // 문자 후보들
        graph = new String[c];
        str = new StringTokenizer(br.readLine());
        for (int i = 0; i < c; i++) {
            graph[i] = str.nextToken();
        }
        Arrays.sort(graph);
        dfs(0, "");

    }

    public static void dfs(int index, String result) {
        if (result.length() == l) {
            int vowelCount = 0;
            int consonantCount = 0;
            for (int i = 0; i < result.length(); i++) {
                char ch = result.charAt(i);
                if (isVowel(ch)) {
                    vowelCount++;
                } else {
                    consonantCount++;
                }
            }
            if (vowelCount >= 1 && consonantCount >= 2) {
                System.out.println(result);
            }
            return;
        }
        if (index == c) {
            return;
        }
        dfs(index + 1, result + graph[index]);
        dfs(index + 1, result);
    }

    private static boolean isVowel(char ch) {
        for (char v : vowel) {
            if (v == ch) {
                return true;
            }
        }
        return false;
    }
}
