package daily.taxi.floyd;

import java.util.Arrays;

public class Main {

    public static int solution(int n, int s, int a, int b, int[][] fares) {
        int[][] cost = new int[n + 1][n + 1];

        for (int i = 1; i <= n; i++) {
            Arrays.fill(cost[i], 200000);
        }

        for (int[] fare : fares) {
            int start = fare[0];
            int end = fare[1];
            int val = fare[2];
            cost[start][end] = val;
            cost[end][start] = val;
        }

        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (i != j) {
                        cost[i][j] = Math.min(cost[i][j], cost[i][k] + cost[k][j]);
                    }
                }
            }
        }
        for (int i = 1; i <= n; i++) {
            cost[i][i] = 0;
        }

        int answer = Integer.MAX_VALUE;
        for (int i = 1; i <= n; i++) {
            answer = Math.min(answer, cost[s][i] + cost[i][a] + cost[i][b]);
        }

        return answer;
    }


    public static void main(String[] args) {
        Main T = new Main();
        System.out.println(T.solution(6, 4, 6, 2, new int[][]{{4, 1, 10}, {3, 5, 24}, {5, 6, 2}, {3, 1, 41}, {5, 1, 24}, {4, 6, 50}, {2, 4, 66}, {2, 3, 22}, {1, 6, 25}}));
        System.out.println(T.solution(7, 3, 4, 1, new int[][]{{5, 7, 9}, {4, 6, 4}, {3, 6, 1}, {3, 2, 3}, {2, 1, 6}}));
    }
}
