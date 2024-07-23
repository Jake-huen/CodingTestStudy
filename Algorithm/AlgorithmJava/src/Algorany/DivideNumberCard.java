package Algorany;

import java.io.*;
import java.util.*;

public class DivideNumberCard {
    public static int solution(int[] arrayA, int[] arrayB) {
        int answer = 0;
        Arrays.sort(arrayA);
        Arrays.sort(arrayB);

        int gcdA = arrayA[0];
        int gcdB = arrayB[0];
        for (int i = 1; i < arrayA.length; i++) {
            gcdA = gcd(arrayA[i], gcdA);
            gcdB = gcd(arrayB[i], gcdB);
        }

        boolean flag = true;
        for (int a : arrayA) {
            if (a % gcdB != 0) {
                continue;
            } else {
                flag = false;
                break;
            }
        }
        if (flag) {
            answer = Math.max(answer, gcdB);
        }
        flag = true;
        for (int b : arrayB) {
            if (b % gcdA != 0) {
                continue;
            } else {
                flag = false;
                break;
            }
        }
        if (flag) {
            answer = Math.max(answer, gcdA);
        }


        return answer;
    }

    public static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else return gcd(b, a % b);
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[]{10, 17}, new int[]{5, 20}));
        System.out.println(solution(new int[]{10, 20}, new int[]{5, 17}));
        System.out.println(solution(new int[]{14, 35, 119}, new int[]{18, 30, 102}));
    }
}
