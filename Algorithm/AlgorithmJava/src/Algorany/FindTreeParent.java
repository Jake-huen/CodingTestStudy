package Algorany;

import java.io.*;
import java.util.*;

public class FindTreeParent {
    static int n;
    static ArrayList<ArrayList<Integer>> graph;
    static int[] answer;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        answer = new int[n + 1];
        visited = new boolean[n + 1];

        for (int i = 0; i < n - 1; i++) {
            StringTokenizer str = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(str.nextToken());
            int end = Integer.parseInt(str.nextToken());
            graph.get(start).add(end);
            graph.get(end).add(start);
        }
        visited[1] = true;
        bfs(1);
        for (int i = 2; i <= n; i++) {
            System.out.println(answer[i]);
        }
    }

    public static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        visited[start] = true;
        while (!q.isEmpty()) {

            int parent = q.poll();
            for (int i : graph.get(parent)) {
                if (!visited[i]) {
                    // System.out.println(i);
                    visited[i] = true;
                    answer[i] = parent;
                    q.add(i);
                }
            }
        }
    }
}
