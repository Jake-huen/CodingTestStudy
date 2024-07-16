package Algorany;

import java.util.*;

public class AutoComplete {

    public int solution(String[] words) {
        int answer = 0;
        Arrays.sort(words);
        int[] counts = new int[words.length];

        for (int i = 0; i < words.length - 1; i++) {
            String pre = words[i];
            String next = words[i + 1];
            int len = Math.min(pre.length(), next.length());
            int sameCount = getSameCount(pre, next, len);

            if (sameCount == len) {
                counts[i] = Math.max(counts[i], sameCount);
            } else {
                counts[i] = Math.max(counts[i], sameCount + 1);
            }
            counts[i + 1] = Math.max(counts[i + 1], sameCount + 1);
        }
        for (int count : counts) {
            answer += count;
        }
        return answer;
    }

    static int getSameCount(String pre, String next, int len) {
        int count = 0;
        for (int i = 0; i < len; i++) {
            if (pre.charAt(i) != next.charAt(i)) {
                return count;
            }
            count += 1;
        }
        return count;
    }

    public static void main(String[] args) {
        AutoComplete autoComplete = new AutoComplete();
        autoComplete.solution(new String[]{"go", "gone", "guild"}); // 7
        autoComplete.solution(new String[]{"abc", "def", "ghi", "jklm"}); // 4
        autoComplete.solution(new String[]{"word", "war", "warrior", "world"}); // 15
    }
}
