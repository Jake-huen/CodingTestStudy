package Algorany;

import java.util.*;
import java.io.*;

public class BBH {

    static int n, s;
    static int[] arr;
    static StringTokenizer str;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = new StringTokenizer(br.readLine());
        n = Integer.parseInt(str.nextToken());
        s = Integer.parseInt(str.nextToken());
        arr = new int[n];
        str = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(str.nextToken());
        }
        answer = Integer.MAX_VALUE;
        int start = 0;
        int end = 0;
        int total = 0;
        while (start < n && end < n) {
            if (total >= s && answer > end - start) {
                answer = end - start;
            }
            if (total < s) {
                total += arr[end];
                end += 1;
            } else {
                total -= arr[start];
                start += 1;
            }
        }
        if (answer == Integer.MAX_VALUE) {
            System.out.println(0);
        } else {
            System.out.println(answer);
        }
    }
}
