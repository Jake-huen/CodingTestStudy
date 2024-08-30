package Algorany;

import java.util.*;
import java.io.*;

public class BuDeunHo {

    static int k;
    static String[] input;
    static boolean[] visited;
    static String result;
    static long max = Long.MIN_VALUE;
    static long min = Long.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        k = Integer.parseInt(br.readLine());
        input = br.readLine().split(" ");
        visited = new boolean[10]; // 0에서 9까지
        result = "";
        dfs(0);
        System.out.println(max);
        if (String.valueOf(min).length() == k) {
            System.out.println("0" + min);
        } else {
            System.out.println(min);
        }

    }

    public static void dfs(int depth) {
        if (depth == k + 1) {
            long num = Long.parseLong(result);
            max = Math.max(max, num);
            min = Math.min(min, num);
            return;
        }

        for (int i = 9; i >= 0; i--) {
            if (!visited[i]) {
                if (depth == 0) {
                    visited[i] = true;
                    result += i;
                    dfs(depth + 1);
                    visited[i] = false;
                    result = result.substring(0, result.length() - 1);
                } else {
                    if (input[depth - 1].equals("<")) {
                        if (result.charAt(result.length() - 1) - '0' < i) {
                            visited[i] = true;
                            result += i;
                            dfs(depth + 1);
                            visited[i] = false;
                            result = result.substring(0, result.length() - 1);
                        }
                    } else if (input[depth - 1].equals(">")) {
                        if (result.charAt(result.length() - 1) - '0' > i) {
                            visited[i] = true;
                            result += i;
                            dfs(depth + 1);
                            visited[i] = false;
                            result = result.substring(0, result.length() - 1);
                        }
                    }
                }

            }
        }
    }
}
