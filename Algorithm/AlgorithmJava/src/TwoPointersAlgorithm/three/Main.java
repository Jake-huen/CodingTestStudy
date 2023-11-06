package TwoPointersAlgorithm.three;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        System.out.println(T.solution(n, k, a));
    }

    private int solution(int n, int k, int[] a) {
        int temp = 0;
        int new_temp;
        for (int i = 0; i < k; i++) {
            temp += a[i];
        }
        int answer = temp;
        for (int i = 1; i < n - k; i++) {
            new_temp = temp - a[i - 1] + a[i + k - 1];
            if (new_temp > answer) {
                answer = new_temp;
            }
            temp = new_temp;
        }
        return answer;
    }
}
