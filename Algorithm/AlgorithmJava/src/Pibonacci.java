import java.util.ArrayList;
import java.util.Scanner;

public class Pibonacci {

    public ArrayList<Integer> Solution(int n) {
        ArrayList<Integer> answers = new ArrayList<>();
        answers.add(1);
        answers.add(1);
        for (int i = 2; i < n; i++) {
            answers.add(answers.get(i - 1) + answers.get(i - 2));
        }
        return answers;
    }
    public static void main(String[] args) {
        Pibonacci T = new Pibonacci();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        for (int x : T.Solution(n)) {
            System.out.print(x + " ");
        }
    }
}
