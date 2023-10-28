import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Mentoring {


    public static void main(String[] args) {
        Mentoring T = new Mentoring();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int m = kb.nextInt();
        int[][] graph = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                graph[i][j] = kb.nextInt();
            }
        }
        System.out.println(T.Solution(n, m, graph));
    }

    private int Solution(int n, int m, int[][] graph) {
        int answers = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) { // 총 경우의 수
                int cnt = 0;
                for (int k = 0; k < m; k++) {
                    int first = 0;
                    int second = 0;
                    for (int l = 0; l < n; l++) {
                        if (graph[k][l] == i) {
                            first = l;
                        } else if (graph[k][l] == j) {
                            second = l;
                        }
                    }
                    if (first < second) { // 뒤에 있는 경우
                        cnt += 1;
                    }
                }
                if (cnt == m) {
                    answers += 1;
                }
            }
        }
        return answers;
    }
}
