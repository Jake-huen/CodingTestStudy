package Algorany;

import java.util.*;

public class MuinDoTrip {

    public int[] solution(String[] maps) {
        ArrayList<Integer> answer = new ArrayList<>();
        int col = maps.length;
        int row = maps[0].length();
        boolean[][] visited = new boolean[col][row];
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        for (int i = 0; i < col; i++) {
            for (int j = 0; j < row; j++) {
                if (maps[i].charAt(j) != 'X' && !visited[i][j]) {
                    visited[i][j] = true;
                    int ans = maps[i].charAt(j) - '0';
                    Queue<int[]> q = new LinkedList<>();
                    q.add(new int[]{i, j});
                    while (!q.isEmpty()) {
                        int[] cur = q.poll();
                        for (int d = 0; d < 4; d++) {
                            int nx = cur[0] + dx[d];
                            int ny = cur[1] + dy[d];
                            if (0 <= nx && nx < col && 0 <= ny && ny < row) {
                                if (maps[nx].charAt(ny) != 'X' && !visited[nx][ny]) {
                                    int tmp = maps[nx].charAt(ny) - '0';
                                    ans += tmp;
                                    visited[nx][ny] = true;
                                    q.add(new int[]{nx, ny});
                                }
                            }
                        }
                    }
                    answer.add(ans);
                }
            }
        }
        int[] result = new int[answer.size()];
        for (int i = 0; i < result.length; i++) {
            result[i] = answer.get(i);
        }
        Arrays.sort(result);
        return result;
    }


    public static void main(String[] args) {
        MuinDoTrip md = new MuinDoTrip();
        md.solution(new String[]{"X591X", "X1X5X", "X231X", "1XXX1"}); // [1, 1, 27]
    }
    // X는 바다, 숫자는 무인도
}
