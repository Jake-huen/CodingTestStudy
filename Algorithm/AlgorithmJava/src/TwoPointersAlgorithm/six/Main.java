package TwoPointersAlgorithm.six;

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
        /*
        최대 k번 0을 1로 바꿀 수 있다. k번의 변경을 통해 1로만 구성된 최대 길이의 연속부분수열
        * */
        int lt = 0;
        int cnt = 0;
        int answer = 0;
        for (int rt = 0; rt < n; rt++) {
            if (a[rt] == 0) {
                cnt += 1;
            }
            while (cnt > k) {
                if (a[lt] == 0) {
                    cnt -= 1;
                }
                lt += 1;
            }
            answer = Math.max(answer, rt - lt + 1);
        }
        return answer;
    }
}
