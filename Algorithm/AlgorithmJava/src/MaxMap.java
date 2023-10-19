import java.util.Scanner;

public class MaxMap {


    public static void main(String[] args) {
        MaxMap T = new MaxMap();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[][] graph = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                graph[i][j] = kb.nextInt();
            }
        }
        System.out.println(T.Solution(n, graph));
    }

    private int Solution(int n, int[][] graph) {
        int answer = 0;
        int sum1, sum2;
        for (int i = 0; i < n; i++) {
            sum1 = sum2 = 0;
            for (int j = 0; j < n; j++) {
                sum1 += graph[i][j];
                sum2 += graph[j][i];
            }
            answer = Math.max(answer, sum1);
            answer = Math.max(answer, sum2);
        }
        sum1 = sum2 = 0;
        for (int i = 0; i < n; i++) {
            sum1 += graph[i][i];
            sum2 += graph[i][n - i - 1];
        }
        answer = Math.max(answer, sum1);
        answer = Math.max(answer, sum2);
        return answer;
    }
}
