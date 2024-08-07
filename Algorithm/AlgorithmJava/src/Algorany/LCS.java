package Algorany;

import java.io.*;

public class LCS {
    static String[] a, b;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        a = br.readLine().split("");
        b = br.readLine().split("");
        dp = new int[a.length + 1][b.length + 1];

        // dp 배열 채우기
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < b.length; j++) {
                if (a[i].equals(b[j])) {
                    dp[i + 1][j + 1] = dp[i][j] + 1;
                } else {
                    dp[i + 1][j + 1] = Math.max(dp[i + 1][j], dp[i][j + 1]);
                }
            }
        }

        // LCS 추적
        int x = a.length;
        int y = b.length;
        StringBuilder ans = new StringBuilder();
        while (x > 0 && y > 0) {
            if (a[x - 1].equals(b[y - 1])) {
                ans.append(a[x - 1]);
                x--;
                y--;
            } else if (dp[x - 1][y] == dp[x][y]) {
                x--;
            } else {
                y--;
            }
        }
        System.out.println(ans.length());
        System.out.println(ans.reverse().toString());
    }
}
