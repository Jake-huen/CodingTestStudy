package Algorany;

import java.util.*;
import java.io.*;

public class SpecialDistanceFindCity {

    static int n, m, k, x;
    static ArrayList<ArrayList<Integer>> graph;
    static List<Integer> answer;
    static int[] visited;

    public static void bfs(int node) {
        // 시작은 x
        Deque<Integer> queue = new ArrayDeque<>();
        queue.add(node);
        visited[node]++;
        while(!queue.isEmpty()){
            int now_node = queue.pollFirst();

            for (int destination : graph.get(now_node)) {
                if(visited[destination] == -1){
                    visited[destination] = visited[now_node] + 1;
                    queue.add(destination);
                }

//                System.out.println("visited[" +destination +"] : " + visited[destination]);
//                System.out.println("queue : " + queue);
//                System.out.println("-------------------------------");
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());
        // 도시 x에서 출발하여 최단 거리가 k인 도시들의 번호 출력
        n = Integer.parseInt(str.nextToken()); // 도시 개수
        m = Integer.parseInt(str.nextToken()); // 도로 개수
        k = Integer.parseInt(str.nextToken()); // 거리 정보
        x = Integer.parseInt(str.nextToken()); // 출발 정보
        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            str = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(str.nextToken());
            int end = Integer.parseInt(str.nextToken());
            graph.get(start).add(end);
//            System.out.println();
//            System.out.println("그래프 데이터 저장 : " + graph.get(start));
        }
        answer = new ArrayList<>();
        visited = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            visited[i] = -1;
        }
        //visited[x] = 0;
        bfs(x);
        for (int i = 0; i <= n; i++) {
            if(visited[i] == k) {
                answer.add(i);
            }
        }
        if (answer.isEmpty()) {
            System.out.println(-1);
        } else {
            for (int i : answer) {
                System.out.println(i);
            }
        }
    }
}
