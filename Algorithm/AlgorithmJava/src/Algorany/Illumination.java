package Algorany;

import java.io.*;
import java.util.*;

public class Illumination {

    static int w, h;
    static int[][] graph;
    static boolean[][] visited;
    static int[][] result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());
        w = Integer.parseInt(str.nextToken());
        h = Integer.parseInt(str.nextToken());
        graph = new int[h + 2][w + 2];
        result = new int[h + 2][w + 2];
        visited = new boolean[h + 2][w + 2];
        for (int i = 1; i <= h; i++) {
            str = new StringTokenizer(br.readLine());
            for (int j = 1; j <= w; j++) {
                graph[i][j] = Integer.parseInt(str.nextToken());
            }
        }
        // col이 홀수냐 짝수냐에 따라서 이동할 수 있는 범위도 달라짐.
        BFS(0, 0);
    }

    public static void BFS(int x, int y) {
        // 좌, 좌상, 우상, 우, 우하, 좌하
        int[][] oddDir = {{0, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}}; // 홀수행
        int[][] evenDir = {{0, -1}, {-1, -1}, {-1, 0}, {0, 1}, {1, 0}, {1, -1}}; // 짝수행

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});
        visited[x][y] = true;

        while (!queue.isEmpty()) {
            int[] temp = queue.poll();
            for (int dir = 0; dir < 6; dir++) {
                int nx = 0;
                int ny = 0;
                if (temp[0] % 2 == 0) { // 짝수번째 열
                    nx = temp[0] + evenDir[dir][0];
                    ny = temp[1] + evenDir[dir][1];
                } else {
                    nx = temp[0] + oddDir[dir][0];
                    ny = temp[1] + oddDir[dir][1];
                }

                if (0 <= nx && nx <= h + 1 && 0 <= ny && ny <= w + 1) {
                    if (!visited[nx][ny]) {
                        if (graph[nx][ny] == 0) {
                            visited[nx][ny] = true;
                            queue.add(new int[]{nx, ny});
                        }
                    }
                }
            }
        }
        int sum = 0;
        for (int i = 1; i <= h; i++) {
            for (int j = 1; j <= w; j++) {
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
}
