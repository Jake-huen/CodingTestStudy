package Algorany;

import java.util.*;
import java.io.*;

public class LionAndRabbit {

    static int n, m;
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    static int[] color;
    static boolean isBipartite; // 그래프가 이분그래프인지 여부
    static long totalCount1, totalCount2; // 두 그룹의 노드 수를 저장하는 변수

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());
        n = Integer.parseInt(str.nextToken());
        m = Integer.parseInt(str.nextToken());

        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            str = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(str.nextToken()) - 1;
            int y = Integer.parseInt(str.nextToken()) - 1;
            graph.get(x).add(y);
            graph.get(y).add(x);
        }

        color = new int[n];
        Arrays.fill(color, -1); // 아직 색칠되지 않은 노드들 초기화
        isBipartite = true;
        totalCount1 = 0;
        totalCount2 = 0;

        for (int i = 0; i < n; i++) {
            if (color[i] == -1) { // 아직 방문하지 않았다면
                if (!bfs(i)) { // BFS 수행
                    isBipartite = false;
                    break;
                }
            }
        }

        if (!isBipartite) { // 이분 그래프가 아니라면
            System.out.println("0");
        } else { // 이분 그래프인 경우
            System.out.println(totalCount1 * totalCount2 * 2); // 경우의 수를 모두 구하려면 두 개의 개수를 곱하고 양쪽 다 있을 수 있으므로 2를 또 곱해준다. 
        }
    }

    public static boolean bfs(int start) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        color[start] = 0;
        long count1 = 0, count2 = 0;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            if (color[node] == 0) {
                count1++;
            } else {
                count2++;
            }

            for (int neighbor : graph.get(node)) {
                if (color[neighbor] == -1) {
                    color[neighbor] = 1 - color[node]; // 방문하지 않은 노드면 반대로 칠함
                    queue.add(neighbor);
                } else if (color[neighbor] == color[node]) { // 같은 색이 인접해 있으면 이분 그래프가 아님.
                    return false;
                }
            }
        }

        totalCount1 += count1;
        totalCount2 += count2;
        return true;
    }
}
