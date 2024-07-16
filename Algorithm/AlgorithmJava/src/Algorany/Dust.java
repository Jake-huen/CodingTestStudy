package Algorany;

import java.util.*;
import java.io.*;

public class Dust {
    static int r, c, t;
    static int[][] graph;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static Node topAir;
    static Node bottomAir;
    static Deque<Node> dust;
    static int answer = 0;

    static class Node {
        int x;
        int y;
        int cost;

        Node(int x, int y, int cost) {
            this.x = x;
            this.y = y;
            this.cost = cost;
        }

        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());
        r = Integer.parseInt(str.nextToken());
        c = Integer.parseInt(str.nextToken());
        t = Integer.parseInt(str.nextToken());
        graph = new int[r][c];
        dust = new LinkedList<>();
        for (int i = 0; i < r; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < c; j++) {
                graph[i][j] = Integer.parseInt(s[j]); // -1: 공기청정기
                if (graph[i][j] == -1) {
                    if (topAir == null) {
                        topAir = new Node(i, j);
                    } else {
                        bottomAir = new Node(i, j);
                    }
                } else if (graph[i][j] > 0) {
                    dust.add(new Node(i, j, graph[i][j])); // x좌표, y좌표, cost
                }
            }
        }
        for (int i = 0; i < t; i++) {
            graph = dustSpread();
            airConditioner();
        }
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (graph[i][j] > 0) {
                    answer += graph[i][j];
                }
            }
        }
        System.out.println(answer);
    }

    public static int[][] dustSpread() {
        int[][] newMap = new int[50][50];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (graph[i][j] == -1) {
                    newMap[i][j] = -1;
                    continue;
                }
                newMap[i][j] += graph[i][j];
                for (int k = 0; k < 4; k++) {
                    int nx = dx[k] + i;
                    int ny = dy[k] + j;
                    if (nx < 0 || nx >= r || ny < 0 || ny >= c) {
                        continue;
                    }
                    if (graph[nx][ny] == -1) {
                        continue;
                    }
                    newMap[nx][ny] += (graph[i][j] / 5);
                    newMap[i][j] -= (graph[i][j] / 5);
                }
            }
        }
        return newMap;
    }

    public static void airConditioner() {
        // 위쪽 청소기 -> 시계 반대
        int top = topAir.x; // 위쪽의 x좌표
        for (int x = top - 1; x > 0; x--) { // 왼쪽 사이드
            graph[x][0] = graph[x - 1][0];
        }
        for (int y = 0; y < c - 1; y++) { // 위쪽 사이드
            graph[0][y] = graph[0][y + 1];
        }
        for (int x = 0; x < top; x++) { // 오른쪽 사이드
            graph[x][c - 1] = graph[x + 1][c - 1];
        }
        for (int y = c - 1; y > 1; y--) { // 왼쪽 사이드
            graph[top][y] = graph[top][y - 1];
        }
        graph[top][1] = 0;
        // 아래쪽 청소기 -> 시계 방향
        int bottom = bottomAir.x;
        for (int x = bottom + 1; x < r - 1; x++) { // 왼쪽 사이드
            graph[x][0] = graph[x + 1][0];
        }
        for (int y = 0; y < c - 1; y++) { // 아래쪽 사이드
            graph[r - 1][y] = graph[r - 1][y + 1];
        }
        for (int x = r - 1; x > bottom; x--) { // 오른쪽 사이드
            graph[x][c - 1] = graph[x - 1][c - 1];
        }
        for (int y = c - 1; y > 1; y--) { // 위쪽 사이드
            graph[bottom][y] = graph[bottom][y - 1];
        }

        graph[bottom][1] = 0;
    }
}
