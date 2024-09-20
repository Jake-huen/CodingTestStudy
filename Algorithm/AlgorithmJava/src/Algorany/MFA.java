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

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = new StringTokenizer(br.readLine());
        int answer = 0;
        C = Integer.parseInt(str.nextToken());
        R = Integer.parseInt(str.nextToken());
        K = Integer.parseInt(str.nextToken()); // 정령 수

        graph = new int[C + 3][R + 1];
        isExit = new boolean[C + 3][R + 1];
        for (int i = 1; i <= K; i++) {
            str = new StringTokenizer(br.readLine());
            int row = Integer.parseInt(str.nextToken()); // 출발하는 행
            int dir = Integer.parseInt(str.nextToken()); // 출구 방향 정보

            answer += moveGolam(0, row, dir, i);
            System.out.println();
        }
        System.out.println(answer);
    }

    public static boolean canGo(int col, int row) {
        return false;
    }

    public static void down(int col, int row, int dir, int id) {
        
    }
    
    public static boolean inRange(int col, int row){
        return false;
    }
    
    private static int moveGolam(int col, int row, int dir, int id) {
        if (canGo(col + 1, row)) {
            down(col + 1, row, dir, id);
        } else if (canGo(col + 1, row - 1)) {
            down(col + 1, row - 1, (dir + 3) % 4, id);
        } else if (canGo(col + 1, row + 1)) {
            down(col + 1, row + 1, (dir + 1) % 4, id);
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

    private static void resetMap() {
    }


}
