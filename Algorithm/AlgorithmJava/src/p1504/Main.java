package p1504;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, e;
    static int[] dist;
    static final int INF = 20000000;
    static ArrayList<ArrayList<Point>> graph;

    static class Point implements Comparable<Point> {
        int end;
        int weight;

        Point(int end, int weight) {
            this.end = end;
            this.weight = weight;
        }

        @Override
        public int compareTo(Point o) {
            return weight - o.weight;
        }
    }


    public static void main(String[] args) throws IOException {
        Main T = new Main();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            graph.get(start).add(new Point(end, weight));
            graph.get(end).add(new Point(start, weight));
        }
        st = new StringTokenizer(br.readLine());
        int v1 = Integer.parseInt(st.nextToken());
        int v2 = Integer.parseInt(st.nextToken());
        int[] result1 = dijkstra(1);
        int s1 = result1[v1]; // 1 -> v1
        int s2 = result1[v2]; // 1 -> v2

        int[] result2 = dijkstra(v1);
        int a1 = result2[n];  // v1 -> n
        int a2 = result2[v2]; // v1 -> v2
        int[] result3 = dijkstra(v2);
        int b1 = result3[n]; // v2 -> n
        int b2 = result3[v1]; // v2 -> v1
        int way1 = s1 + a2 + b1;
        int way2 = s2 + b2 + a1;
        int answer = Math.min(way1, way2);
        if (answer >= INF) {
            System.out.print(-1);
        } else {
            System.out.print(answer);
        }
    }

    private static int[] dijkstra(int start) {
        dist = new int[n + 1];
        Arrays.fill(dist, INF);
        dist[start] = 0;
        PriorityQueue<Point> q = new PriorityQueue<>();
        q.add(new Point(start, 0));
        while (!q.isEmpty()) {
            Point temp = q.poll();
            int current_node = temp.end;
            int current_dist = temp.weight;

            if (dist[current_node] < current_dist) {
                continue;
            }

            for (Point p : graph.get(current_node)) {
                int new_node = p.end;
                int new_dist = p.weight;
                int distance = current_dist + new_dist;
                if (distance < dist[new_node]) {
                    dist[new_node] = distance;
                    q.add(new Point(new_node, distance));
                }
            }
        }
        return dist;
    }

}







