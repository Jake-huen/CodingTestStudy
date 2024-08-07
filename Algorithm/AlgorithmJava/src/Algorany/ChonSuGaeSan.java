package Algorany;

import java.util.*;
import java.io.*;

public class ChonSuGaeSan {
    static int n; // 전체 사람 수
    static int a, b; // 촌수 계산해야하는 두사람
    static int m; // 부모 자식들 간의 관계 수
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>(); // 부모 자식 관계
    static boolean[] visited;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer str = new StringTokenizer(br.readLine());
        a = Integer.parseInt(str.nextToken()) - 1;
        b = Integer.parseInt(str.nextToken()) - 1;
        m = Integer.parseInt(br.readLine());
        visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            str = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(str.nextToken()) - 1;
            int y = Integer.parseInt(str.nextToken()) - 1;
            graph.get(x).add(y);
            graph.get(y).add(x);
        }

        // a에서 b까지 DFS나 BFS 통해서 연결된 길이 구하면 됨.
        dfs(a, 0);
        System.out.println(answer == 0 ? -1 : answer);
    }

    public static void dfs(int start, int depth) {
        if (start == b) {
            answer = depth;
            return;
        }

        for (int i : graph.get(start)) {
            if (!visited[i]) {
                visited[i] = true;
                // System.out.println(i);
                dfs(i, depth + 1);
                visited[i] = false;
            }
        }
    }
}
