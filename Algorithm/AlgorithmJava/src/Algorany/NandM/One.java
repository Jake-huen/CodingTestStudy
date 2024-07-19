package Algorany.NandM;

import java.util.*;
import java.io.*;

public class One {

    static int n, m;
    static int[] graph;
    static int[] result;
    static StringBuilder sb;
    static StringTokenizer str;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = new StringTokenizer(br.readLine());
        n = Integer.parseInt(str.nextToken());
        m = Integer.parseInt(str.nextToken());
        graph = new int[n];
        visited = new boolean[n];
        result = new int[m];
        sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            graph[i - 1] = i;
        }
        Arrays.sort(graph);
        dfs(0);
        System.out.println(sb.toString());
    }

    public static void dfs(int depth) {
        if (depth == m) {
            for (int i : result) {
                sb.append(i).append(" ");
            }
            sb.append("\n");
            return;
        }
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                continue;
            }
            visited[i] = true;
            result[depth] = graph[i];
            dfs(depth + 1);
            visited[i] = false;
        }
    }
}