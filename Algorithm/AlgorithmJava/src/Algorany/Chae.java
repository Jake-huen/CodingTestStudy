package Algorany;

import java.util.*;
import java.io.*;

public class Chae {

    static int N;
    static int K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());
        N = Integer.parseInt(str.nextToken());
        K = Integer.parseInt(str.nextToken());
        int idx = 0;
        boolean[] visited = new boolean[N + 1];
        for (int i = 2; i <= N; i++) {
            if (!visited[i]) {
                for (int j = i; j <= N; j += i) {
                    if (!visited[j]) {
                        visited[j] = true;
                        idx += 1;
                        if (idx == K) {
                            System.out.println(j);
                            return;
                        }
                    }
                }
            }
        }
    }
}
