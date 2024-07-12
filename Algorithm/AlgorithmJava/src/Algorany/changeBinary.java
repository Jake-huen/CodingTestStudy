package Algorany;

import java.util.*;

// 바뀐 횟수, 없앤 0의 개수
public class changeBinary {
    public int[] solution(String s) {
        int[] answer = new int[2];
        while (!s.equals("1")) {
            int result = 0;
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '0') {
                    answer[1] += 1;
                } else {
                    result += 1;
                }
            }
            StringBuilder temp = new StringBuilder();
            while (result != 0) {
                temp.append(result % 2);
                result = result / 2;
            }
            answer[0] += 1;
            s = temp.reverse().toString();
        }
        return answer;
    }

    public static void main(String[] args) {
        changeBinary c = new changeBinary();
        int[] answer = c.solution("110010101001");
        System.out.println(answer[0] + " " + answer[1]);
    }
}
