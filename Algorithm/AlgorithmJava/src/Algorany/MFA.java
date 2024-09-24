package Algorany;

import java.util.*;
import java.io.*;

public class MFA {

    static StringTokenizer str;
    static int R, C, K;
    static int[][] graph;
    static boolean[][] isExit;
    // 0북 1동 2남 3서
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = new StringTokenizer(br.readLine());
        C = Integer.parseInt(str.nextToken());
        R = Integer.parseInt(str.nextToken());
        K = Integer.parseInt(str.nextToken()); // 정령 수

        graph = new int[C + 3][R + 1];
        isExit = new boolean[C + 3][R + 1];
        for (int i = 1; i <= K; i++) {
            str = new StringTokenizer(br.readLine());
            int row = Integer.parseInt(str.nextToken()) - 1; // 출발하는 열
            int dir = Integer.parseInt(str.nextToken()); // 출구 방향 정보

            moveGolam(0, row, dir, i);
        }
        System.out.println(answer);
    }

    public static boolean canGo(int col, int row) {
        boolean flag = 0 <= row - 1 && row + 1 < R && col + 1 < C + 3;
        flag = flag && (graph[col - 1][row - 1] == 0);
        flag = flag && (graph[col - 1][row] == 0);
        flag = flag && (graph[col - 1][row + 1] == 0);
        flag = flag && (graph[col][row - 1] == 0);
        flag = flag && (graph[col][row] == 0);
        flag = flag && (graph[col][row + 1] == 0);
        flag = flag && (graph[col + 1][row] == 0);

        return flag;
    }


    public static boolean inRange(int col, int row) {
        return 3 <= col && col < C + 3 && 0 <= row && row < R;
    }

    private static void moveGolam(int col, int row, int dir, int id) {
        if (canGo(col + 1, row)) {
            moveGolam(col + 1, row, dir, id);
        } else if (canGo(col + 1, row - 1)) {
            moveGolam(col + 1, row - 1, (dir + 3) % 4, id);
        } else if (canGo(col + 1, row + 1)) {
            moveGolam(col + 1, row + 1, (dir + 1) % 4, id);
        } else {
            if (!inRange(col - 1, row - 1) || !inRange(col + 1, row + 1)) {
                resetMap();
            } else {
                // 정착
                graph[col][row] = id;
                for (int k = 0; k < 4; k++) {
                    graph[col + dx[k]][row + dy[k]] = id;
                }
                isExit[col + dx[dir]][row + dy[dir]] = true;
                answer += bfs(col, row) - 3 + 1;
            }
        }
    }

    private static int bfs(int col, int row) {
        int result = col;
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visit = new boolean[C + 3][R + 1];
        q.offer(new int[]{col, row});
        visit[col][row] = true;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int k = 0; k < 4; k++) {
                int ny = cur[0] + dy[k];
                int nx = cur[1] + dx[k];

                if (inRange(ny, nx) && !visit[ny][nx] && (graph[ny][nx] == graph[cur[0]][cur[1]] || graph[ny][nx]!=0 && isExit[cur[0]][cur[1]])){
                    q.add(new int[]{ny, nx});
                    visit[ny][nx] = true;
                    result = Math.max(result, ny);
                }
            }
        }
        return result;
    }

    private static void resetMap() {
        for (int i = 0; i < C + 3; i++) {
            for (int j = 0; j <= R; j++) {
                graph[i][j] = 0;
                isExit[i][j] = false;
            }
        }
    }


}
