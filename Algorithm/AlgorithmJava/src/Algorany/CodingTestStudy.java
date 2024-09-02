package Algorany;

import java.util.*;

public class CodingTestStudy {
    public int solution(int alp, int cop, int[][] problems) {
        int mAlp = 0, mCop = 0;
        for (int[] problem : problems) {
            mAlp = Math.max(mAlp, problem[0]);
            mCop = Math.max(mCop, problem[1]);
        }

        alp = Math.min(alp, mAlp);
        cop = Math.min(cop, mCop);

        int[][] dp = new int[mAlp + 1][mCop + 1];
        for (int i = 0; i <= mAlp; i++) {
            for (int j = 0; j <= mCop; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        dp[alp][cop] = 0;

        for (int i = alp; i <= mAlp; i++) {
            for (int j = cop; j <= mCop; j++) {
                // 1씩 증가시키는 경우 고려
                if (i + 1 <= mAlp) {
                    dp[i + 1][j] = Math.min(dp[i + 1][j], dp[i][j] + 1);
                }
                if (j + 1 <= mCop) {
                    dp[i][j + 1] = Math.min(dp[i][j + 1], dp[i][j] + 1);
                }

                for (int[] problem : problems) {
                    int alp_req = problem[0], cop_req = problem[1];
                    int alp_rwd = problem[2], cop_rwd = problem[3];
                    int cost = problem[4];

                    if (i >= alp_req && j >= cop_req) { // 문제를 풀 수 있는 기준을 넘겼을 때
                        int newAlp = Math.min(mAlp, i + alp_rwd);
                        int newCop = Math.min(mCop, j + cop_rwd);
                        dp[newAlp][newCop] = Math.min(dp[newAlp][newCop], dp[i][j] + cost);
                    }
                }
            }
        }
        System.out.println(dp[mAlp][mCop]);
        return dp[mAlp][mCop];
    }

    public static void main(String[] args) {
        CodingTestStudy cs = new CodingTestStudy();
        cs.solution(10, 10, new int[][]{{10, 15, 2, 1, 2}, {20, 20, 3, 3, 4}}); // 15
    }
}
