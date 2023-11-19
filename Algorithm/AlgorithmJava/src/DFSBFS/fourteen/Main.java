package DFSBFS.fourteen;

import java.util.*;

class Point {
    int x, y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {

    static int[][] city;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static ArrayList<Point> house, pizza;
    static int n;
    static int m;
    static int len;
    static int[] combi;

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        house = new ArrayList<>();
        pizza = new ArrayList<>();
        city = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                city[i][j] = sc.nextInt(); // 0:빈칸, 1:집, 2:피자집
                if (city[i][j] == 1) {
                    house.add(new Point(i, j));
                } else if (city[i][j] == 2) {
                    pizza.add(new Point(i, j));
                }
            }
        }
        len = pizza.size(); // 피자집의 개수 -> len C m
        combi = new int[m]; //
        T.DFS(0, 0);
    }

    private void DFS(int L, int s) {
        if(L==m){
            for (int x : combi) {
                System.out.print(x+" ");
            }
            System.out.println();
        }
        else{
            for (int i = s; i < len; i++) {
                combi[L] = i;
                DFS(L + 1, i + 1);
            }
        }
    }
    // 먼저 피자집들을 다 모아서 그 중에 M개를 뽑고, 뽑은 것들에 대해서 도시의 피자배달 거리를 계산
    // 그 중 최소 피자배달거리 출력
}
