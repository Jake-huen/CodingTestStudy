package HashMapSetAlgorithm.four;

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String t = sc.next();
        T.solution(s, t);
    }

    private void solution(String s, String t) {
        HashMap<Character, Integer> map = new HashMap<>();
        HashMap<Character, Integer> Tmap = new HashMap<>();
        char[] T = t.toCharArray();
        for (int i = 0; i <= T.length; i++) {

        }

        char[] S = s.toCharArray();
        for (int i = 0; i < S.length; i++) {
            map.put(S[i], map.getOrDefault(S[i], 0) + 1);
        }
    }
}
