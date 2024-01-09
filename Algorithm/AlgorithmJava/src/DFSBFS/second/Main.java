package DFSBFS.second;

import java.util.*;

public class Main {
    static int c;
    static int n;
    static int answer = Integer.MIN_VALUE;

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        c = sc.nextInt();
        n = sc.nextInt();
        int[] dogs = new int[n];
        for (int i = 0; i < n; i++) {
            dogs[i] = sc.nextInt();
        }
        T.DFS(0, 0, dogs);
        System.out.println(answer);
    }

    public void DFS(int L, int sum, int[] arr) {
        if (sum > c) {
            return;
        }
        if (L == n) {
            answer = Math.max(answer, sum);
        } else {
            DFS(L + 1, sum + arr[L], arr);
            DFS(L + 1, sum, arr);
        }

    }

    /**
     * 트럭 : C킬로그램 넘게 태울 수 없음
     * - C를 넘지 않으면서 바둑이들을 가장 무겁게 태우고 싶다
     * - N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 철수가 트럭에 태울 수 있는
     * 가장 무거운 무게를 구하는 프로그램을 구해라
     * */
}
