package Algorany;

import java.util.*;
import java.io.*;

public class Virus {

    static int n;
    static int m;
    static int[][] computers;
    static boolean[] visited;
    static ArrayList<Integer> answer = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        computers = new int[n + 1][n + 1];
        visited = new boolean[n + 1];
        for (int i = 0; i < m; i++) {
            StringTokenizer str = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(str.nextToken());
            int end = Integer.parseInt(str.nextToken());
            computers[start][end] = 1;
            computers[end][start] = 1;
        }
        visited[1] = true;
        dfs(1, 0);
        System.out.println(answer.size());

    }

    public static void dfs(int node, int ans) {
        // System.out.println(node);
        visited[node] = true;
        for (int i = 1; i <= n; i++) {
            if (!visited[i] && computers[node][i] == 1) {
                answer.add(i);
                dfs(i, ans + 1);
            }
        }
    }
}
