package Algorany;

import java.io.*;
import java.util.*;

public class Lab {

    static int n, m;
    static int[][] graph;
    static int answer = 0;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());
        n = Integer.parseInt(str.nextToken());
        m = Integer.parseInt(str.nextToken());
        graph = new int[n][m];
        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(s[j]); // 0은 빈 칸, 1은 벽, 2는 바이러스
            }
        }
        dfs(0);
        System.out.println(answer);
    }

    public static void dfs(int wallCount) {
        if (wallCount == 3) {
            bfs();
            return;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 0) {
                    graph[i][j] = 1;
                    dfs(wallCount + 1);
                    graph[i][j] = 0;
                }
            }
        }

    }

    public static void bfs() {
        int[][] new_graph = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                new_graph[i][j] = graph[i][j];
            }
        }
        // 일단 바이러스 다 퍼진 뒤에 안전지역 개수 구해야함.
        Queue<int[]> q = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (new_graph[i][j] == 2) {
                    q.add(new int[]{i, j});
                }
            }
        }

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int k = 0; k < 4; k++) {
                int nx = cur[0] + dx[k];
                int ny = cur[1] + dy[k];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (new_graph[nx][ny] == 0) {
                        new_graph[nx][ny] = 2;
                        q.add(new int[]{nx, ny});
                    }
                }
            }
        }

        int total = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (new_graph[i][j] == 0) {
                    total += 1;
                }
            }
        }
        answer = Math.max(answer, total);
    }
}
