package Algorany.KFTC;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Three {
    public static void main(String[] args) {
        String input = "011010111";
        List<Integer> counts = countContinuousOnes(input);
        Map<Integer, List<Integer>> indexMap = new HashMap<>();

        // 인덱스를 Map에 저장
        for (int i = 0; i < counts.size(); i++) {
            int count = counts.get(i);
            indexMap.putIfAbsent(count, new ArrayList<>());
            indexMap.get(count).add(i);
        }

        // 같은 값 찾기
        for (Map.Entry<Integer, List<Integer>> entry : indexMap.entrySet()) {
            List<Integer> indices = entry.getValue();
            if (indices.size() > 1) {
                System.out.println("Value: " + entry.getKey() + " at indices: " + indices);
            }
        }
    }

    private static List<Integer> countContinuousOnes(String s) {
        List<Integer> counts = new ArrayList<>();
        int count = 0;

        for (char c : s.toCharArray()) {
            if (c == '1') {
                count++;
            } else {
                if (count > 0) {
                    counts.add(count);
                    count = 0;
                }
            }
        }
        // 마지막 연속된 1의 개수 추가
        if (count > 0) {
            counts.add(count);
        }

        return counts;
    }
}
