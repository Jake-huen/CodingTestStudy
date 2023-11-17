package StackQueue.four;

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        T.solution(s);
    }

    private void solution(String s) {
        Stack<Integer> result = new Stack<>();
        for (char x : s.toCharArray()) {
            if (x == '+') {
                int b = result.pop();
                int a = result.pop();
                result.push(a + b);
            } else if (x == '-') {
                int b = result.pop();
                int a = result.pop();
                result.push(a - b);
            } else if (x == '*') {
                int b = result.pop();
                int a = result.pop();
                result.push(a * b);
            } else if (x == '/') {
                int b = result.pop();
                int a = result.pop();
                result.push(a / b);
            } else {
                result.push(Integer.parseInt(String.valueOf(x)));
            }
        }
        System.out.println(result.pop());
    }
}
