package algorithm16243;

import java.util.Queue;
import java.util.Scanner;

public class Main {

    class Point{
        int x;
        int y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int l = sc.nextInt();
        int r = sc.nextInt();
        int[][] people = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                people[i][j] = sc.nextInt();
            }
        }
        T.solution(n, l, r, people);
    }

    private void solution(int n, int l, int r, int[][] people) {
    }
}
