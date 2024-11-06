package Algorany;

import java.io.*;
import java.util.*;

public class HideAndSeek3 {

    static int N, K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());
        N = Integer.parseInt(str.nextToken());
        K = Integer.parseInt(str.nextToken());
        boolean[] visited = new boolean[100001];
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{N, 0}); // 위치, 시간
        visited[N] = true;
        int answer = Integer.MAX_VALUE;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            visited[cur[0]] = true;
            if (cur[0] == K) {
                answer = Math.min(answer, cur[1]);
            }

            if (2 * cur[0] <= 100000) {
                if (!visited[2 * cur[0]]) {
                    visited[2 * cur[0]] = true;
                    q.add(new int[]{2 * cur[0], cur[1]});
                }
            }
            if (cur[0] + 1 <= 100000) {
                if (!visited[cur[0] + 1]) {
                    q.add(new int[]{cur[0] + 1, cur[1] + 1});
                }
            }
            if (cur[0] - 1 >= 0) {
                if (!visited[cur[0] - 1]) {
                    q.add(new int[]{cur[0] - 1, cur[1] + 1});
                }
            }
        }
        System.out.println(answer);
    }
}


// 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
// 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
// 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.
//
// 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
//
// 입력
// 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
//
// 출력
// 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
