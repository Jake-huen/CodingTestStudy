package Algorany;

import java.util.*;
import java.io.*;

public class bubun {

    static int N, M;
    static int[] numbers;
    static LinkedHashSet<ArrayList<Integer>> result;
    static ArrayList<Integer> temp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        N = Integer.parseInt(s[0]);
        M = Integer.parseInt(s[1]);
        numbers = new int[N];
        StringTokenizer str = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(str.nextToken());
        }
        Arrays.sort(numbers);
        result = new LinkedHashSet<>();
        temp = new ArrayList<>();
        dfs(0, 0);
        // N개의 자연수 중에서 M개를 고른 수열
        for (ArrayList<Integer> list : result) {
            for (int i : list) {
                System.out.print(i + " ");
            }
            System.out.println();
        }
    }

    public static void dfs(int depth, int start) {
        if (depth == M) {
            result.add(new ArrayList<>(temp));
            return;
        }
        for (int i = start; i < N; i++) {
            temp.add(numbers[i]);
            dfs(depth + 1, i);
            temp.remove(temp.size() - 1);
        }

    }
}
