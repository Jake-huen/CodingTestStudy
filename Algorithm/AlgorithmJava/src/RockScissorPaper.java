import java.util.ArrayList;
import java.util.Scanner;

public class RockScissorPaper {

    public char rcp(int x, int y) {
        if (x == y) {
            return 'D';
        } else if ((x == 1 && y == 3) || (x == 2 && y == 1) || (x == 3 && y == 2)) {
            return 'A';
        } else{
            return 'B';
        }
    }

    public ArrayList<Character> Solution(int n, int[] a, int[] b) {
        ArrayList<Character> answer = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            answer.add(rcp(a[i], b[i]));
        }

        return answer;
    }

    public static void main(String[] args) {
        RockScissorPaper T = new RockScissorPaper();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] a = new int[n];
        int[] b = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = kb.nextInt();
        }
        for (int i = 0; i < n; i++) {
            b[i] = kb.nextInt();
        }
        for (char x : T.Solution(n, a, b)) {
            System.out.println(x);
        }
    }
}
