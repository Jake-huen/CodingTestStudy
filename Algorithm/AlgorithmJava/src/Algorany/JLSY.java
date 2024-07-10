package Algorany;

import java.io.*;
import java.util.*;

public class JLSY {
    static int n;
    static int[][] graph;
    static int[][] j_graph;
    static boolean[][] visited;
    static boolean[][] j_visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        j_graph = new int[n][n];
        visited = new boolean[n][n];
        j_visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < n; j++) {
                if (s.charAt(j) == 'R') {
                    graph[i][j] = 1;
                    j_graph[i][j] = 1;
                } else if (s.charAt(j) == 'B') {
                    graph[i][j] = 2;
                    j_graph[i][j] = 2;
                } else if (s.charAt(j) == 'G') {
                    graph[i][j] = 3;
                    j_graph[i][j] = 1;
                }
            }
        }
        int[] ans = new int[2];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] > 0 && !visited[i][j]) {
                    bfs(i, j, graph[i][j]);
                    ans[0] += 1;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j_graph[i][j] > 0 && !j_visited[i][j]) {
                    j_bfs(i, j, j_graph[i][j]);
                    ans[1] += 1;
                }
            }
        }
        System.out.println(ans[0] + " " + ans[1]);

    }

    public static void bfs(int x, int y, int color) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x, y});
        visited[x][y] = true;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];
                if(0<=nx && nx<n && 0<=ny && ny<n){
                    if (!visited[nx][ny]) {
                        if (graph[nx][ny] == color) {
                            visited[nx][ny] = true;
                            q.add(new int[]{nx, ny});
                        }
                    }
                }
            }
        }
    }

    public static void j_bfs(int x, int y, int color) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x, y});
        j_visited[x][y] = true;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];
                if(0<=nx && nx<n && 0<=ny && ny<n){
                    if (!j_visited[nx][ny]) {
                        if (j_graph[nx][ny] == color) {
                            j_visited[nx][ny] = true;
                            q.add(new int[]{nx, ny});
                        }
                    }
                }
            }
        }
    }
}
