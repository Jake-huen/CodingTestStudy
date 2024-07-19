package Algorany.NandM;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Six {

    static int n, m;
    static int[] graph;
    static int[] result;
    static StringBuilder sb;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());
        n = Integer.parseInt(str.nextToken());
        m = Integer.parseInt(str.nextToken());
        graph = new int[n];
        result = new int[m];
        visited = new boolean[n];
        sb = new StringBuilder();
        str = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            graph[i] = Integer.parseInt(str.nextToken());
        }
        Arrays.sort(graph);
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
        int before = depth > 0 ? result[depth - 1] : 0;
        for (int i = start; i < n; i++) {
            if (visited[i]) {
                continue;
            }
            if (graph[i] > before) {
                visited[i] = true;
                result[depth] = graph[i];
                dfs(i, depth + 1);
                visited[i] = false;
            }
        }
    }
}