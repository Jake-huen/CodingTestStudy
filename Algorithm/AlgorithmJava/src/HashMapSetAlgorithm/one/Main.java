package HashMapSetAlgorithm.one;

import java.util.HashMap;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String s = sc.next();
        System.out.println(T.solution(n, s));
    }

    private char solution(int n, String s) {
        HashMap<Character, Integer> result = new HashMap<>();
        for (char x : s.toCharArray()) {
            result.put(x, result.getOrDefault(x, 0) + 1);
        }
        char answer=' ';
        int max = Integer.MIN_VALUE;
        for (char x : result.keySet()) {
            if (max < result.get(x)) {
                max = result.get(x);
                answer = x;
            }
        }
        return answer;
    }
}
