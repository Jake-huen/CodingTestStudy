package StackQueue.three;

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = sc.nextInt();
            }
        }
        int m = sc.nextInt();
        int[] moves = new int[m];
        for (int i = 0; i < m; i++) {
            moves[i] = sc.nextInt();
        }
        T.solution(n, board, m, moves);
    }

    private void solution(int n, int[][] board, int m, int[] moves) {
        /*
         * 00 01 02 03 04
         * 10 11 12 13 14
         * 20 21 22 23 24
         * 30 31 32 33 34
         *
         * n-10 n1 n2 .... n-1n-1
         * */
        Stack<Integer> result = new Stack<>();
        int answer = 0;
        for (int move : moves) {
            for (int i = 0; i < board.length; i++) {
                if (board[i][move - 1] != 0) {
                    int temp = board[i][move - 1];
                    board[i][move - 1] = 0;
                    if (!result.isEmpty() && temp == result.peek()) {
                        answer += 2;
                        result.pop();
                    } else {
                        result.push(temp);
                    }
                    break;
                }
            }
        }
        System.out.println(answer);
    }
}
