import java.util.Scanner;

public class LookStudent {
    public int Solution(int n, int[] students) {
        int check = students[0];
        int answer = 1;
        for (int i = 1; i < n; i++) {
            if (students[i] > check) {
                answer += 1;
                check = students[i];
            }
        }
        return answer;
    }
    public static void main(String[] args) {
        LookStudent T = new LookStudent();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] students = new int[n];
        for (int i = 0; i < n; i++) {
            students[i] = kb.nextInt();
        }
        System.out.println(T.Solution(n, students));
    }
}
