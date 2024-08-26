package Algorany;

import java.util.*;
import java.io.*;

public class Domino {
    static int n;
    static String[][] domino;
    // 도미노를 N개 골라야함. 선택한 도미노를 두 개가 같은 행에서 고르고, 선택한 도미노를 같은 열에서 고르면 안된다.
    // (1,3) (3,2) (2,4) (4,1)
    // 모든 도미노는 그 뒷면에 숫자가 쓰여 있다. 이 게임에서 점수를 계산할 때는 자기가 고른 도미노의 뒷면에 쓰여 있는 수를 모두 곱한다. 그 다음에 만약 사이클 그룹의 개수가 짝수가 되면 그 수에 -1을 곱한다
    // 세준이는 자기가 이 게임에서 얻을 수 있는 최대 점수와 최소 점수가 궁금해 졌다.
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine()); // 6보다 작거나 같은 자연수
        // i행 j열에 쓰여 있는 수는 도미노 (i,j)의 뒷면에 쓰여 있는 수 -> ABCDEFGHI : -1,-2,...-9
        domino = new String[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer str = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                domino[i][j] = str.nextToken();
            }
        }
        // 같은 행에서 2개를 고르기. -> N개중 2개. N-2개는 나머지 열에서 뽑아야함.
        // DP, BFS, DFS, 우선순위 큐

    }
}
