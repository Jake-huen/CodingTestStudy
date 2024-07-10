package Algorany;

import java.io.*;
import java.util.*;

public class CatchHoney2 {
    static int n;
    static int[] honey;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer str = new StringTokenizer(br.readLine());
        honey = new int[n];
        for (int i = 0; i < n; i++) {
            honey[i] = Integer.parseInt(str.nextToken());
        }

        // 꿀이 젤 오른쪽에 있을 때
        int fixedBee = Arrays.stream(honey).sum() - honey[0];
        int movedBee = fixedBee;
        int ans = 0;
        for (int i = 1; i < n - 1; i++) {
            movedBee -= honey[i];
            ans = Math.max(ans, movedBee + fixedBee - honey[i]);
        }
        // 꿀이 젤 왼쪽에 있을 때
        fixedBee = Arrays.stream(honey).sum() - honey[n - 1];
        movedBee = fixedBee;
        for (int i = n - 2; i > 0; i--) {
            movedBee -= honey[i];
            ans = Math.max(ans, movedBee + fixedBee - honey[i]);
        }
        // 꿀이 중간에 있을 때
        int temp = Arrays.stream(honey).sum() - honey[0] - honey[n - 1];
        for (int i = 1; i < n - 1; i++) {
            ans = Math.max(ans, temp + honey[i]);
        }
        System.out.println(ans);
    }
}
