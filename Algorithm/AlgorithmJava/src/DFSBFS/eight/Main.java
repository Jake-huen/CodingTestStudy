package DFSBFS.eight;

import java.util.*;

public class Main {
    static int n, f;
    boolean flag = false;
    static int[] pm;
    static int[] b;
    static int[][] dy;
    static int[] ch;

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt(); // 4
        f = sc.nextInt(); // 16
        pm = new int[n];
        b = new int[n];
        ch = new int[n + 1];
        dy = new int[n + 1][n + 1];
        for (int i = 0; i < n; i++) {
            b[i] = T.Comb(n - 1, i);
        }
        T.DFS(0, 0);
    }

    private int Comb(int n, int r) {
        if (dy[n][r] > 0) {
            return dy[n][r];
        }
        if (n == r || r == 0) {
            return 1;
        } else {
            return dy[n][r] = Comb(n - 1, r - 1) + Comb(n - 1, r);
        }
    }

    private void DFS(int L, int sum) {
        if (flag) {
            return;
        }
        if (L == n) {
            if (sum == f) {
                for (int x : pm) {
                    System.out.print(x+" ");
                }
                System.out.println();
                flag = true;
            }
        } else {
            for (int i = 1; i <= n; i++) {
                if (ch[i] == 0) {
                    ch[i] = 1;
                    pm[L] = i;
                    DFS(L + 1, sum + (pm[L] * b[L]));
                    ch[i] = 0;
                }
            }
        }
    }
}
