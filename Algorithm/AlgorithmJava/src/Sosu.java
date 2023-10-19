import java.util.ArrayList;
import java.util.Scanner;

public class Sosu {
    public int Solution(int n) {
        int answer = 0;
        int[] checklist = new int[n + 1];
        for (int i = 2; i <= n; i++) {
            if (checklist[i] == 0) {
                answer += 1;
                for (int j = i; j <= n; j = j + i) {
                    if (j % i == 0) {
                        checklist[j] = 1;
                    }
                }
                checklist[i] = 1;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Sosu T = new Sosu();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        System.out.print(T.Solution(n));
    }
}
