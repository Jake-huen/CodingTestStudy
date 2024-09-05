package Algorany;

import java.util.*;
import java.io.*;

public class PermutationSunsue {

    static int n;
    static boolean[] visited;
    static long[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new long[21];
        visited = new boolean[n + 1];

        // 팩토리얼 계산
        graph[0] = 1;
        for (int i = 1; i <= 20; i++) {
            graph[i] = graph[i - 1] * i;
        }

        String s = br.readLine();
        String[] input = s.split(" ");
        int mode = Integer.parseInt(input[0]);
        int[] a = new int[n];

        if (mode == 1) { // idx 번째 순열 출력
            long idx = Long.parseLong(input[1]); // idx에 해당하는 순열 찾기
            for (int i = 0; i < n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (visited[j]) {
                        continue;
                    }
                    if (graph[n - i - 1] < idx) {
                        idx -= graph[n - i - 1];
                    } else {
                        a[i] = j;
                        visited[j] = true;
                        break;
                    }
                }
            }
            for (int i = 0; i < n; i++) {
                System.out.print(a[i] + " ");
            }
            System.out.println();

        } else if (mode == 2) { // 주어진 순열이 몇 번째인지 구하기
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(input[i + 1]);
            }
            long ans = 1;
            Arrays.fill(visited, false); // 방문 배열 초기화
            for (int i = 0; i < n; i++) {
                for (int j = 1; j < a[i]; j++) {
                    if (!visited[j]) {
                        ans += graph[n - i - 1];
                    }
                }
                visited[a[i]] = true; // 현재 사용된 숫자는 방문 처리
            }
            System.out.println(ans);
        }
    }
}
