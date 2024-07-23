package Algorany.BackTracking;

import java.util.*;
import java.io.*;

public class ABCDE {

    static int n, m; // 사람 수, 친구 관계 수
    static int a, b;
    static ArrayList<ArrayList<Integer>> graph;
    static StringTokenizer str;
    static boolean[] visited;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = new StringTokenizer(br.readLine());
        n = Integer.parseInt(str.nextToken());
        m = Integer.parseInt(str.nextToken());
        graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        visited = new boolean[n];
        for (int i = 0; i < m; i++) {
            str = new StringTokenizer(br.readLine());
            a = Integer.parseInt(str.nextToken());
            b = Integer.parseInt(str.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        for (int i = 0; i < n; i++) {
            if (answer == 0) {
                dfs(i, 1);
            }
        }
        System.out.println(answer);
    }

    public static void dfs(int start, int depth) {
        if (depth == 5) {
            answer = 1;
            return;
        }
        visited[start] = true;
        for (int i : graph.get(start)) {
            if (!visited[i]) {
                dfs(i, depth + 1);
            }
        }
        visited[start] = false;
    }
}
