package Algorany;

import java.util.*;

public class BuyingCookie {

    int answer;

    public int solution(int[] cookie) {
        answer = 0;

        for (int i = 1; i <= cookie.length - 1; i++) {
            int left = i;
            int leftSum = cookie[i];
            int right = i + 1;
            int rightSum = cookie[i + 1];
            while (true) {
                if (leftSum == rightSum && answer < leftSum) {
                    answer = leftSum;
                } else if (leftSum <= rightSum && left != 0) {
                    left -= 1;
                    leftSum += cookie[left];
                } else if (leftSum >= rightSum && right != cookie.length - 1) {
                    right += 1;
                    rightSum += cookie[right];
                } else {
                    break;
                }
            }
        }
        System.out.println(answer);
        return answer;
    }

    public static void main(String[] args) {
        BuyingCookie bc = new BuyingCookie();
        bc.solution(new int[]{1, 2, 3, 3});
        bc.solution(new int[]{1, 2, 4, 5});
    }

}
