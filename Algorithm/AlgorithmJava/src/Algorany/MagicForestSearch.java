package Algorany;

import java.util.*;
import java.io.*;

public class MagicForestSearch {
    static StringTokenizer str;
    static int R, C, K;
    static int[][] graph;
    // 0북 1동 2남 3서
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static boolean isIn(int col, int row) {
        if (0 <= col && col <= C && 0 <= row && row <= R) {
            return true;
        }
        return false;
    }

    public static int moveToExit(int[] cur) {
        int answer = 0;
        boolean[][] visited = new boolean[C + 1][R + 1];
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{cur[0], cur[1]});
        // 추가되는건 정령의 위치만.
        while (!q.isEmpty()) {
            int[] node = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = node[0] + dx[i];
                int ny = node[1] + dy[i];
                if (isIn(nx, ny) && !visited[nx][ny] && graph[nx][ny] != 0) {
                    visited[nx][ny] = true;
                    answer = Math.max(answer, nx);
                    if (graph[nx][ny] == 3) {
                        System.out.println("nx : " + nx + " ny : " + ny);
                        for (int j = 0; j < 4; j++) {
                            int nnx = nx + dx[j];
                            int nny = ny + dy[j];
                            if (isIn(nnx, nny) && !visited[nnx][nny] && (graph[nnx][nny] == 1 || graph[nnx][nny] == 3)) {
                                System.out.println("nnx : " + nnx + " nny : " + nny);
                                for (int k = 0; k < 4; k++) {
                                    int nnnx = nnx + dx[k];
                                    int nnny = nny + dy[k];
                                    if (isIn(nnnx, nnny) && !visited[nnnx][nnny] && graph[nnnx][nnny] == 2) {
                                        visited[nnnx][nnny] = true;
                                        q.add(new int[]{nnnx, nnny});
                                        System.out.println("추가 : " + nnnx + " " + nnny);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        System.out.println(answer);
        return answer;
    }

    public static int moveGolam(int row, int dir) {
        int[] cur = goDown(row, dir);
        if (cur[0] < 0) {
            for (int i = 0; i < 4; i++) {
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];
                if (isIn(nx, ny)) {
                    if (i == cur[2]) {
                        graph[nx][ny] = 3; // 출구
                    } else {
                        graph[nx][ny] = 1; // 골렘 위치
                    }
                }
            }
        } else {
            cur = goLeft(cur);
            cur = goRight(cur);
            graph[cur[0]][cur[1]] = 2; // 요정 위치
            for (int i = 0; i < 4; i++) {
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];
                if (isIn(nx, ny)) {
                    if (i == cur[2]) {
                        graph[nx][ny] = 3; // 출구
                    } else {
                        graph[nx][ny] = 1; // 골렘 위치
                    }
                }
            }
        }

        System.out.println("최종 위치 : " + cur[0] + " " + cur[1] + " " + cur[2]);

        if (isGolamOut()) {
            System.out.println("바깥에 있음");
            graph = new int[C + 1][R + 1];
            return 0;
        } else {
            return moveToExit(cur);
        }
    }

    public static int[] goDown(int row, int dir) {
        int col = 0; // 시작을 그래프 바로 위로 정함
        while (col <= C) {
            if (col > 0 && row + 1 <= R && row - 1 >= 1) {
                if (graph[col - 1][row + 1] > 0 || graph[col - 1][row - 1] > 0) {
                    break;
                }
            }
            if (graph[col][row] == 0) {
                col += 1;
            } else {
                break;
            }
        }
        col -= 2;
        return new int[]{col, row, dir};
    }

    public static boolean canMoveLeft(int[] cur) {
        int x = cur[0];
        int y = cur[1];
        if (x - 1 == -1 && y - 2 > 0 && x + 2 <= C) {
            if (graph[x][y - 2] == 0 && graph[x + 1][y - 1] == 0 && graph[x + 1][y - 2] == 0 && graph[x + 2][y - 1] == 0) {
                return true;
            }
        }
        if (y - 2 > 0 && x + 2 <= C && x - 1 >= 0) {
            if (graph[x][y - 2] == 0 && graph[x + 1][y - 1] == 0 && graph[x - 1][y - 1] == 0 && graph[x + 1][y - 2] == 0 && graph[x + 2][y - 1] == 0) {
                return true;
            }
        }
        return false;
    }

    public static int[] goLeft(int[] cur) {
        int[] newCur = {cur[0], cur[1], cur[2]};
//        for (int i = 0; i <= C; i++) {
//            for (int j = 0; j <= R; j++) {
//                System.out.println("i : " + i + " j " + j + " " + graph[i][j]);
//            }
//        }
        while (canMoveLeft(newCur)) {
            newCur[0] += 1;
            newCur[1] -= 1;
            newCur[2] = (newCur[2] + 3) % 4;
            System.out.println("MagicForestSearch.goLeft");
            System.out.println(newCur[0] + " " + newCur[1]);
        }
        System.out.println(newCur[0] + " " + newCur[1]);
        return newCur;
    }

    public static boolean canMoveRight(int[] cur) {
        int x = cur[0];
        int y = cur[1];
        if (x - 1 == -1 && y + 2 <= R && x + 2 <= C && y - 1 > 0) {
            if (graph[x][y + 2] == 0 && graph[x + 1][y + 1] == 0 && graph[x + 1][y + 2] == 0 && graph[x + 2][y + 1] == 0) {
                return true;
            }
        }
        if (y + 2 <= R && x + 2 <= C && x - 1 >= 0 && y - 1 > 0) {
            if (graph[x - 1][y - 1] == 0 && graph[x][y + 2] == 0 && graph[x + 1][y + 1] == 0 && graph[x + 1][y + 2] == 0 && graph[x + 2][y + 1] == 0) {
                return true;
            }
        }
        return false;
    }

    public static int[] goRight(int[] cur) {
        int[] newCur = {cur[0], cur[1], cur[2]};
        while (canMoveRight(newCur)) {
            newCur[0] += 1;
            newCur[1] += 1;
            newCur[2] = (newCur[2] + 1) % 4;
            System.out.println("MagicForestSearch.goRight");
            System.out.println(newCur[0] + " " + newCur[1]);
        }
        System.out.println(newCur[0] + " " + newCur[1]);
        return newCur;
    }

    public static boolean isGolamOut() {
        for (int i = 0; i <= R; i++) {
            if (graph[0][i] != 0) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = new StringTokenizer(br.readLine());
        int answer = 0;
        C = Integer.parseInt(str.nextToken());
        R = Integer.parseInt(str.nextToken());
        K = Integer.parseInt(str.nextToken()); // 정령 수

        graph = new int[C + 1][R + 1];
        for (int i = 0; i < K; i++) {
            str = new StringTokenizer(br.readLine());
            int row = Integer.parseInt(str.nextToken()); // 출발하는 행
            int dir = Integer.parseInt(str.nextToken()); // 출구 방향 정보

            answer += moveGolam(row, dir);
            System.out.println();
            if (isGolamOut()) { // 골렘이 밖에 나가있다면
                graph = new int[C + 1][R + 1];
            }
        }
        System.out.println(answer);
    }
}
/*
6 5 6
2 3
2 0
4 2
2 0
2 0
2 2

29

7 9 6
4 1
5 1
2 1
8 1
2 2
6 0

37
 */