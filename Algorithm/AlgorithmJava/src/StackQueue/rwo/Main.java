package StackQueue.rwo;

import java.util.Scanner;
import java.util.Stack;

public class Main {


    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        System.out.println(T.solution(s));
    }

    private String solution(String s) {
        String result = "";
        Stack<Character> stack = new Stack<>();
        for (char x : s.toCharArray()) {
            if (x == ')') {
                while (stack.pop() != '(');
            }
            else {
                stack.push(x);
            }
        }
        for (int i = 0; i < stack.size(); i++) {
            result += stack.get(i);
        }
        return result;
    }
}
