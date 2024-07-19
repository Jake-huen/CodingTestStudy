package Algorany.NandM;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Three {

    static int n, m;
    static int[] graph;
    static int[] result;
    static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());
        n = Integer.parseInt(str.nextToken());
        m = Integer.parseInt(str.nextToken());
        graph = new int[n];
        result = new int[m];
        sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            graph[i] = i + 1;
        }
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
            result[depth] = graph[i];
            dfs(depth + 1);
        }
    }
}