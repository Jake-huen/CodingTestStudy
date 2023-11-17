package StackQueue.one;

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        if (T.solution(s)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }

    private boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        for (char x : s.toCharArray()) {
            if (x == '(') {
                stack.push(x);
            } else if (x == ')') {
                if (stack.isEmpty()) {
                    return false;
                }
                stack.pop();
            }
        }
        if (!stack.isEmpty()) {
            return false;
        }
        return true;
    }
}
