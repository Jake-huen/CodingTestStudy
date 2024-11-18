package Algorany.KFTC;

import java.util.*;

public class Three {
    public static void main(String[] args) {
        // 여러 개의 입력 문자열
        List<String> inputs = Arrays.asList("011010111", "110011", "111", "011010111", "0011");
        Map<List<Integer>, List<Integer>> indexMap = new HashMap<>();

        // 각 입력 문자열에 대해 연속된 1의 개수 세기
        for (int inputIndex = 0; inputIndex < inputs.size(); inputIndex++) {
            String input = inputs.get(inputIndex);
            List<Integer> counts = countContinuousOnes(input);
            System.out.println("Input: " + input + " -> Counts: " + counts); // 중간 출력

            // 인덱스를 Map에 저장
            indexMap.putIfAbsent(counts, new ArrayList<>());
            indexMap.get(counts).add(inputIndex); // 현재 입력 문자열의 인덱스 저장
        }

        // 같은 count 값 찾기
        for (Map.Entry<List<Integer>, List<Integer>> entry : indexMap.entrySet()) {
            List<Integer> keys = entry.getKey();
            List<Integer> indices = entry.getValue();
            if (indices.size() > 1) {
                System.out.println("Counts: " + keys + " found in inputs at indices: " + indices);
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

// HashMap을 사용하였습니다. 해당 문자열을 분석해서 01101 이런식이면 key값을 2 1로 String 형식으로 저장하여서, 
// 해당 key 값에 해당하는 다른 문자열을 모두 저장하여서 출력할 수 있습니다. 