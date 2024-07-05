package Algorany;

import java.util.*;

class FarNode {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] i : edge) {
            int start = i[0];
            int end = i[1];

            graph.get(start).add(end);
            graph.get(end).add(start);
        }

        boolean[] visited = new boolean[n + 1];

        return bfs(graph, n, visited);
    }

    public static int bfs(ArrayList<ArrayList<Integer>> graph, int n, boolean[] visited) {
        Queue<int[]> q = new LinkedList<>();
        int answer = 0;
        q.add(new int[]{1, 0});

        int maxCost = 0;

        while (!q.isEmpty()) {
            int[] arr = q.poll();
            int v = arr[0];
            int cost = arr[1];
            if (maxCost == cost) {
                answer += 1;
            } else if (maxCost < cost) {
                maxCost = cost;
                answer = 1;
            }

            for (int i = 0; i < graph.get(v).size(); i++) {
                int w = graph.get(v).get(i);
                if (!visited[w]) {
                    q.add(new int[]{w, cost + 1});
                    visited[w] = true;
                }
            }
        }
        return answer;

    }

}
