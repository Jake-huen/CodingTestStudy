package Algorany;

import java.util.*;
import java.io.*;

public class SendNews {

    static int n;
    static ArrayList<ArrayList<Integer>> graph;
    static int[] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer str = new StringTokenizer(br.readLine());
        graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < n; i++) {
            int a = Integer.parseInt(str.nextToken());
            if (a != -1) {
                graph.get(a).add(i);
            }
        }
        dp = new int[n];
        int min = depth(0);
        System.out.println(min);
    }

    static int depth(int idx) {
        for (int nxt : graph.get(idx)) {
            dp[nxt] = 1 + depth(nxt);
        }
        Collections.sort(graph.get(idx), new Sort());
        int res = 0;
        for (int i = 0; i < graph.get(idx).size(); i++) {
            int num = graph.get(idx).get(i);
            dp[num] += i;
            res = Math.max(res, dp[num]);
        }
        return res;
    }
    static class Sort implements Comparator<Integer> {
        @Override
        public int compare(Integer o1, Integer o2) {
            return dp[o2] - dp[o1];
        }
    }
}
