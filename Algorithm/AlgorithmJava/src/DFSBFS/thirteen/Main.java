package DFSBFS.thirteen;

import java.util.*;

class Point {
    int x, y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static int n;
    static int[][] board;
    static int[] dx = {-1, 1, 0, 0, -1, -1, 1, 1};
    static int[] dy = {0, 0, -1, 1, -1, 1, -1, 1};

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        board = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = sc.nextInt();
            }
        }
        T.solution();
    }

    private void solution() {
        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 1) {
                    BFS(i, j);
                    answer += 1;
                }
            }
        }
        System.out.println(answer);
    }

    private void BFS(int x, int y) {
        Deque<Point> q = new ArrayDeque<>();
        q.add(new Point(x, y));
        board[x][y] = 2;
        while (!q.isEmpty()) {
            Point node = q.poll();
            for (int i = 0; i < 8; i++) {
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && board[nx][ny] == 1) {
                    board[nx][ny] = board[node.x][node.y] + 1;
                    q.add(new Point(nx, ny));
                }
            }
        }
    }
}
