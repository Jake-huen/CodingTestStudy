package Algorany;

import java.io.*;
import java.util.*;

public class CntIsland {

    static StringTokenizer str;
    static int w, h;
    static int[][] graph;
    static boolean[][] visited;
    static int answer;
    static int[] dx = {-1, -1, -1, 0, 0, 0, 1, 1, 1};
    static int[] dy = {-1, 0, 1, -1, 0, 1, -1, 0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            str = new StringTokenizer(br.readLine());
            w = Integer.parseInt(str.nextToken());
            h = Integer.parseInt(str.nextToken());
            if (w == 0 && h == 0) {
                return;
            }
            graph = new int[h][w];
            visited = new boolean[h][w];
            for (int i = 0; i < h; i++) {
                str = new StringTokenizer(br.readLine());
                for (int j = 0; j < w; j++) {
                    graph[i][j] = Integer.parseInt(str.nextToken());
                }
            }
            answer = 0;
            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    if (!visited[i][j] && graph[i][j] == 1) {
                        bfs(i, j);
                        answer += 1;
                    }
                }
            }
            System.out.println(answer);
        }
    }

    public static void bfs(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            for (int i = 0; i < 9; i++) {
                int nx = dx[i] + cur[0];
                int ny = dy[i] + cur[1];
                if (0 <= nx && nx < h && 0 <= ny && ny < w) {
                    if (!visited[nx][ny] && graph[nx][ny] == 1) {
                        visited[nx][ny] = true;
                        queue.add(new int[]{nx, ny});
                    }
                }
            }
        }
    }
}
