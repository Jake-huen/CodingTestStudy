import java.util.ArrayList;
import java.util.Scanner;

public class Score {


    public static void main(String[] args) {
        Score T = new Score();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] results = new int[n];
        for (int i = 0; i < n; i++) {
            results[i] = kb.nextInt();
        }
        System.out.println(T.Solution(n, results));
    }

    public int Solution(int n, int[] results) {
        int cnt = 0;
        int sum = 0;
        for (int result : results) {
            if (result == 0) {
                cnt = 0;
            } else {
                cnt += 1;
                sum += cnt;
            }
        }
        return sum;
    }
}
