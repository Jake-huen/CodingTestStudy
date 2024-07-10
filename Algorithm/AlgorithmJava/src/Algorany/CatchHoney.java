package Algorany;

import java.io.*;
import java.util.*;

public class CatchHoney {

    static int n;
    static int[] honey;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        honey = new int[n];
        StringTokenizer str = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            honey[i] = Integer.parseInt(str.nextToken());
        }
        long total = 0;

        // 꿀이 젤 오른쪽에 있는 경우 -> 움직이는 벌은 1 ~ n-1 중 하나
        long fixBeeSum = Arrays.stream(honey).sum() - honey[0];
        long moveBeeSum = fixBeeSum;

        for (int i = 1; i < n - 1; i++) {
            long sum = fixBeeSum - honey[i]; // 현재 고정된 벌의 꿀 총 합
            moveBeeSum = moveBeeSum - honey[i]; // 움직이는 벌의 합
            sum += moveBeeSum;
            total = Math.max(total, sum);
        }

        // 꿀이 젤 왼쪽에 있는 경우 -> 움직이는 벌은 n-1 ~ 1 중 하나
        fixBeeSum = Arrays.stream(honey).sum() - honey[n - 1];
        moveBeeSum = fixBeeSum;

        for (int i = n - 2; i > 0; i--) {
            long sum = fixBeeSum - honey[i];
            moveBeeSum = moveBeeSum - honey[i];
            sum += moveBeeSum;
            total = Math.max(total, sum);
        }

        // 중간에 꿀통이 있는 경우
        int maxHoney = 0;
        long temp = 0;
        for (int i = 1; i < n - 1; i++) {
            temp += honey[i];
            if (honey[i] > maxHoney) {
                maxHoney = honey[i];
            }
        }
        temp += maxHoney;
        total = Math.max(temp, total);
        System.out.println(total);
    }
}
