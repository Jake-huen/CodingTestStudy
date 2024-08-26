package Algorany;

import java.util.*;
import java.io.*;

public class RicochatRobot {

    class Point {
        int x, y, cnt;

        Point() {
        }

        Point(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }

    public int solution(String[] board) {
        int answer = 0;
        // board .(빈공간) R(로봇 처음 위치) D(장애물 위치) G(목표 위치)
        int col = board.length;
        int row = board[0].length();
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        boolean[][] visited = new boolean[col][row];
        Point start = new Point();
        Point goal = new Point();
        for (int i = 0; i < col; i++) {
            for (int j = 0; j < row; j++) {
                if (board[i].charAt(j) == 'R') {
                    start.x = i;
                    start.y = j;
                }
                if (board[i].charAt(j) == 'G') {
                    goal.x = i;
                    goal.y = j;
                }
            }
        }
        Queue<Point> queue = new LinkedList<>();
        queue.add(new Point(start.x, start.y, 0));
        visited[start.x][start.y] = true;
        while (!queue.isEmpty()) {
            Point cur = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = cur.x;
                int ny = cur.y;

                while (true) {
                    int nextX = nx + dx[i];
                    int nextY = ny + dy[i];

                    if (nextX < 0 || nextX >= col || nextY < 0 || nextY >= row || board[nextX].charAt(nextY) == 'D') {
                        break;
                    }
                    nx = nextX;
                    ny = nextY;
                }

                if (board[nx].charAt(ny) == 'G') {
                    return cur.cnt + 1;
                }
                if (!visited[nx][ny]) {
                    queue.add(new Point(nx, ny, cur.cnt + 1));
                    visited[nx][ny] = true;
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        RicochatRobot rb = new RicochatRobot();
        System.out.println(rb.solution(new String[]{"...D..R", ".D.G...", "....D.D", "D....D.", "..D...."})); // 7
        System.out.println(rb.solution(new String[]{".D.R", "....", ".G..", "...D"})); // -1
    }
}
