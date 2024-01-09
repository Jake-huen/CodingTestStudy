package DFSBFS.seven;

import java.util.*;

public class Main {
    static int n, r;
    static int[][] dy;

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        r = sc.nextInt();
        dy = new int[n + 1][n + 1];
        System.out.println(T.DFS(n, r));
    }

    private int DFS(int n, int r) {
        if (dy[n][r] > 0) {
            return dy[n][r];
        }
        if (n == r || r == 0) {
            return 1;
        } else {
            return dy[n][r] = DFS(n - 1, r - 1) + DFS(n - 1, r);
        }
    }
}
/**
 * 5 3
 */
