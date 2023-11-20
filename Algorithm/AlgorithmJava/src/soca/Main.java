package soca;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        int[][] grid = {
                {1, 2, 2, 2},
                {1, 2, 1, 1},
                {1, 2, 2, 1},
                {3, 2, 1, 1}
        };
        analyzeSquares(grid);
        System.out.println(solution(4, 3, grid));
    }

    public static int solution(int n, int k, int[][] grid) {
        int answer = -1;
        for (int i = 1; i <= k; i++) {

        }
        return answer;
    }

    private static void analyzeSquares(int[][] array) {
        int n = array.length;

        for (int size = 1; size <= n; size++) {
            System.out.println(size + "x" + size + " squares:");

            // HashMap을 정의하여 현재 정사각형의 좌표를 키로 사용
            HashMap<String, HashMap<Integer, Integer>> result = countNumbers(array, size);

            // 결과 출력
            for (String key : result.keySet()) {
                System.out.println("Starting from coordinate " + key + ":");
                HashMap<Integer, Integer> numbersCount = result.get(key);
                int maxCount = 0;
                int maxNum = -1;
                for (Map.Entry<Integer, Integer> entry : numbersCount.entrySet()) {
                    int num = entry.getKey();
                    int count = entry.getValue();
                    if (count > maxCount) {
                        maxCount = count;
                        maxNum = num;
                    }
                }

                // 나머지 값들 합계 계산
                int sumOfOtherValues = 0;
                for (Map.Entry<Integer, Integer> entry : numbersCount.entrySet()) {
                    int count = entry.getValue();
                    if (entry.getKey() != maxNum) {
                        sumOfOtherValues += count;
                    }
                }

                System.out.println("Max value: " + maxNum + " (occurs " + maxCount + " times)");
                System.out.println("Sum of other values: " + sumOfOtherValues);
                System.out.println();
            }
        }
    }

    private static HashMap<String, HashMap<Integer, Integer>> countNumbers(int[][] array, int size) {
        int n = array.length;
        HashMap<String, HashMap<Integer, Integer>> result = new HashMap<>();

        for (int i = 0; i <= n - size; i++) {
            for (int j = 0; j <= n - size; j++) {
                HashMap<Integer, Integer> numbersCount = new HashMap<>();

                for (int x = i; x < i + size; x++) {
                    for (int y = j; y < j + size; y++) {
                        int num = array[x][y];
                        numbersCount.put(num, numbersCount.getOrDefault(num, 0) + 1);
                    }
                }

                // 좌표를 키로 사용하여 결과에 추가
                String coordinate = "(" + i + ", " + j + ")";
                result.put(coordinate, numbersCount);
            }
        }

        return result;
    }
}
