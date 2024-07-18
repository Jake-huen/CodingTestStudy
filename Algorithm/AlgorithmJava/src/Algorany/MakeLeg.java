package Algorany;

import java.io.*;
import java.util.*;

public class MakeLeg {
    static int n, m;
    static int[][] graph;
    static int[][] map;
    static boolean[][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> {
        return o1[2] - o2[2];
    });
    static int[] parents;
    static int idx = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());
        n = Integer.parseInt(str.nextToken());
        m = Integer.parseInt(str.nextToken());
        graph = new int[n][m];
        map = new int[n][m];
        visited = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(s[j]);
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 1 && !visited[i][j]) {
                    idx += 1;
                    bfs(i, j, idx);
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] != 0) {
                    makeBridge(i, j, map[i][j]);
                }
            }
        }

        parents = new int[idx];
        for (int i = 0; i < idx; i++) {
            parents[i] = i;
        }

        // 우선순위 큐의 요소들을 우선순위 순서대로 출력
//        for (int[] bridge : pq) {
//            System.out.println(bridge[0] + " " + bridge[1] + " " + bridge[2]);
//        }

        int answer = shortestPath();
        System.out.println(answer == 0 ? -1 : answer);
    }

    public static void bfs(int x, int y, int number) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y, number});
        map[x][y] = number;
        visited[x][y] = true;
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + cur[0];
                int ny = dy[i] + cur[1];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (!visited[nx][ny] && graph[nx][ny] == 1) {
                        visited[nx][ny] = true;
                        map[nx][ny] = cur[2];
                        queue.add(new int[]{nx, ny, cur[2]});
                    }
                }
            }
        }
    }

    public static void makeBridge(int x, int y, int number) {
        for (int i = 0; i < 4; i++) { // 방향 4가지
            int nx = x;
            int ny = y;
            int bridgeLen = 0;
            while (true) {
                nx += dx[i];
                ny += dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (map[nx][ny] == number) break; // 같은 섬이면 종료
                    if (map[nx][ny] > 0) { // 다른 섬 도착
                        if (bridgeLen > 1) {
                            pq.add(new int[]{number - 1, map[nx][ny] - 1, bridgeLen});
                        }
                        break;
                    }
                    bridgeLen++;
                } else {
                    break; // 범위를 벗어나면 종료
                }
            }
        }
    }

    public static int shortestPath() {
        int sum = 0;
        int count = 0;
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int from = cur[0];
            int to = cur[1];
            int cost = cur[2];
            if (find(from) != find(to)) { // 사이클이 아닌 경우
                sum += cost;
                union(from, to);
                count++;
            }
        }
        // 모든 섬이 연결되었는지 확인
        if (count == idx - 1) {
            return sum;
        } else {
            return 0;
        }
    }

    public static int find(int x) {
        if (parents[x] == x) return x;
        return parents[x] = find(parents[x]); // 경로 압축
    }

    public static void union(int x, int y) {
        x = find(x);
        y = find(y);
        if (x < y) {
            parents[y] = x;
        } else {
            parents[x] = y;
        }
    }
}
