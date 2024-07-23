package Algorany.BackTracking;

import java.io.*;
import java.util.*;

public class Lotto {

    static StringTokenizer str;
    static int k;
    static int[] numbers;
    static int[] result;
    static boolean[] visited;
    static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            str = new StringTokenizer(br.readLine());
            k = Integer.parseInt(str.nextToken());
            if (k == 0) {
                return;
            }
            result = new int[6];
            numbers = new int[k];
            visited = new boolean[k];
            for (int i = 0; i < k; i++) {
                numbers[i] = Integer.parseInt(str.nextToken());
            }
            sb = new StringBuilder();
            dfs(0, 0);
            System.out.println(sb.toString());
        }
    }

    public static void dfs(int start, int depth) {
        if (depth == 6) {
            for (int i : result) {
                sb.append(i).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = start; i < k; i++) {
            if (!visited[i]) {
                visited[i] = true;
                result[depth] = numbers[i];
                dfs(i, depth + 1);
                visited[i] = false;
            }
        }
    }
}
