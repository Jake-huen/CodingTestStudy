package Algorany;

import java.io.*;
import java.util.*;

public class PutNumberInDanji {

    static int n;
    static int[][] graph;
    static boolean[][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static ArrayList<Integer> answer = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < n; j++) {
                graph[i][j] = s.charAt(j) - 48;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j] && graph[i][j] == 1) {
                    answer.add(bfs(i, j));
                }
            }
        }
        answer.sort(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o1 - o2;
            }
        });
        System.out.println(answer.size());
        for (Integer integer : answer) {
            System.out.println(integer);
        }
    }

    public static int bfs(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});
        int total = 1;
        visited[x][y] = true;
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                    if (!visited[nx][ny]) {
                        if (graph[nx][ny] == 1) {
                            visited[nx][ny] = true;
                            total += 1;
                            queue.add(new int[]{nx, ny});
                        }
                    }
                }
            }
        }
        return total;
    }
}
