package Algorany;

import java.util.*;
import java.io.*;

public class CodeTreeTour {

    static int Q;
    static ArrayList<int[]>[] graph;
    static int n; // 도시 개수
    static int m; // 간선 개수
    static int s = 0; // 출발지
    static HashMap<Integer, int[]> products = new LinkedHashMap<>();
    static int[] dist; // 다익스트라로 계산된 최단 거리

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Q = Integer.parseInt(br.readLine());

        for (int i = 0; i < Q; i++) {
            String[] order = br.readLine().split(" ");
            if (order[0].equals("100")) { // 랜드 건설
                n = Integer.parseInt(order[1]); // 도시 개수
                m = Integer.parseInt(order[2]); // 간선 개수
                graph = new ArrayList[n];
                for (int x = 0; x < n; x++) {
                    graph[x] = new ArrayList<>();
                }
                for (int j = 0; j < m; j++) {
                    int v = Integer.parseInt(order[3 + 3 * j]);
                    int u = Integer.parseInt(order[4 + 3 * j]);
                    int w = Integer.parseInt(order[5 + 3 * j]);
                    graph[v].add(new int[]{u, w});
                    graph[u].add(new int[]{v, w});
                }
                dist = dijkstra(s);
            } else if (order[0].equals("200")) { // 여행 상품 생성
                int id = Integer.parseInt(order[1]);
                int revenue = Integer.parseInt(order[2]);
                int dest = Integer.parseInt(order[3]);
                products.put(id, new int[]{revenue, dest});
            } else if (order[0].equals("300")) { // 여행 상품 취소
                int id = Integer.parseInt(order[1]);
                products.remove(id);
            } else if (order[0].equals("400")) { // 최적의 여행 상품 판매
                int profit = -1;
                int idx = -1;
                List<Integer> sortedKeys = new ArrayList<>(products.keySet());
                Collections.sort(sortedKeys); // 키 오름차순 정렬
                for (Integer key : sortedKeys) {
                    int[] value = products.get(key);
                    int result = bestProduct(value);
                    if (result > profit) {
                        profit = result;
                        idx = key;
                    }
                }
                System.out.println(idx);
                if (idx != -1) {
                    products.remove(idx);
                }
            } else if (order[0].equals("500")) { // 출발지 변경
                s = Integer.parseInt(order[1]);
                dist = dijkstra(s);
            }
        }
    }

    public static int[] dijkstra(int start) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;
        pq.add(new int[]{start, 0});

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int curNode = cur[0];
            int curDist = cur[1];

            if (curDist > dist[curNode]) continue;

            for (int[] neighbor : graph[curNode]) {
                int nextNode = neighbor[0];
                int nextDist = curDist + neighbor[1];

                if (nextDist < dist[nextNode]) {
                    dist[nextNode] = nextDist;
                    pq.add(new int[]{nextNode, nextDist});
                }
            }
        }
        return dist;
    }

    public static int bestProduct(int[] value) {
        int rev = value[0];
        int dest = value[1];
        int travelCost = dist[dest];
        if (travelCost == Integer.MAX_VALUE) {
            return Integer.MIN_VALUE; // 도달할 수 없는 경우
        }
        return rev - travelCost;
    }
}

