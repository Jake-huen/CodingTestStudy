package Algorany;

import java.io.*;
import java.util.*;

public class SafeZone {

    static int n;
    static int[][] graph;
    static int limit;
    static boolean[][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        // 물에 잠기지 않는 영역의 수
        // 일정 높이 이하의 지점은 물에 잠긴
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer str = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int temp = Integer.parseInt(str.nextToken());
                ;
                graph[i][j] = temp;
                if (temp > limit) {
                    limit = temp;
                }
            }
        }
        for (int i = 0; i <= limit; i++) {
            visited = new boolean[n][n];
            int total = 0;
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    if (!visited[j][k] && graph[j][k] > i) {
                        bfs(j, k, i);
                        total += 1;
                    }
                }
            }
            if(total > answer){
                answer = total;
            }
        }
        System.out.println(answer);
    }

    public static void bfs(int x, int y, int check) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});
        visited[x][y] = true;
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + cur[0];
                int ny = dy[i] + cur[1];
                if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                    if (!visited[nx][ny] && graph[nx][ny] > check) {
                        visited[nx][ny] = true;
                        queue.add(new int[]{nx, ny});
                    }
                }
            }
        }
    }

}
