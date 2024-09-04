package Algorany;

import java.util.*;

public class FillPuzzle {

    public int solution(int[][] game_board, int[][] table) {
        int answer = -1;
        ArrayList<ArrayList<int[]>> board = bfs(game_board);
        int col = table.length;
        int row = table[0].length;
        for (int i = 0; i < col; i++) {
            for (int j = 0; j < row; j++) {
                if (table[i][j] == 1) {
                    table[i][j] = 0;
                } else {
                    table[i][j] = 1;
                }
            }
        }
        ArrayList<ArrayList<int[]>> tb = bfs(table);
        answer = compareBlock(board, tb, answer);

//        for (ArrayList<int[]> bf : gm) {
//            for (int[] ints : bf) {
//                System.out.print(ints[0] + " " + ints[1]);
//                System.out.println();
//            }
//            System.out.println();
//        }
        System.out.println(answer);
        return answer;
    }

    private int compareBlock(ArrayList<ArrayList<int[]>> board, ArrayList<ArrayList<int[]>> table, int answer) {
        int board_size = board.size();
        int table_size = table.size();
        boolean[] visited = new boolean[board_size];

        for (int i = 0; i < table_size; i++) {
            for (int j = 0; j < board_size; j++) {
                if (visited[j] || table.get(i).size() != board.get(j).size()) {
                    continue;
                }
                if (isRotate(table.get(i), board.get(j))) {
                    visited[j] = true;
                    answer += board.get(j).size();
                    break;
                }
            }
        }


        return answer;
    }

    private boolean isRotate(ArrayList<int[]> board, ArrayList<int[]> table) {
        Collections.sort(board, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return Integer.compare(o1[0], o2[0]);
            }
        });

        // 90도씩 회전해보기, 0 90 180 270
        for (int i = 0; i < 4; i++) {
            Collections.sort(table, new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    return Integer.compare(o1[0], o2[0]);
                }
            });

            int cur_x = table.get(0)[0];
            int cur_y = table.get(0)[1];

            // 회전하면서 좌표가 바뀌기 때문에 다시 (0,0) 기준으로 정렬
            for (int j = 0; j < table.size(); j++) {
                table.get(j)[0] -= cur_x;
                table.get(j)[1] -= cur_y;
            }

            boolean check = true;

            // 좌표 비교
            for (int j = 0; j < board.size(); j++) {
                if (board.get(j)[0] != table.get(j)[0] || board.get(j)[1] != table.get(j)[1]) {
                    check = false;
                    break;
                }
            }
            if (check) {
                return true;
            } else {
                // 90도 회전시키기
                for (int j = 0; j < table.size(); j++) {
                    int temp = table.get(j)[0];
                    table.get(j)[0] = table.get(j)[1];
                    table.get(j)[1] = -temp;
                }
            }
        }
        return false;
    }

    public ArrayList<ArrayList<int[]>> bfs(int[][] graph) {
        int col = graph.length;
        int row = graph[0].length;
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        boolean[][] visited = new boolean[col][row];
        ArrayList<ArrayList<int[]>> result = new ArrayList<>();
        for (int i = 0; i < col; i++) {
            for (int j = 0; j < row; j++) {
                if (graph[i][j] == 0 && !visited[i][j]) { // 빈 공간
                    ArrayList<int[]> ans = new ArrayList<>();
                    Queue<int[]> q = new LinkedList<>();
                    q.add(new int[]{i, j});
                    ans.add(new int[]{i, j});
                    visited[i][j] = true;
                    while (!q.isEmpty()) {
                        int[] cur = q.poll();
                        for (int d = 0; d < 4; d++) {
                            int nx = cur[0] + dx[d];
                            int ny = cur[1] + dy[d];
                            if (0 <= nx && nx < col && 0 <= ny && ny < row) {
                                if (!visited[nx][ny] && graph[nx][ny] == 0) {
                                    visited[nx][ny] = true;
                                    q.add(new int[]{nx, ny});
                                    ans.add(new int[]{nx, ny});
                                }
                            }
                        }
                    }
                    result.add(ans);
                }
            }
        }
        return result;


    }

    public static void main(String[] args) {
        FillPuzzle fp = new FillPuzzle();
        fp.solution(new int[][]{{1, 1, 0, 0, 1, 0}, {0, 0, 1, 0, 1, 0}, {0, 1, 1, 0, 0, 1}, {1, 1, 0, 1, 1, 1}, {1, 0, 0, 0, 1, 0}, {0, 1, 1, 1, 0, 0}},
                new int[][]{{1, 0, 0, 1, 1, 0}, {1, 0, 1, 0, 1, 0}, {0, 1, 1, 0, 1, 1}, {0, 0, 1, 0, 0, 0}, {1, 1, 0, 1, 1, 0}, {0, 1, 0, 0, 0, 0}}); // 14
    }
}


//조각은 한 번에 하나씩 채워 넣습니다.
//조각을 회전시킬 수 있습니다.
//조각을 뒤집을 수는 없습니다.
//게임 보드에 새로 채워 넣은 퍼즐 조각과 인접한 칸이 비어있으면 안 됩니다.
// 총 몇 칸을 채울 수 있는지 return