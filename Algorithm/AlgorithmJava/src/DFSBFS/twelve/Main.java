package DFSBFS.twelve;

import java.util.*;

class Point {
    int x, y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static int n; // 세로칸의 수
    static int m; // 가로칸의 수
    static int[][] tomato;
    static int[][] visited;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, -1, 0, 1};

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        m = sc.nextInt(); // 가로칸의 수
        n = sc.nextInt(); // 세로칸의 수
        tomato = new int[n][m];
        visited = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                tomato[i][j] = sc.nextInt();
            }
        }
        T.solution(tomato);
    }

    private void solution(int[][] tomato) {
        Deque<Point> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) { // 익은 토마토 넣기
            for (int j = 0; j < m; j++) {
                if (tomato[i][j] == 1) {
                    q.addLast(new Point(i, j));
                }
            }
        }
        while (!q.isEmpty()) {
            Point node = q.pollFirst();
            for (int i = 0; i < 4; i++) {
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && tomato[nx][ny] == 0) {
                    tomato[nx][ny] = 1;
                    visited[nx][ny] = visited[node.x][node.y] + 1;
                    q.addLast(new Point(nx, ny));
                }
            }
        }
        boolean flag = true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (tomato[i][j] == 0) {
                    flag = false;
                    break;
                }
            }
        }
        int answer = Integer.MIN_VALUE;
        if (flag) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    answer = Math.max(answer, visited[i][j]);
                }
            }
            System.out.println(answer);
        } else {
            System.out.println(-1);
        }
    }
}
