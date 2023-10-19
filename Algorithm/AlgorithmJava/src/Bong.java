import java.util.Scanner;

public class Bong {
    public static void main(String[] args) {
        Bong T = new Bong();
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
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int tmp = graph[i][j];
                int left, right, up, down;
                left = right = up = down = 0;
                if (i > 0) {
                    up = graph[i - 1][j];
                }
                if (i != n - 1) {
                    down = graph[i + 1][j];
                }
                if (j > 0) {
                    left = graph[i][j - 1];
                }
                if (j != n - 1) {
                    right = graph[i][j + 1];
                }
                if (tmp > up && tmp > down && tmp > left && tmp > right) {
                    ans+=1;
                }
            }
        }
        return ans;
    }
}
