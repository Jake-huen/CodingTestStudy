import java.util.*;

public class Main {
    public String solution(int cnt, String str) {
        String a = "";
        for (int i = 0; i < cnt; i++) {
            String temp = str.substring(7 * i, 7 * i + 7);
            String answer = "";
            for (int j = 0; j < 7; j++) {
                if (temp.charAt(j) == '#') {
                    answer += "1";
                } else if (temp.charAt(j) == '*') {
                    answer += "0";
                }
            }
            char ans = (char) Integer.parseInt(answer, 2);
            a += ans;
        }
        return a;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int cnt = kb.nextInt();
        String str = kb.next();
        System.out.println(T.solution(cnt, str));
    }
}
