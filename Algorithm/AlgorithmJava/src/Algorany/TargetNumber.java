package Algorany;

import java.util.*;

public class TargetNumber {
    int answer;
    int[] result;
    int T;

    public int solution(int[] numbers, int target) {
        T = target;
        answer = 0;
        // 부호 경우의 수 구하기
        result = new int[numbers.length];
        dfs(0, numbers);
        System.out.println(answer);
        return answer;
    }

    public void dfs(int cnt, int[] numbers) {
        if (cnt == numbers.length) {
            // 부호 계산
            int ans = 0;
            for (int i = 0; i < numbers.length; i++) {
                ans += (result[i] * numbers[i]);
            }
            if (ans == T) {
                answer += 1;
            }
            return;
        }
        for (int i = 0; i < 2; i++) {
            int tmp = (i == 0) ? 1 : -1;
            result[cnt] = tmp;
            dfs(cnt + 1, numbers);
        }

    }

    public static void main(String[] args) {
        TargetNumber tn = new TargetNumber();
        tn.solution(new int[]{1, 1, 1, 1, 1}, 3); // 5
    }
}
