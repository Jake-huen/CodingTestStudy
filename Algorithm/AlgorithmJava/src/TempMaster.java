import java.util.Scanner;

public class TempMaster {

    public static void main(String[] args) {
        TempMaster T = new TempMaster();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[][] graph = new int[n+1][6];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <=5; j++) {
                graph[i][j] = kb.nextInt();
            }
        }
        System.out.println(T.Solution(n, graph));
    }

    private int Solution(int n, int[][] graph) {
        int answer = 0, min = Integer.MIN_VALUE;
        for (int i = 1; i <= n; i++) {
            int cnt = 0;
            for (int j = 1; j <= n; j++) {
                for (int k = 1; k <= 5; k++) {
                    if (graph[i][k] == graph[j][k]) {
                        cnt+=1;
                        break;
                    }
                }
            }
            if (cnt > min) {
                min = cnt;
                answer = i;
            }
        }
        return answer;
    }
}
