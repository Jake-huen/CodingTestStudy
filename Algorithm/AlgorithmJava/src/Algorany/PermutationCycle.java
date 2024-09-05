package Algorany;

import java.util.*;
import java.io.*;

public class PermutationCycle {

    static int t; // 테스트케이스 개수
    static int n; // 순열의 크기
    static int[] graph; // 순열
    static Map<Integer, Integer> map; // 순열 맵

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());
        ArrayList<Integer> answer = new ArrayList<>();
        for (int temp = 0; temp < t; temp++) {
            n = Integer.parseInt(br.readLine());
            graph = new int[n];
            StringTokenizer str = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                graph[i] = Integer.parseInt(str.nextToken());
            }
            map = new LinkedHashMap<>();
            for (int i = 1; i <= n; i++) {
                map.put(i, graph[i - 1]);
            }

            int result = 0;
            boolean[] visited = new boolean[n + 1];
            for (int i = 1; i <= n; i++) {
                if (!visited[i]) {
                    int start = i;
                    while(true){
                        int next = map.get(start);
                        if(visited[next]){
                            break;
                        } else {
                            visited[next] = true;
                            start = next;
                        }
                    }
                    result += 1;
                }
            }
            answer.add(result);
        }
        for (int i : answer) {
            System.out.println(i);
        }
    }
}
