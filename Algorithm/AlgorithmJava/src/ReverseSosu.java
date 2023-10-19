import java.util.Scanner;

public class ReverseSosu {


    public static void main(String[] args) {
        ReverseSosu T = new ReverseSosu();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] sosuList = new int[n];
        for (int i = 0; i < n; i++) {
            sosuList[i] = kb.nextInt();
        }
        T.Solution(n, sosuList);
    }

    public void Solution(int n, int[] sosuList) {
        for (int i = 0; i < n; i++) {
            int tmp = sosuList[i];
            int res = 0;
            while (tmp > 0) {
                res = res * 10 + tmp % 10;
                tmp = tmp / 10;
            }
            if (isPrime(res)) {
                System.out.print(res + " ");
            }
        }
    }

    public boolean isPrime(int number) {
        int[] checklist = new int[number + 1];
        checklist[0] = 1;
        checklist[1] = 1;
        for (int i = 2; i < number; i++) {
            if (checklist[i] == 0) {
                checklist[i] = 1;
                for (int j = i; j <= number; j = j + i) {
                    checklist[j] = 1;
                }
            }
        }
        if (checklist[number] == 1) {
            return false;
        } else {
            return true;
        }
    }
}
