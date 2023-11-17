package HashMapSetAlgorithm.four;

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String t = sc.next();
        System.out.println(T.solution(s, t));
    }

    private int solution(String a, String b) {
        HashMap<Character, Integer> am = new HashMap<>();
        HashMap<Character, Integer> bm = new HashMap<>();
        int answer = 0;
        for (char x : b.toCharArray()) {
            bm.put(x, bm.getOrDefault(x, 0) + 1);
        }
        int l = b.length() - 1;
        for (int i = 0; i < l; i++) {
            am.put(a.charAt(i), am.getOrDefault(a.charAt(i), 0) + 1);
        }
        int lt = 0;
        for (int rt = l; rt < a.length(); rt++) {
            am.put(a.charAt(rt), am.getOrDefault(a.charAt(rt), 0) + 1);
            if (am.equals(bm)) {
                answer += 1;
            }
            am.put(a.charAt(lt), am.get(a.charAt(lt)) - 1);
            if (am.get(a.charAt(lt)) == 0) {
                am.remove(a.charAt(lt));
            }
            lt++;
        }
        return answer;
    }
}
