package Algorany;

import java.util.*;
import java.io.*;

public class NandM12 {

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
        str = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            graph[i] = Integer.parseInt(str.nextToken());
        }
        result = new int[m];
        Arrays.sort(graph);
        sb = new StringBuilder();
        dfs(0, 0);
        System.out.println(sb.toString());
    }

    public static void dfs(int start, int depth) {
        if (depth == m) {
            for(int i : result){
                sb.append(i).append(" ");
            }
            sb.append("\n");
            return;
        }
        for (int i = start; i < n; i++) {
            if (i > 0) {
                if (graph[i - 1] == graph[i]) {
                    continue;
                }
            }
            result[depth] = graph[i];
            dfs(i, depth + 1);
        }
    }
}
