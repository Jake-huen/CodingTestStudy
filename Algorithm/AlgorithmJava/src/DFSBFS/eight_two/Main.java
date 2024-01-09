package DFSBFS.eight_two;

import java.util.*;

public class Main {

    static int n, f;
    static int[] pm;
    static int[] ch;
    static boolean flag;
    static int[][] dy;
    static int[] combination;

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        f = sc.nextInt();
        // nC0 nC1 nC2 nC3 .. nCn
        dy = new int[n + 1][n + 1];
        ch = new int[n + 1];
        pm = new int[n];
        combination = new int[n];
        for (int i = 0; i < n; i++) {
            combination[i] = T.combi(n-1, i);
        }
        T.DFS(0, 0);
    }

    private void DFS(int L, int sum) {
        if (flag) {
            return;
        }
        if (L == n) {
            if (sum == f) {
                for (int x : pm) {
                    System.out.print(x + " ");
                }
                System.out.println();
                flag = true;
            }
        } else {
            for (int i = 1; i <= n; i++) {
                if (ch[i] == 0) {
                    ch[i] = 1;
                    pm[L] = i;
                    DFS(L + 1, sum + (combination[L] * pm[L]));
                    ch[i] = 0;
                }
            }
        }
    }

    private int combi(int n, int r) {
        if (dy[n][r] > 0) {
            return dy[n][r];
        }
        if (n == r || r == 0) {
            return 1;
        }
        return dy[n][r] = combi(n - 1, r - 1) + combi(n - 1, r);
    }
}
