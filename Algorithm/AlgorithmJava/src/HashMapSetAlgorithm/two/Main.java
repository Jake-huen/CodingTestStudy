package HashMapSetAlgorithm.two;

import java.util.Scanner;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        String temp = sc.next();
        char[] a = temp.toCharArray();
        temp = sc.next();
        char[] b = temp.toCharArray();
        System.out.println(T.solution(a, b));
    }

    private String solution(char[] a, char[] b) {
        HashMap<Character, Integer> charNumberOfA = new HashMap<>();

        for (int i = 0; i < a.length; i++) {
            charNumberOfA.put(a[i], charNumberOfA.getOrDefault(a[i], 0) + 1);
        }
        for (int i = 0; i < b.length; i++) {
            if (!charNumberOfA.containsKey(b[i]) || charNumberOfA.get(b[i]) == 0) {
                return "NO";
            } else {
                charNumberOfA.put(b[i], charNumberOfA.get(b[i]) - 1);
            }
        }
        return "YES";
    }
}
