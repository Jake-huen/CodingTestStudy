package daily.taxi;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {

    static class Node implements Comparable<Node> {
        int node;
        int distance;

        public Node(int node, int distance) {
            this.node = node;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node o) {
            return Integer.compare(this.distance, o.distance);
        }
    }

    public static int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = Integer.MAX_VALUE;

        ArrayList<Node>[] cost = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            cost[i] = new ArrayList<>();
        }

        for (int[] fare : fares) {
            int start = fare[0];
            int end = fare[1];
            int val = fare[2];
            cost[start].add(new Node(end, val));
            cost[end].add(new Node(start, val));
        }
        int[][] dist = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            Arrays.fill(dist[i], Integer.MAX_VALUE);
        }

        for (int i = 1; i <= n; i++) {
            dijkstra(i, n, cost, dist[i]);
        }

        for (int i = 1; i <= n; i++) {
            answer = Math.min(answer, dist[s][i] + dist[i][a] + dist[i][b]);
        }

        return answer;
    }

    public static void dijkstra(int start, int n, ArrayList<Node>[] cost, int[] dist) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0));
        dist[start] = 0;

        while (!pq.isEmpty()) {
            Node cur = pq.poll();

            for (Node next : cost[cur.node]) {
                int newDist = dist[cur.node] + next.distance;
                if (newDist < dist[next.node]) {
                    dist[next.node] = newDist;
                    pq.add(new Node(next.node, newDist));
                }
            }
        }
    }

    public static void main(String[] args) {
        Main T = new Main();
        System.out.println(T.solution(6, 4, 6, 2, new int[][]{{4, 1, 10}, {3, 5, 24}, {5, 6, 2}, {3, 1, 41}, {5, 1, 24}, {4, 6, 50}, {2, 4, 66}, {2, 3, 22}, {1, 6, 25}}));
        System.out.println(T.solution(7, 3, 4, 1, new int[][]{{5, 7, 9}, {4, 6, 4}, {3, 6, 1}, {3, 2, 3}, {2, 1, 6}}));
    }
}
