package TwoPointersAlgorithm.one;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = kb.nextInt();
        }
        int m = kb.nextInt();
        int[] b = new int[m];
        for (int i = 0; i < m; i++) {
            b[i] = kb.nextInt();
        }
        for (int x : T.solution(a, b, n, m)) System.out.print(x + " ");
    }

    private ArrayList<Integer> solution(int[] a, int[] b, int n, int m) {
        ArrayList<Integer> answer = new ArrayList<>();
        int p1 = 0;
        int p2 = 0;
        while (p1 < n && p2 < m) {
            if (a[p1] < b[p2]) {
                answer.add(a[p1]);
                p1 += 1;
            } else if (a[p1] >= b[p2]) {
                answer.add(b[p2]);
                p2 += 1;
            }
        }
        while (p1 < n) {
            answer.add(a[p1]);
            p1 += 1;
        }
        while (p2 < m) {
            answer.add(b[p2]);
            p2 += 1;
        }
        return answer;
    }


}
