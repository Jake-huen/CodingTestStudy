package Algorany;

import java.io.*;
import java.util.*;

public class Watch {
    static int n, m;
    static int[][] graph;
    static int[][] cases;
    static StringTokenizer str;
    static ArrayList<Node> cctv = new ArrayList<>();
    static int answer = Integer.MAX_VALUE;

    public static class Node {
        int x;
        int y;
        int num;

        Node(int x, int y, int num) {
            this.x = x;
            this.y = y;
            this.num = num;
        }
    }

    public static int[][] copyMap(int[][] graph) {
        int[][] result = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                result[i][j] = graph[i][j];
            }
        }
        return result;
    }

    public static int result(int[][] graph) {
        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 0) {
                    result += 1;
                }
            }
        }
        return result;
    }

    public static void left(int[][] graph, int x, int y) {
        for (int i = y - 1; i >= 0; i--) {
            if (graph[x][i] == 6) {
                return;
            }
            if (graph[x][i] != 0) {
                continue;
            }
            graph[x][i] = -1;
        }
    }

    public static void right(int[][] graph, int x, int y) {
        for (int i = y + 1; i < m; i++) {
            if (graph[x][i] == 6) {
                return;
            }
            if (graph[x][i] != 0) {
                continue;
            }
            graph[x][i] = -1;
        }
    }

    public static void up(int[][] graph, int x, int y) {
        for (int i = x - 1; i >= 0; i--) {
            if (graph[i][y] == 6) {
                return;
            }
            if (graph[i][y] != 0) {
                continue;
            }
            graph[i][y] = -1;
        }
    }

    public static void down(int[][] graph, int x, int y) {
        for (int i = x + 1; i < n; i++) {
            if (graph[i][y] == 6) {
                return;
            }
            if (graph[i][y] != 0) {
                continue;
            }
            graph[i][y] = -1;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = new StringTokenizer(br.readLine());
        n = Integer.parseInt(str.nextToken());
        m = Integer.parseInt(str.nextToken());
        graph = new int[n][m];
        for (int i = 0; i < n; i++) {
            str = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(str.nextToken());
                if (graph[i][j] >= 1 && graph[i][j] < 6) {
                    cctv.add(new Node(i, j, graph[i][j])); // cctv 개수
                }
            }

        }

        // 모든 경우에서 사각지대의 개수를 구해야함 -> 0의 개수
        // 각각의 케이스의 경우
        dfs(0, graph, cctv);
        System.out.println(answer);
    }

    public static void dfs(int cnt, int[][] graph, ArrayList<Node> cctv) {
        if (cnt == cctv.size()) {
            // System.out.println(result(graph));
            answer = Math.min(answer, result(graph));
            return;
        }
        int cctvNum = cctv.get(cnt).num;
        int x = cctv.get(cnt).x;
        int y = cctv.get(cnt).y;
        int[][] tmp;

        if (cctvNum == 1) { // 1번 cctv일 경우
            tmp = copyMap(graph);
            left(tmp, x, y);
            dfs(cnt + 1, tmp, cctv);

            tmp = copyMap(graph);
            right(tmp, x, y);
            dfs(cnt + 1, tmp, cctv);

            tmp = copyMap(graph);
            up(tmp, x, y);
            dfs(cnt + 1, tmp, cctv);

            tmp = copyMap(graph);
            down(tmp, x, y);
            dfs(cnt + 1, tmp, cctv);
        } else if (cctvNum == 2) {
            tmp = copyMap(graph);
            left(tmp, x, y);
            right(tmp, x, y);
            dfs(cnt + 1, tmp, cctv);

            tmp = copyMap(graph);
            up(tmp, x, y);
            down(tmp, x, y);
            dfs(cnt + 1, tmp, cctv);
        } else if (cctvNum == 3) {
            tmp = copyMap(graph);
            left(tmp, x, y);
            up(tmp, x, y);
            dfs(cnt + 1, tmp, cctv);

            tmp = copyMap(graph);
            left(tmp, x, y);
            down(tmp, x, y);
            dfs(cnt + 1, tmp, cctv);

            tmp = copyMap(graph);
            right(tmp, x, y);
            down(tmp, x, y);
            dfs(cnt + 1, tmp, cctv);

            tmp = copyMap(graph);
            right(tmp, x, y);
            up(tmp, x, y);
            dfs(cnt + 1, tmp, cctv);
        } else if (cctvNum == 4) {
            tmp = copyMap(graph);
            up(tmp, x, y);
            left(tmp, x, y);
            down(tmp, x, y);
            dfs(cnt + 1, tmp, cctv);

            tmp = copyMap(graph);
            left(tmp, x, y);
            down(tmp, x, y);
            right(tmp, x, y);
            dfs(cnt + 1, tmp, cctv);

            tmp = copyMap(graph);
            up(tmp, x, y);
            right(tmp, x, y);
            down(tmp, x, y);
            dfs(cnt + 1, tmp, cctv);

            tmp = copyMap(graph);
            left(tmp, x, y);
            up(tmp, x, y);
            right(tmp, x, y);
            dfs(cnt + 1, tmp, cctv);
        } else if (cctvNum == 5) {
            tmp = copyMap(graph);
            up(tmp, x, y);
            left(tmp, x, y);
            right(tmp, x, y);
            down(tmp, x, y);
            dfs(cnt + 1, tmp, cctv);
        }

    }
}
