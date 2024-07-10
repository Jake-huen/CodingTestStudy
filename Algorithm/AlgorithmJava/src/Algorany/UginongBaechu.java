package Algorany;

import java.util.*;
import java.io.*;

public class UginongBaechu {

    static int t;
    static int m, n, k;
    static int[][] graph;
    static StringTokenizer str;
    static boolean[][] visited;
    static int answer;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            str = new StringTokenizer(br.readLine());
            m = Integer.parseInt(str.nextToken());
            n = Integer.parseInt(str.nextToken());
            k = Integer.parseInt(str.nextToken());
            answer = 0;
            graph = new int[n][m];
            for (int j = 0; j < k; j++) {
                str = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(str.nextToken());
                int y = Integer.parseInt(str.nextToken());
                graph[y][x] = 1;
            }
            visited = new boolean[n][m];
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    if (!visited[j][k] && graph[j][k] == 1) {
                        bfs(j, k);
                        answer += 1;
                    }
                }
            }
            System.out.println(answer);
        }
    }

    public static void bfs(int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x, y});
        visited[x][y] = true;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            visited[cur[0]][cur[1]] = true;
            for (int i = 0; i < 4; i++) {
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (!visited[nx][ny]) {
                        if (graph[nx][ny] == 1) {
                            visited[nx][ny] = true;
                            q.add(new int[]{nx, ny});
                        }
                    }
                }
            }
        }
    }
}
