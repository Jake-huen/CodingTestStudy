package Algorany;

import java.io.*;
import java.util.*;

public class RainDrop {
    static int H, W;
    static int[] blocks;
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());
        H = Integer.parseInt(str.nextToken()); // 세로길이
        W = Integer.parseInt(str.nextToken()); // 가로길이
        blocks = new int[W];
        String[] s = br.readLine().split(" ");
        for (int i = 0; i < W; i++) {
            blocks[i] = Integer.parseInt(s[i]);
        }

        // 왼쪽에서 젤 큰거, 오른쪽에서 젤 큰거 중에서 작은것과의 차이
        for (int i = 1; i < W-1; i++) {
            int left = 0;
            int right = 0;
            for (int j = 0; j < i; j++) {
                left = Math.max(blocks[j], left);
            }
            for (int j = i + 1; j < W; j++) {
                right = Math.max(blocks[j], right);
            }
            if(left > blocks[i] && right > blocks[i]){
                int temp = Math.min(left, right);
                answer += (temp - blocks[i]);
            }
        }
        System.out.println(answer);

    }
}
