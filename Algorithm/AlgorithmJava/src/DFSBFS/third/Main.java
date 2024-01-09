package DFSBFS.third;

import java.util.*;

public class Main {

    static int n, m;
    static int[] scores;
    static int[] times;
    static int answer = Integer.MIN_VALUE;

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        scores = new int[n];
        times = new int[n];
        for (int i = 0; i < n; i++) {
            scores[i] = sc.nextInt();
            times[i] = sc.nextInt();
        }
        T.DFS(0, 0, 0, scores, times);
        System.out.println(answer);
    }

    private void DFS(int L, int totalTime, int sum, int[] scores, int[] times) {
        if (totalTime > m) {
            return;
        }
        if (L == n) {
            answer = Math.max(answer, sum);
        } else {
            DFS(L + 1, totalTime + times[L], sum + scores[L], scores, times);
            DFS(L + 1, totalTime, sum, scores, times);
        }
    }
}
