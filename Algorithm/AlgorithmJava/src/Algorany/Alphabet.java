package Algorany;

import java.util.*;
import java.io.*;

public class Alphabet {
    static int r, c;
    static char[][] graph;
    static StringTokenizer str;
    static int answer;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = new StringTokenizer(br.readLine());

        r = Integer.parseInt(str.nextToken());
        c = Integer.parseInt(str.nextToken());
        graph = new char[r][c];
        for (int i = 0; i < r; i++) {
            String s = br.readLine();
            for (int j = 0; j < c; j++) {
                graph[i][j] = s.charAt(j);
            }
        }
        visited = new boolean[26];
        visited[graph[0][0] - 'A'] = true;
        dfs(0, 0, 1);
        System.out.println(answer);
    }

    public static class Node {
        int x;
        int y;
        String s;

        public Node(int x, int y, String s) {
            this.x = x;
            this.y = y;
            this.s = s;
        }
    }

    public static void dfs(int x, int y, int count) {
        answer = Math.max(answer, count);
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (0 <= nx && nx < r && 0 <= ny && ny < c) {
                if(!visited[graph[nx][ny] - 'A']){
                    visited[graph[nx][ny] - 'A'] = true;
                    dfs(nx,ny,count+1);
                    visited[graph[nx][ny] - 'A'] = false;
                }
            }
        }
    }
}
