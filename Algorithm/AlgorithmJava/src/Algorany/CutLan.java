package Algorany;

import java.util.*;
import java.io.*;

public class CutLan {
    static int k, n;
    static int[] lan;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());
        k = Integer.parseInt(str.nextToken());
        n = Integer.parseInt(str.nextToken());
        lan = new int[k];
        for (int i = 0; i < k; i++) {
            lan[i] = Integer.parseInt(br.readLine());
        }
        int start = 1;
        int end = Arrays.stream(lan).max().getAsInt();
        int answer = 0;
        int mid;
        int result;
        while (start <= end) {
            mid = (start + end) / 2;
            result = 0;
            for (int i = 0; i < k; i++) {
                if (mid > 0) {
                    result += lan[i] / mid;
                }
            }
            if (result < n) {
                end = mid-1;
            } else if (result >= n) {
                answer = mid;
                start = mid + 1;
            }
        }
        System.out.println(answer);
    }

}
