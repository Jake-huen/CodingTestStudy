package Algorany;

import java.util.*;
import java.io.*;


public class CountConnected {

    static int n, m;
    static StringTokenizer str;
    static int[][] graph;
    static boolean[] visited;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = new StringTokenizer(br.readLine());
        n = Integer.parseInt(str.nextToken());
        m = Integer.parseInt(str.nextToken());
        graph = new int[n + 1][n + 1];
        answer = 0;
        visited = new boolean[n + 1];
        for (int i = 0; i < m; i++) {
            str = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(str.nextToken());
            int v = Integer.parseInt(str.nextToken());
            graph[u][v] = 1;
            graph[v][u] = 1;
        }
        for (int i = 1; i < n + 1; i++) {
            if(!visited[i]){
                bfs(i);
                answer+=1;
            }
        }
        System.out.println(answer);
    }

    public static void bfs(int node) {
        visited[node] = true;
        Queue<Integer> q = new LinkedList<>();
        q.add(node);
        while (!q.isEmpty()) {
            int cur = q.poll();
            for (int i = 1; i <= n; i++) {
                if (!visited[i] && graph[cur][i] == 1) {
                    visited[i] = true;
                    q.add(i);
                }
            }
        }
    }
}
