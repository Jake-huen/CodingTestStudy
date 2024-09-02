package Algorany;
import java.io.*;
import java.util.*;

public class JumpJump {

    static int n;
    static int[] graph;
    static int s;
    static boolean[] visited;
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n];
        visited = new boolean[n];

        StringTokenizer str = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            graph[i] = Integer.parseInt(str.nextToken());
        }
        s = Integer.parseInt(br.readLine()) - 1;
        dfs(s);
        System.out.println(answer);
    }

    public static void dfs(int start){
        visited[start] = true;
        answer +=1;
        int nleft = start - graph[start] >=0 ? start-graph[start] : -1;
        int nright = start + graph[start] < n ? start + graph[start] : -1;
        if (nleft != -1 && !visited[nleft]) {
            dfs(nleft);
        }
        if (nright != -1 && !visited[nright]) {
            dfs(nright);
        }
    }
}
