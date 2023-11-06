package TwoPointersAlgorithm.three;

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
        T.solution(n, m, a);
    }

    private void solution(int n, int m, int[] a) {
        
    }
}
