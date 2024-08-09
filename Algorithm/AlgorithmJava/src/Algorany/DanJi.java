package Algorany;

import java.io.*;
import java.util.*;

public class DanJi {
    static int n;
    static int[][] graph;
    static boolean[][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static ArrayList<Integer> answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split("");
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(s[j]);
            }
        }
        int cnt = 0;
        answer = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 1 && !visited[i][j]) {
                    bfs(i, j);
                    cnt += 1;
                }
            }
        }
        System.out.println(cnt);
        Collections.sort(answer);
        for (int i : answer) {
            System.out.println(i);
        }
    }

    public static void bfs(int col, int row) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{col, row});
        int result = 1;
        visited[col][row] = true;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + cur[0];
                int ny = dy[i] + cur[1];
                if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                    if (!visited[nx][ny] && graph[nx][ny] == 1) {
                        visited[nx][ny] = true;
                        q.add(new int[]{nx, ny});
                        result += 1;
                    }
                }
            }
        }
        answer.add(result);
    }
}
