package Algorany;

import java.util.*;

public class DefenceGame {
    int answer;

    public int solution(int n, int k, int[] enemy) {
        int soldiers = n;
        int K = k;
        answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int rounds = 0;
        for (int i = 0; i < enemy.length; i++) {
            pq.add(enemy[i]);
            if (soldiers - enemy[i] < 0) {
                if (K > 0) {
                    soldiers += pq.poll();
                    soldiers -= enemy[i];
                    K -= 1;
                    rounds += 1;
                } else {
                    break;
                }
            } else {
                soldiers -= enemy[i];
                rounds += 1;
            }
        }
        answer = Math.max(answer, rounds);
        System.out.println(answer);

        return answer;
    }

    public static void main(String[] args) {
        DefenceGame d = new DefenceGame();
        d.solution(7, 3, new int[]{4, 2, 4, 5, 3, 3, 1});
        // 몇 라운드 까지 막을 수 있는지, 다 막을 수 있다면 enemy[i] 길이 리턴
    }
}
