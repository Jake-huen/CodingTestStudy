package Algorany;

import java.io.*;
import java.util.*;

public class Shortcut {
    static int V, E, K;
    static ArrayList<Node>[] graph;
    static boolean[] isVisited;
    static int[] dijkstraTable;

    static class Node {
        int n;
        int cost;

        Node(int n, int cost) {
            this.n = n;
            this.cost = cost;
        }
    }

    public static void dijkstra(int start) {
        isVisited = new boolean[V + 1];
        dijkstraTable = new int[V + 1];
        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> {
            return o1.cost - o2.cost;
        });
        pq.add(new Node(start, 0));
        while (!pq.isEmpty()) {
            Node curNode = pq.poll();

            for (Node node : graph[curNode.n]) {
                int newW = curNode.cost + node.cost;
                int originW = dijkstraTable[node.n];
                if (originW > newW) {
                    dijkstraTable[node.n] = newW;
                    pq.add(new Node(node.n, newW));
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());
        V = Integer.parseInt(str.nextToken()); // 정점 수
        E = Integer.parseInt(str.nextToken()); // 간선 수
        K = Integer.parseInt(br.readLine()); // 시작 정점의 번호
        graph = new ArrayList[V + 1];
        for (int i = 1; i <= V; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < E; i++) {
            str = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(str.nextToken());
            int v = Integer.parseInt(str.nextToken());
            int w = Integer.parseInt(str.nextToken());
            graph[u].add(new Node(v, w));
        }

        dijkstra(K);

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < V + 1; i++) {
            if (i == K) {
                sb.append(0).append("\n");
            } else if (dijkstraTable[i] == Integer.MAX_VALUE) {
                sb.append("INF").append("\n");
            } else {
                sb.append(dijkstraTable[i]).append("\n");
            }
        }
        System.out.println(sb);
    }
}
