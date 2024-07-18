package Algorany;

import java.util.*;
import java.io.*;

public class ColorFirst {

    static int W, H, f, c, x1, y1, x2, y2;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());

        W = Integer.parseInt(str.nextToken()); // 가로
        H = Integer.parseInt(str.nextToken()); // 세로
        f = Integer.parseInt(str.nextToken()); // 처음에 접는 세로선
        c = Integer.parseInt(str.nextToken()); // 가로로 나누는 크기
        x1 = Integer.parseInt(str.nextToken());
        y1 = Integer.parseInt(str.nextToken());
        x2 = Integer.parseInt(str.nextToken());
        y2 = Integer.parseInt(str.nextToken());
        int temp = (x2 - x1) * (y2 - y1) * (c + 1);
        if (f <= W / 2) { // 왼쪽 크기 <= 오른쪽 크기
            if (f <= x1) { // 왼쪽 영향 없음
                System.out.println(W * H - temp);
            } else { // 왼쪽 영향
                System.out.println(W * H - (temp + (Math.min(f, x2) - x1) * (y2 - y1) * (c + 1)));
            }
        } else { // 왼쪽 크기 > 오른쪽 크기
            if (W <= x1 + f) {
                System.out.println(W * H - temp);
            } else {
                System.out.println(W * H - (temp + (Math.min(W, f + x2) - (f + x1)) * (y2 - y1) * (c + 1)));
            }
        }
    }
}
