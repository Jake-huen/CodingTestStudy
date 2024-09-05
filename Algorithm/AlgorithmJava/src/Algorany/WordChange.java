package Algorany;

import java.util.*;

public class WordChange {
    ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    Map<Integer, String> hashMap;
    int n;

    public int solution(String begin, String target, String[] words) {
        for (int i = 0; i <= words.length; i++) {
            graph.add(new ArrayList<>());
        }
        n = words.length;
        int answer = Integer.MAX_VALUE;
        hashMap = new LinkedHashMap<>();
        for (int i = 0; i < words.length; i++) {
            hashMap.put(i, words[i]);
        }
        hashMap.put(words.length, begin);
        int beg = words.length;
        int tar = -1;

        // target이 words에 존재하는지 확인
        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(target)) {
                tar = i;
                break;
            }
        }

        // target이 존재하지 않으면 변환 불가
        if (tar == -1) return 0;

        for (int i = 0; i <= words.length; i++) {
            String word1 = hashMap.get(i);
            for (int j = i + 1; j <= words.length; j++) {
                String word2 = hashMap.get(j);
                int cnt = 0;
                for (int t = 0; t < word1.length(); t++) {
                    if (word1.charAt(t) != word2.charAt(t)) {
                        cnt += 1;
                    }
                }
                if (cnt == 1) {
                    graph.get(i).add(j);
                    graph.get(j).add(i);
                }
            }
        }

        answer = bfs(beg, tar);
        return answer == Integer.MAX_VALUE ? 0 : answer;
    }

    public int bfs(int start, int target) {
        Queue<int[]> q = new LinkedList<>();
        boolean[] visited = new boolean[n + 1];
        visited[start] = true;
        q.add(new int[]{start, 0});

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int index = cur[0];
            int cost = cur[1];
            if (index == target) {
                return cost;
            }
            for (int i : graph.get(index)) {
                if (!visited[i]) {
                    q.add(new int[]{i, cost + 1});
                    visited[i] = true;
                }
            }
        }
        return Integer.MAX_VALUE;
    }

    public static void main(String[] args) {
        WordChange wc = new WordChange();
        System.out.println(wc.solution("hit", "cog", new String[]{"hot", "dot", "dog", "lot", "log", "cog"})); // 4
        System.out.println(wc.solution("hit", "cog", new String[]{"hot", "dot", "dog", "lot", "log"})); // 0
    }
}
