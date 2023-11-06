package TwoPointersAlgorithm.five;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(T.solution(n));
    }

    private int solution(int n) {
        int answer = 0;
        int cnt = 1;
        n -= 1;
        while (n > 0) {
            cnt += 1;
            n = n - cnt;
            if (n % cnt == 0) {
                answer += 1;
            }
        }
        return answer;
    }
}
