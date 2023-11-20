package DFSBFS.s2;

import java.util.*;

// 중복을 허락해서 구슬 M번 뽑기
// 동전 뽑기
// 순열구하기 -> N개의 자연수 중에서 M개를 뽑아서 일렬로 나열하는 방법
// N개의 구슬 중에서 M개를 뽑는 방법의 수
public class Main {
    static int[] combi;
    static int n, m;

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        combi = new int[m];
        T.DFS(0, 1);
    }

    private void DFS(int L, int S) {
        if (L == m) {
            for (int x : combi) {
                System.out.print(x + " ");
            }
            System.out.println();
        } else {
            for (int i = S; i <= n; i++) {
                combi[L] = i;
                DFS(L + 1, i + 1);
            }
        }
    }
}
