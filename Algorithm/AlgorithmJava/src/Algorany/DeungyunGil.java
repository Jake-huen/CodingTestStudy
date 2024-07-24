package Algorany;

import java.util.*;

import static java.util.Arrays.compare;

public class DeungyunGil {

    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        // m이 세로, n이 가로
        int[][] graph = new int[n + 1][m + 1];
        int mod = 1000000007;

        for (int[] puddle : puddles) {
            graph[puddle[1]][puddle[0]] = -1;
        }
        graph[1][1] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (graph[i][j] == -1) continue;
                if (graph[i - 1][j] > 0) {
                    graph[i][j] += graph[i - 1][j] % mod;
                }
                if (graph[i][j - 1] > 0) {
                    graph[i][j] += graph[i][j - 1] % mod;
                }
            }
        }

        return graph[n][m]%mod;
    }

    public static void main(String[] args) {
        DeungyunGil d = new DeungyunGil();
        System.out.println(d.solution(4, 3, new int[][]{{2, 2}}));
    }

}
