package Algorany;

import java.util.*;
import java.io.*;

public class DfsAndBfs {

    static int n, m, v;
    static int[][] graph;
    static boolean[] visited;
    static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());
        n = Integer.parseInt(str.nextToken());
        m = Integer.parseInt(str.nextToken());
        v = Integer.parseInt(str.nextToken());
        graph = new int[n + 1][n + 1];
        for (int i = 0; i < m; i++) {
            str = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(str.nextToken());
            int y = Integer.parseInt(str.nextToken());
            graph[x][y] = 1;
            graph[y][x] = 1;
        }
        sb = new StringBuilder();
        visited = new boolean[n + 1];
        dfs(v);
        System.out.println(sb.toString());
        sb = new StringBuilder();
        visited = new boolean[n + 1];
        bfs(v);
        System.out.println(sb.toString());
    }

    private static void bfs(int v) {
        Queue<Integer> q = new LinkedList<>();
        q.add(v);
        visited[v] = true;
        while (!q.isEmpty()) {
            int cur = q.poll();
            sb.append(cur + " ");
            for (int i = 0; i <= n; i++) {
                if(!visited[i] && graph[cur][i] ==1){
                    q.add(i);
                    visited[i] = true;
                }
            }
        }
    }

    private static void dfs(int v) {
        sb.append(v + " ");
        visited[v] = true;
        for (int i = 0; i <= n; i++) {
            if (!visited[i] && graph[v][i] == 1) {
                dfs(i);
            }
        }
    }


}
