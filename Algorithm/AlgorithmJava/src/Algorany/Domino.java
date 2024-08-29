package Algorany;

import java.util.*;
import java.io.*;

public class Domino {
    static int n;
    static int[][] domino;
    static boolean[] visited;
    static ArrayList<Integer> result;
    static int[] answer = {Integer.MAX_VALUE, Integer.MIN_VALUE};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        domino = new int[n][n];

        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            for (int j = 0; j < n; j++) {
                char c = input.charAt(j);
                if (Character.isDigit(c)) {
                    domino[i][j] = c - '0';
                } else {
                    domino[i][j] = -(c - 'A' + 1);
                }
            }
        }
        result = new ArrayList<>();
        visited = new boolean[n];
        perm(0);

        StringBuilder sb = new StringBuilder();
        sb.append(answer[0]).append("\n").append(answer[1]);
        System.out.println(sb.toString());
    }

    static void perm(int depth) {
        if (depth == n) {
            // 점수 계산
            score();
        }
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                result.add(i);
                perm(depth + 1);
                result.remove(result.size() - 1);
                visited[i] = false;
            }
        }
    }

    static void score() {
        // row는 0부터 n-1까지 증가하고, col 조합이 바껴나간다.
        int score = 1;
        int cycles = 0;
        boolean[] cycleVisited = new boolean[n]; // 순열 조합.

        for (int i = 0; i < n; i++) {
            score = score * domino[i][result.get(i)];
        }

        for (int i = 0; i < n; i++) {
            if (!cycleVisited[i]) {
                cycles += 1;
                int cur = i;
                while(!cycleVisited[cur]){
                    cycleVisited[cur] = true;
                    cur = result.get(cur);
                }
            }
        }

        if (cycles % 2 == 0) {
            score *= -1;
        }
        answer[0] = Math.min(answer[0], score);
        answer[1] = Math.max(answer[1], score);

    }
}
