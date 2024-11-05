package Algorany;

import java.util.*;
import java.io.*;

public class Illumination2 {

    static int W, H;
    static int[][] graph;
    static boolean[][] visited;
    // 좌 좌상 우상 우 우하 좌하
    static int[][] oddDir = {{0, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}};
    static int[][] evenDir = {{0, -1}, {-1, -1}, {-1, 0}, {0, 1}, {1, 0}, {1, -1}};

    public static void bfs(int c, int r) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{c, r});
        visited[c][r] = true;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int dir = 0; dir < 6; dir++) {
                int nx;
                int ny;
                if (cur[0] % 2 == 0) {
                    nx = cur[0] + evenDir[dir][0];
                    ny = cur[1] + evenDir[dir][1];
                } else {
                    nx = cur[0] + oddDir[dir][0];
                    ny = cur[1] + oddDir[dir][1];
                }

                if (0 <= nx && nx <= H + 1 && 0 <= ny && ny <= W + 1) {
                    if (!visited[nx][ny]) {
                        if(graph[nx][ny] == 0){
                            visited[nx][ny] = true;
                            q.add(new int[]{nx, ny});
                        }
                    }
                }
            }
        }
        int sum = 0;
        for (int i = 1; i <= H; i++) {
            for (int j = 1; j <= W; j++) {
                if (graph[i][j] == 0) {
                    continue;
                }
                for (int t = 0; t < 6; t++) {
                    int nx;
                    int ny;
                    if (i % 2 == 0) {
                        nx = i + evenDir[t][0];
                        ny = j + evenDir[t][1];
                    } else {
                        nx = i + oddDir[t][0];
                        ny = j + oddDir[t][1];
                    }
                    if (visited[nx][ny]) {
                        sum += 1;
                    }
                }
            }
        }
        System.out.println(sum);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        W = Integer.parseInt(str[0]); // r
        H = Integer.parseInt(str[1]); // c
        graph = new int[H + 2][W + 2];
        visited = new boolean[H + 2][W + 2];
        for (int i = 1; i <= H; i++) {
            StringTokenizer temp = new StringTokenizer(br.readLine());
            for (int j = 1; j <= W; j++) {
                graph[i][j] = Integer.parseInt(temp.nextToken()); // 건물이 있으면 1
            }
        }
        bfs(0, 0);
    }
}
