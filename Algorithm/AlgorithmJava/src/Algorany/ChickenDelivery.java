package Algorany;

import java.io.*;
import java.util.*;

public class ChickenDelivery {
    static StringTokenizer str;
    static int n, m;
    static int[][] graph;
    static int answer = Integer.MAX_VALUE;
    static ArrayList<int[]> houses;
    static ArrayList<int[]> chickenPositions;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = new StringTokenizer(br.readLine());
        n = Integer.parseInt(str.nextToken());
        m = Integer.parseInt(str.nextToken());
        graph = new int[n][n];
        houses = new ArrayList<>();
        chickenPositions = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            str = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(str.nextToken());
                if (graph[i][j] == 1) {
                    houses.add(new int[]{i, j});
                } else if (graph[i][j] == 2) {
                    chickenPositions.add(new int[]{i, j});
                }
            }
        } // 0은 빈칸, 1은 집, 2는 치킨집 -> 치킨집 중에서 M개 선택
        boolean[] selected = new boolean[chickenPositions.size()];
        dfs(0, 0, selected);
        System.out.println(answer);
    }

    public static void dfs(int chicken, int start, boolean[] selected) {
        if (chicken == m) {
            // 도시의 치킨 거리 계산
            ArrayList<int[]> selectedChickens = new ArrayList<>();
            for (int i = 0; i < selected.length; i++) {
                if (selected[i]) {
                    selectedChickens.add(chickenPositions.get(i));
                }
            }
            answer = Math.min(answer, chickenDistance(selectedChickens));
            return;
        }
        for (int i = start; i < chickenPositions.size(); i++) {
            if (!selected[i]) {
                selected[i] = true;
                dfs(chicken + 1, i + 1, selected);
                selected[i] = false;
            }
        }
    }

    public static int chickenDistance(ArrayList<int[]> chickens) {
        // 3인 곳과 1인곳의 거리 중 최소인 곳(치킨 거리)
        int[][] map = new int[n][n];

        int sum = 0;
        for (int[] house : houses) {
            int x = house[0];
            int y = house[1];
            int temp = Integer.MAX_VALUE;
            for (int[] chicken : chickens) {
                temp = Math.min(temp, Math.abs(x - chicken[0]) + Math.abs(y - chicken[1]));
            }
            sum += temp;
        }
        return sum;
    }
}
