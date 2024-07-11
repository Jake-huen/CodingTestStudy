package Algorany;

import java.io.*;
import java.util.*;

public class DragonLiquid {

    static int n;
    static int[] liquids;
    static int answer = 2000000000;
    static int[] answerIdx = new int[2];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        liquids = new int[n];
        StringTokenizer str = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            liquids[i] = Integer.parseInt(str.nextToken());
        }

        // 각 요소에 대해 이분 탐색을 사용하여 최적 쌍을 찾기
        for (int i = 0; i < n - 1; i++) {
            binarySearch(i, liquids[i]);
        }

        // 결과 출력
        System.out.println(liquids[answerIdx[0]] + " " + liquids[answerIdx[1]]);
    }

    private static void binarySearch(int idx, int target) {
        int start = idx + 1;
        int end = n - 1;
        int mid;

        while (start <= end) {
            mid = (start + end) / 2;
            int sum = target + liquids[mid];
            if (Math.abs(sum) < answer) {
                answer = Math.abs(sum);
                answerIdx[0] = idx;
                answerIdx[1] = mid;
            }
            if (sum < 0) {
                start = mid + 1;
            } else if (sum > 0) {
                end = mid - 1;
            } else {
                // 합이 0인 경우 더 나은 값이 없으므로 바로 반환
                return;
            }
        }

        // 이분 탐색 이후 최적값 주변 탐색
        if (start < n && Math.abs(target + liquids[start]) < answer) {
            answer = Math.abs(target + liquids[start]);
            answerIdx[0] = idx;
            answerIdx[1] = start;
        }
        if (end > idx && Math.abs(target + liquids[end]) < answer) {
            answer = Math.abs(target + liquids[end]);
            answerIdx[0] = idx;
            answerIdx[1] = end;
        }
    }
}


