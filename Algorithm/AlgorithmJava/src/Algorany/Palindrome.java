package Algorany;

import java.io.*;
import java.util.*;

public class Palindrome {
    static int n, m;
    static int[] graph;
    static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n];
        StringTokenizer str = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            graph[i] = Integer.parseInt(str.nextToken());
        }
        ArrayList<ArrayList<Integer>> map = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            map.add(new ArrayList<>());
        }
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }

        // 길이 2의 팰린드롬
        for (int i = 0; i < n - 1; i++) {
            if (graph[i] == graph[i + 1]) {
                dp[i][i + 1] = 1;
            }
        }

        // 길이 3 이상의 팰린드롬
        // 양 끝 문자가 동일하고 그 사이의 부분 문자열이 팰린드롬이면 그 문자열 역시 팰린드롬이다.
        for (int length = 3; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                if (graph[i] == graph[j] && dp[i + 1][j - 1] == 1) {
                    dp[i][j] = 1;
                }
            }
        }

        m = Integer.parseInt(br.readLine());
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < m; i++) {
            str = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(str.nextToken()) - 1;
            int e = Integer.parseInt(str.nextToken()) - 1;
            if (dp[s][e] == 1) {
                answer.append(1).append("\n");
            } else {
                answer.append(0).append("\n");
            }
        }
        System.out.println(answer.toString());
    }

}
