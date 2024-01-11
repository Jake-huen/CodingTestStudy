package DFSBFS.tenth;

import java.util.*;

public class Main {

    static int[][] map;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static boolean[][] check;
    static int ans = 0;
    static int[][] answer;

    class Point {
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        map = new int[7][7];
        answer = new int[7][7];
        check = new boolean[7][7];
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                map[i][j] = sc.nextInt();
                check[i][j] = false;
            }
        }
        map[0][0] = 1;
        T.DFS(0, 0);
        System.out.println(ans);
//        for (int i = 0; i < 7; i++) {
//            for (int j = 0; j < 7; j++) {
//                T.BFS();
//            }
//        }
//        T.BFS();
//        System.out.println(answer[6][6]);
    }

    private void DFS(int x, int y) {
        if (x == 6 && y == 6) {
            ans += 1;
        } else {
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < 7 && ny >= 0 && ny < 7) {
                    if (map[nx][ny] == 0) {
                        map[nx][ny] = 1;
                        DFS(nx, ny);
                        map[nx][ny] = 0;
                    }
                }
            }
        }
    }

    private void BFS() {
        Deque<Point> queue = new ArrayDeque<>();
        queue.add(new Point(0, 0));
        answer[0][0] = 1;
        check[0][0] = true;
        while (!queue.isEmpty()) {
            Point cur = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if (nx >= 0 && nx < 7 && ny >= 0 && ny < 7) {
                    if (!check[nx][ny] && map[nx][ny] == 0) {
                        queue.add(new Point(nx, ny));
                        answer[nx][ny] = answer[cur.x][cur.y] + 1;
                        check[nx][ny] = true;
                    }
                }
            }
        }
    }
}
