package Algorany;

import java.util.*;
import java.io.*;

public class CodeTreeTour {

    static int Q;
    static int[][] graph;
    static int n; // 도시 개수
    static int m; // 간선 개수
    static int s = 0; // 출발지
    static HashMap<Integer, int[]> products = new LinkedHashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Q = Integer.parseInt(br.readLine());

        for (int i = 0; i < Q; i++) {
            String[] order = br.readLine().split(" ");
            if (order[0].equals("100")) { // 랜드 건설
                n = Integer.parseInt(order[1]); // 도시 개수
                m = Integer.parseInt(order[2]); // 간선 개수
                graph = new int[n][n];
                for (int x = 0; x < n; x++) {
                    for (int y = 0; y < n; y++) {
                        graph[x][y] = Integer.MAX_VALUE;
                    }
                }
                for (int j = 0; j < m; j++) {
                    int v = Integer.parseInt(order[3 + 3 * j]);
                    int u = Integer.parseInt(order[4 + 3 * j]);
                    int w = Integer.parseInt(order[5 + 3 * j]);
                    graph[v][u] = Math.min(graph[v][u], w);
                    graph[u][v] = Math.min(graph[u][v], w);
                }
            } else if (order[0].equals("200")) { // 여행 상품 생성
                int id = Integer.parseInt(order[1]);
                int revenue = Integer.parseInt(order[2]);
                int dest = Integer.parseInt(order[3]);
                products.put(id, new int[]{revenue, dest});
                // 여행 상품 : (id, revenue, dest)
                // 얻게 되는 매출 : revenue, 도착지 : dest
            } else if (order[0].equals("300")) { // 여행 상품 취소
                int id = Integer.parseInt(order[1]);
                products.remove(id);
            } else if (order[0].equals("400")) { // 최적의 여행 상품 판매
                int profit = -1;
                int idx = -1;
                for (Map.Entry<Integer, int[]> integerEntry : products.entrySet()) {
                    int result = bestProduct(integerEntry.getValue());
                    System.out.println("key = " + integerEntry.getKey() + " value = " + result);
                    // System.out.println("result = " + result);
                    if (result > profit) {
                        profit = result;
                        idx = integerEntry.getKey();
                    }
                }
                if (idx != -1) {
                    products.remove(idx);
                }
                System.out.println(idx);
            } else if (order[0].equals("500")) { // 여행 상품의 출발지를 전부 s로 변경
                s = Integer.parseInt(order[1]);
            }
        }
    }

    public static int bestProduct(int[] value) {
        // 최적의 여행 상품 id를 출력하고, 관리 목록에서 제외함.
        // 조건에 맞는게 없으면 -1 출력
        // cost : 현재 여행 상품 출발지에서 도착지까지 도달하기 위한 최단거리
        // 이득 : revenue - cost, 이득이 최대인 상품을 우선적으로 고려. 이득이 동일하면 id가 작은 상품.
        // 이득이 음수라면 판매 불가 상품 / 도착지까지 갈 수 없다면 판매 불가 상품
        int rev = value[0];
        int dest = value[1];
        //System.out.println("도착지 : " + dest);
        Queue<int[]> q = new LinkedList<>();
        boolean[] visited = new boolean[n];
        q.add(new int[]{s, 0});
        //System.out.println("start = " + s);
        visited[s] = true;
        int answer = -1;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int next = cur[0];
            int cost = cur[1];
            if (next == dest) {
                System.out.println("dest = " + dest);
                answer = Math.max(answer, rev - cost);
            }
            for (int i = 0; i < n; i++) {
                if (graph[cur[0]][i] != Integer.MAX_VALUE && !visited[i]) {
                    visited[i] = true;
                    q.add(new int[]{i, cur[1] + graph[cur[0]][i]});
                }
            }
        }
        if (answer == -1) {
            return -1;
        } else {
            return answer;
        }
    }
}
