package Algorany;

import java.util.*;
import java.util.stream.Collectors;

public class AutoComplete {

    public int solution(String[] words) {
        int answer = 0;
        int[][] graph = new int[words.length][words.length];
        Arrays.sort(words);
        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j < words.length; j++) {
                graph[i][j] = -1;
            }
        }
        // 같은 글자가 하나라도 있으면 계속해서 입력해야함.
        for (int i = 0; i < words.length; i++) {
            String check = words[i];
            for (int j = i + 1; j < words.length; j++) {
                int idx = words[i].length();
                int count = 0;
                int k;
                for (k = 0; k < idx; k++) {
                    if (check.charAt(k) == words[j].charAt(k)) {
                        count += 1;
                    } else {
                        break;
                    }
                }
                if (k == idx) {
                    graph[i][j] = Math.max(graph[i][j], count);
                    graph[j][i] = Math.max(graph[j][i], count + 1);
                } else {
                    graph[i][j] = Math.max(graph[i][j], count + 1);
                    graph[j][i] = Math.max(graph[j][i], count + 1);
                }
            }
        }

        for (int i = 0; i < words.length; i++) {
            int temp = 0;
            for (int j = 0; j < words.length; j++) {
                System.out.println("i " + words[i] + " j " + words[j] + " " + graph[i][j]);
                temp = Math.max(temp, graph[i][j]);
                temp = Math.min(temp, words[i].length());
            }
            answer += temp;
        }
        System.out.println(answer);
        return answer;
    }

    public static void main(String[] args) {
        AutoComplete autoComplete = new AutoComplete();
        autoComplete.solution(new String[]{"go", "gone", "guild"}); // 7
        autoComplete.solution(new String[]{"abc", "def", "ghi", "jklm"}); // 4
        autoComplete.solution(new String[]{"word", "war", "warrior", "world"}); // 15
    }
}
