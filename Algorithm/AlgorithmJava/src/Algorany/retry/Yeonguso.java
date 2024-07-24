package Algorany.retry;

import java.util.*;
import java.io.*;

public class Yeonguso {
    static int n, m;
    static StringTokenizer str;
    static int[][] graph;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int answer = 0;
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = new StringTokenizer(br.readLine());
        n = Integer.parseInt(str.nextToken());
        m = Integer.parseInt(str.nextToken());
        graph = new int[n][m];

        for (int i = 0; i < n; i++) {
            str = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(str.nextToken());
            }
        }
        // 벽의 개수는 3개 놓아야 함.
        dfs(0);
        System.out.println(answer);

    }

    public static void dfs(int wall) {
        if (wall == 3) {
            answer = Math.max(answer, bfs());
            return;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 0) {
                    graph[i][j] = 1;
                    dfs(wall + 1);
                    graph[i][j] = 0;
                }
            }
        }
    }

    public static int bfs() {
        Queue<int[]> q = new LinkedList<>();
        int[][] map = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                map[i][j] = graph[i][j];
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 2) {
                    q.add(new int[]{i, j});
                }
            }
        }
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (map[nx][ny] == 0) {
                        map[nx][ny] = 2;
                        q.add(new int[]{nx, ny});
                    }
                }
            }
        }
        int temp = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                //System.out.println(i + " " + j + " " + map[i][j]);
                if (map[i][j] == 0) {
                    temp += 1;
                }
            }
        }
        //System.out.println(temp);
        return temp;
    }
}
