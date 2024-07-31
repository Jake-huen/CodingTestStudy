package Algorany;

import java.io.*;
import java.util.*;

public class MaxHeap {

    static int n;
    static int x;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>((o1, o2) -> {
            return o1 - o2;
        });
        for (int i = 0; i < n; i++) {
            x = Integer.parseInt(br.readLine());
            if (x > 0) { // 삽입
                pq.add(x);
            } else { // 배열에서 가장 큰 값 출력
                if (!pq.isEmpty()) {
                    System.out.println(pq.poll());
                }else {
                    System.out.println(0);
                }

            }
        }
    }
}
