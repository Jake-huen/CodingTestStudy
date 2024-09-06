package Algorany;

import java.util.*;

public class GetItem {

    static char map[][] = new char[101][101];

    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        // 이 영역이 지나갈 수 있는 영역인지 판단해야함.
        for (int i = 0; i < rectangle.length; i++) {
            int y1 = rectangle[i][1];
            int x1 = rectangle[i][0];
            int y2 = rectangle[i][3];
            int x2 = rectangle[i][2];
            draw(y1 * 2, x1 * 2, y2 * 2, x2 * 2);
        }

        return bfs(characterY * 2, characterX * 2, itemY * 2, itemX * 2);
    }

    public int bfs(int Y, int X, int findY, int findX) {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{Y, X, 0});
        boolean[][] visited = new boolean[101][101];
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            if (cur[0] == findY && cur[1] == findX) {
                return cur[2] / 2;
            }

            for (int i = 0; i < 4; i++) {
                int ny = cur[0] + dy[i];
                int nx = cur[1] + dx[i];
                if (0 <= ny && ny < map.length && 0 <= nx && nx < map[0].length) {
                    if (!visited[ny][nx] && map[ny][nx] == '2') {
                        visited[ny][nx] = true;
                        q.add(new int[]{ny, nx, cur[2] + 1});
                    }
                }
            }
        }
        return 0;
    }


    private void draw(int y1, int x1, int y2, int x2) {
        for (int i = y1; i <= y2; i++) {
            for (int j = x1; j <= x2; j++) {
                if (map[i][j] == '1') continue;
                map[i][j] = '1';
                if (i == y1 || i == y2 || j == x1 || j == x2) {
                    map[i][j] = '2';
                }
            }
        }

    }

    public static void main(String[] args) {
        GetItem gi = new GetItem();
        System.out.println(gi.solution(new int[][]{{1, 1, 7, 4}, {3, 2, 5, 5}, {4, 3, 6, 9}, {2, 6, 8, 8}}, 1, 3, 7, 8)); // 17
    }
}
