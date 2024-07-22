package Algorany.BackTracking;

import java.io.*;
import java.util.*;

public class PartPermutationSum {

    static int n, s;
    static StringTokenizer str;
    static int[] graph;
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = new StringTokenizer(br.readLine());
        n = Integer.parseInt(str.nextToken());
        s = Integer.parseInt(str.nextToken());
        graph = new int[n];
        String[] st = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            graph[i] = Integer.parseInt(st[i]);
        }

        dfs(0, 0);
        if (s == 0) {
            answer-=1;
        }
        System.out.println(answer);
    }

    public static void dfs(int start, int sum) {
        if (start == n) {
            if (sum == s) {
                answer += 1;
            }
            return;
        }
        dfs(start + 1, sum + graph[start]);
        dfs(start + 1, sum);
    }
}
