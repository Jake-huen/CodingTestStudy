package Algorany;

import java.util.*;

public class FindBackBigNumber {

    public static void main(String[] args) {
        int[] answer = solution(new int[]{2, 3, 3, 5});
        for (int i : answer) {
            System.out.println(i);
        }

        answer = solution(new int[]{9, 1, 5, 3, 6, 2});
        for (int i : answer) {
            System.out.println(i);
        }
    }

    public static int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        Deque<Integer> stack = new LinkedList<>();
        for (int i = numbers.length - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() <= numbers[i]) {
                stack.pop();
            }
            if (stack.isEmpty()) {
                answer[i] = -1;
            } else {
                answer[i] = stack.peek();
            }
            for (Integer integer : stack) {
                System.out.println(integer);
            }
            stack.push(numbers[i]);
            System.out.println();
        }
        return answer;
    }
}
