package Algorany;

import java.util.*;

public class GameMap {

    public int solution(int[][] maps) {
        int answer = 0;
        int col = maps.length;
        int row = maps[0].length;
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        int[][] graph = new int[col][row];
        boolean[][] visited = new boolean[col][row];
        for (int i = 0; i < col; i++) {
            for (int j = 0; j < row; j++) {
                graph[i][j] = maps[i][j];
            }
        }

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0});
        visited[0][0] = true;
        while (!q.isEmpty()) {

            int[] cur = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];
                if (0 <= nx && nx < col && 0 <= ny && ny < row) {
                    if (maps[nx][ny] == 1 && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        graph[nx][ny] += graph[cur[0]][cur[1]];
                        q.add(new int[]{nx, ny});
                    }
                }
            }
        }

        if (graph[col - 1][row - 1] <= 1) {
            return -1;
        } else {
            answer = graph[col - 1][row - 1];
        }

        return answer;
    }

    public static void main(String[] args) {
        GameMap gm = new GameMap();
        System.out.println(gm.solution(new int[][]{{1, 0, 1, 1, 1}, {1, 0, 1, 0, 1}, {1, 0, 1, 1, 1}, {1, 1, 1, 0, 1}, {0, 0, 0, 0, 1}})); // 11
    }
}
