package HashMapSetAlgorithm.five;

import java.util.*;

public class Main {


    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] cards = new int[n];
        for (int i = 0; i < n; i++) {
            cards[i] = sc.nextInt();
        }
        System.out.println(T.solution(n, k, cards));
    }

    private int solution(int n, int k, int[] cards) {
        int answer = -1;
        TreeSet<Integer> Tset = new TreeSet<>(Collections.reverseOrder()); // 내림차순
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int l = j + 1; l < n; l++) {
                    Tset.add(cards[i] + cards[j] + cards[l]);
                }
            }
        }
        int cnt = 0;
        for (int x : Tset) {
            cnt++;
            if(cnt==k) return x;
        }
        return answer;
    }
}
