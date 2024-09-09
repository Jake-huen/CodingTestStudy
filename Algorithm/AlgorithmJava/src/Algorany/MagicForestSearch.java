package Algorany;

import java.util.*;
import java.io.*;

public class MagicForestSearch {
    static StringTokenizer str;
    static int R,C,K;
    static int[][] graph;

    public static int moveGolam(int col, int dir){
        goDown();
        return 0;
    }

    public static void goDown(int row){
        int col = 0;
        while(col <= C){

        }
    }

    public static boolean isGolamOut() {
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = new StringTokenizer(br.readLine());
        int answer = 0;
        R = Integer.parseInt(str.nextToken());
        C = Integer.parseInt(str.nextToken());
        K = Integer.parseInt(str.nextToken()); // 정령 수

        graph = new int[C][R];
        for(int i=0;i<K;i++){
            str = new StringTokenizer(br.readLine());
            int row = Integer.parseInt(str.nextToken()) - 1; // 출발하는 행
            int dir = Integer.parseInt(str.nextToken()); // 출구 방향 정보
            // 0북 1동 2남 3서
            answer += moveGolam(col, dir);
            if(isGolamOut()){ // 골렘이 밖에 나가있다면
                graph = new int[C][R];
            }
        }
        System.out.println(answer);

    }
}