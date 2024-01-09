package DFSBFS.first;

import java.util.*;

public class Main {
    static int n;
    static int[] numbers;
    static int total = 0;
    static String answer = "NO";
    static boolean flag = false;

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = sc.nextInt();
            total += numbers[i];
        }
        T.DFS(0, 0, numbers);
        System.out.println(answer);
    }

    public void DFS(int L, int sum, int[] numbers) {
        if (flag) {
            return;
        }
        if (sum > total / 2) {
            return;
        }
        if (L == n) {
            if (total - sum == sum) {
                answer = "YES";
                flag = true;
            }
        } else {
            DFS(L + 1, sum + numbers[L], numbers);
            DFS(L + 1, sum, numbers);
        }
    }
}
