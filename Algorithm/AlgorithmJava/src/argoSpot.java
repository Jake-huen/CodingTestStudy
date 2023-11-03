import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Point {
    int x;
    int y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class argoSpot {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int n, m;
    static int[][] graph;


    public void solution(int col, int row, int[][] graph) {
        System.out.println(bfs(0, 0));
    }

    public static void main(String[] args) throws IOException {
        argoSpot T = new argoSpot();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken()); // 가로 크기
        n = Integer.parseInt(st.nextToken()); // 세로 크기
        graph = new int[n][m];
        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = Character.getNumericValue(input.charAt(j));
            }
        }
        T.solution(n, m, graph);
    }

    public static int bfs(int x, int y) {
        Deque<Point> q = new ArrayDeque<>();
        q.offer(new Point(x, y));
        int[][] wall = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                wall[i][j] = -1;
            }
        }
        wall[0][0] = 0;
        int nx, ny;
        while (!q.isEmpty()) {
            Point p = q.pollFirst();
            for (int i = 0; i < 4; i++) {
                nx = p.x + dx[i];
                ny = p.y + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (wall[nx][ny] == -1) {
                        if (graph[nx][ny] == 0) {
                            wall[nx][ny] = wall[p.x][p.y];
                            Point temp = new Point(nx, ny);
                            q.addFirst(temp);
                        } else {
                            wall[nx][ny] = wall[p.x][p.y] + 1;
                            Point temp = new Point(nx, ny);
                            q.addLast(temp);
                        }
                    }
                }
            }
        }
        return wall[n - 1][m - 1];
    }
}