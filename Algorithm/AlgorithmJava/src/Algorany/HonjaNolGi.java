package Algorany;

import java.util.*;

public class HonjaNolGi {

    public int solution(int[] cards) {
        int N = cards.length;
        boolean[] visited = new boolean[N];
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                int cnt = 0;
                int cur = i;
                while (!visited[cur]) {
                    visited[cur] = true;
                    cnt += 1;
                    cur = cards[cur] - 1;
                }
                result.add(cnt);
            }
        }
        Collections.sort(result, Collections.reverseOrder());
        int answer = 0;
        if (result.size() >= 2) {
            answer = result.get(0) * result.get(1);
        }

        return answer;
    }

    public static void main(String[] args) {
        HonjaNolGi honjaNolGi = new HonjaNolGi();
        // 상자 안에 들어있는 카드 번호가 순서대로 담긴 배열
        honjaNolGi.solution(new int[]{8, 6, 3, 7, 2, 5, 1, 4}); // 12
    }
}
