package Algorany;

import java.io.*;
import java.util.*;

public class Dagak {

    static int n;
    static long[] x;
    static long[] y;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        x = new long[n + 1];
        y = new long[n + 1];
        long a = 0;
        long b = 0;
        for (int i = 0; i < n; i++) {
            StringTokenizer str = new StringTokenizer(br.readLine());
            x[i] = Integer.parseInt(str.nextToken());
            y[i] = Integer.parseInt(str.nextToken());
        }
        x[n] = x[0];
        y[n] = y[0];

        for (int i = 0; i < n; i++) {
            a += (y[i + 1] * x[i]);
            b += (y[i] * x[i + 1]);
        }
        String temp = String.format("%.1f", Math.abs(a - b) / 2.0);
        System.out.println(temp);
    }
}
