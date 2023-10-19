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

    }
}
