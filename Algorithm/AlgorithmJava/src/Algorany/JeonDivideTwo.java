package Algorany;

import java.util.*;

public class JeonDivideTwo {
    // n개의 송전탑이 전선을 통해 트리로 구성 -> 하나를 끊어서 2개로 분할하고 싶음.
    // 두 전력망의 송전탑 갯수를 맞추고 싶음.
    boolean[] visited;

    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        for (int i = 0; i < wires.length; i++) {
            int[][] graph = new int[n + 1][n + 1];
            for (int j = 0; j < wires.length; j++) {
                if (i != j) { // i는 끊어버림
                    int[] wire = wires[j];
                    graph[wire[0]][wire[1]] = 1;
                    graph[wire[1]][wire[0]] = 1;
                }
            }
            visited = new boolean[n + 1];
            int idx = 0;
            int[] ans = new int[2];
            for (int ii = 1; ii < n + 1; ii++) {
                if (!visited[ii]) {
                    ans[idx] = bfs(ii, n + 1, graph);
                    idx += 1;
                }
            }
            answer = Math.min(Math.abs(ans[1] - ans[0]), answer);

        }

        return answer;
    }

    public int bfs(int start, int len, int[][] graph) {
        int ans = 1;
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        visited[start] = true;
        while (!q.isEmpty()) {
            int cur = q.poll();
            for (int i = 1; i < len; i++) {
                if (graph[cur][i] == 1 && !visited[i]) {
                    q.add(i);
                    visited[i] = true;
                    ans += 1;
                }
            }
        }
        return ans;
    }

    static class anotherSolution {
        int N, min;
        int[][] map;
        int[] vst;
        int dfs(int n){
            vst[n] = 1;
            int child = 1;
            for(int i = 1; i <= N; i++) {
                if(vst[i] == 0 && map[n][i] == 1) {
                    vst[i] = 1;
                    child += dfs(i);
                }
            }
            min = Math.min(min, Math.abs(child - (N - child)));
            return child;
        }
        public int solution(int n, int[][] wires) {
            N = n;
            min = n;
            map = new int[n+1][n+1];
            vst = new int[n+1];
            for(int[] wire : wires) {
                int a = wire[0], b = wire[1];
                map[a][b] = map[b][a] = 1;
            }
            dfs(1);
            return min;
        }
    }


    public static void main(String[] args) {
        JeonDivideTwo j = new JeonDivideTwo();
        int[][] wires = {{1, 3}, {2, 3}, {3, 4}, {4, 5}, {4, 6}, {4, 7}, {7, 8}, {7, 9}};
        System.out.println(j.solution(9, wires)); // 3
        System.out.println(j.solution(4, new int[][]{{1, 2}, {2, 3}, {3, 4}})); // 0
    }
}
