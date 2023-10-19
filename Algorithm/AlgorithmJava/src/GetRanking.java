import java.util.*;

public class GetRanking {

    public static void main(String[] args) {
        GetRanking T = new GetRanking();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] scores = new int[n];
        for (int i = 0; i < n; i++) {
            scores[i] = kb.nextInt();
        }
        for (int x : T.Solution(n, scores)) {
            System.out.print(x+" ");
        }
    }

    private ArrayList<Integer> Solution(int n, int[] scores) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int tmp = 1;
            for (int j = 0; j < n; j++) {
                if (scores[j] > scores[i]) {
                    tmp += 1;
                }
            }
            answer.add(tmp);
        }
        return answer;
    }
}
