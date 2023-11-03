import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;

public class DragonCurve {

    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, -1, 0, 1};
    static int[][] graph = new int[101][101];


    public static void main(String[] args) throws IOException {
        DragonCurve T = new DragonCurve();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < 101; i++) {
            for (int j = 0; j < 101; j++) {
                graph[i][j] = 0;
            }
        }
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int d = sc.nextInt();
            int g = sc.nextInt();

            T.draw(x, y, d, g);
            graph[x][y] = 1;
        }
        int answer = 0;
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (graph[i][j] == 1 && graph[i + 1][j] == 1 && graph[i][j + 1] == 1 && graph[i + 1][j + 1] == 1) {
                    answer += 1;
                }
            }
        }

        System.out.print(answer);
    }

    private void draw(int x, int y, int d, int g) {
        ArrayList<Integer> dir = new ArrayList<>();
        dir.add(d);
        for (int i = 0; i < g; i++) {
            ArrayList<Integer> temp = new ArrayList<>();
            for (int j = dir.size() - 1; j >= 0; j--) {
                temp.add((dir.get(j) + 1) % 4);
            }
            for (int j = 0; j < temp.size(); j++) {
                dir.add(temp.get(j));
            }
        }
        int nx, ny;
        for (int i : dir) {
            nx = x + dx[i];
            ny = y + dy[i];

            graph[nx][ny] = 1;
            x = nx;
            y = ny;
        }
    }
}
