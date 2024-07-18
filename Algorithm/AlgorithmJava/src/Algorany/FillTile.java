package Algorany;

import java.io.*;
import java.util.*;

public class FillTile {
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        int[] dp = new int[n + 1];
        // n = 2 -> 3가지, n = 4 -> 3*3 + 2
        dp[1] = 0;
        dp[2] = 3;
        for (int i = 4; i <= n; i += 2) {
            dp[i] = dp[i - 2] * 3; // 2개짜리 만드는 경우의 수는 3가지
            for (int j = i - 4; j >= 0; j -= 2) {
                dp[i] += dp[j] * 2; // 특별 타일 갯수
            }
        }
        System.out.println(dp[n]);
    }
}
