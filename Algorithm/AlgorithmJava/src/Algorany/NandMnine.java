package Algorany;

import java.util.*;
import java.io.*;

public class NandMnine {

    static int n, m;
    static int[] graph;
    static int[] result;
    static boolean[] visited;
    static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());
        n = Integer.parseInt(str.nextToken());
        m = Integer.parseInt(str.nextToken());
        graph = new int[n];
        str = new StringTokenizer(br.readLine());
        result = new int[m];
        sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            graph[i] = Integer.parseInt(str.nextToken());
        }
        Arrays.sort(graph);
        visited = new boolean[n];
        dfs(0, 0);
        System.out.println(sb.toString());
    }

    public static void dfs(int start, int depth) {
        if (depth == m) {
            for (int i : result) {
                sb.append(i).append(" ");
            }
            sb.append("\n");
            return;
        }
        int before = 0;
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                continue;
            }
            if (before != graph[i]) {
                result[depth] = graph[i];
                visited[i] = true;
                before = graph[i];
                dfs(i, depth + 1);
                visited[i] = false;
            }
        }
    }
}
