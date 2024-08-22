package Algorany;

import java.util.*;

public class CorrectGwalho {

    public int solution(String s) {
        int length = s.length();
        int answer = 0;
        // 문자열을 회전하면서 체크
        for (int i = 0; i <= length; i++) {
            String rotated = s.substring(i, length) + s.substring(0, i);
            if (isValid(rotated)) {
                answer +=1;
            }
        }

        return answer;
    }

    // 스택을 이용해 올바른 괄호인지 확인하는 메서드
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                char open = stack.pop();
                if ((c == ')' && open != '(') ||
                        (c == '}' && open != '{') ||
                        (c == ']' && open != '[')) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        CorrectGwalho correctGwalho = new CorrectGwalho();
        System.out.println(correctGwalho.solution("}]()[{"));
    }
}
