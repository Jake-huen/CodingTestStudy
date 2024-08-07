package Algorany;

import java.util.*;
import java.io.*;

public class Sdoqu {
    static int[][] graph = new int[9][9];
    static boolean flag;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 9; i++) {
            String str = br.readLine();
            for (int j = 0; j < 9; j++) {
                graph[i][j] = Character.getNumericValue(str.charAt(j));
            }
        }
        // 해당 칸이 0일경우에 어떤걸 체크해야 하는가?! -> 같은 열 visited, 같은 행 visited, 같은 박스 visited 확인해야함.
        dfs(0);

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                System.out.print(graph[i][j]);
            }
            System.out.println();
        }
    }

    public static void dfs(int depth) {
        if (depth == 81) {
            flag = true;
            return;
        }
        int x = depth % 9;
        int y = depth / 9;
        if (graph[y][x] != 0) {
            dfs(depth + 1);
        } else {
            for (int i = 1; i <= 9; ++i) {
                if (!isVaild(y, x, i)) {
                    continue;
                }
                graph[y][x] = i;
                dfs(depth + 1);
                if (flag)
                    return;
                graph[y][x] = 0;
            }
        }
    }

    public static boolean isVaild(int y, int x, int n) {
        for (int i = 0; i < 9; ++i) {
            if (graph[y][i] == n || graph[i][x] == n) {
                return false;
            }
        }

        int yy = y / 3 * 3;
        int xx = x / 3 * 3;
        for (int i = yy; i < yy + 3; ++i) {
            for (int j = xx; j < xx + 3; ++j) {
                if (graph[i][j] == n) {
                    return false;
                }
            }
        }
        return true;
    }
}
