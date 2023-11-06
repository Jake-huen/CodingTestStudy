package TwoPointersAlgorithm.four;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        System.out.println(T.solution(n, m, a));
    }

    private int solution(int n, int m, int[] a) {
        int sum = 0;
        int p1 = 0;
        int answer = 0;
        for (int p2 = 0; p2 < n; p2++) {
            sum += a[p2];
            if (sum == m) {
                answer += 1;
            }
            while (sum >= m) {
                sum -= a[p1];
                p1 += 1;
                if (sum == m) {
                    answer += 1;
                }
            }

        }
        return answer;
    }
}
