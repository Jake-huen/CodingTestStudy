package Algorany.테크닉;

import java.util.ArrayList;
import java.util.List;

public class 경우구하기 {

    // 분할 결과를 저장할 리스트
    private static void printPartitions(int[] partition) {
        for (int num : partition) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    // 분할 결과를 출력하는 메서드
    private static void printPartitions(List<Integer> partition) {
        for (int num : partition) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    // n을 k개의 숫자로 분할 (0 포함)
    private static void partitionWithZero(int n, int k, int[] partition, int index) {
        if (k == 1) {
            partition[index] = n;
            printPartitions(partition);
            return;
        }

        for (int i = 0; i <= n; i++) {
            partition[index] = i;
            partitionWithZero(n - i, k - 1, partition, index + 1);
        }
    }

    // n을 k개의 숫자로 분할 (0 포함하지 않음)
    private static void partitionWithoutZero(int n, int k, int[] partition, int index) {
        if (k == 1) {
            if (n > 0) {
                partition[index] = n;
                printPartitions(partition);
            }
            return;
        }

        for (int i = 1; i <= n; i++) {
            partition[index] = i;
            partitionWithoutZero(n - i, k - 1, partition, index + 1);
        }
    }

    // 주어진 정수 n의 모든 분할을 생성하는 재귀 메서드
    private static void partition(int n, int max, List<Integer> partition) {
        if (n == 0) {
            printPartitions(partition);
            return;
        }

        for (int i = Math.min(max, n); i >= 1; i--) {
            partition.add(i);
            partition(n - i, i, partition);
            partition.remove(partition.size() - 1);
        }
    }

    public static void main(String[] args) {
        int n = 8;  // 나눌 정수
        int k = 3;  // 숫자의 개수

        System.out.println("0을 포함하는 경우:");
        partitionWithZero(n, k, new int[k], 0);

        System.out.println("\n0을 포함하지 않는 경우:");
        partitionWithoutZero(n, k, new int[k], 0);
    }
}

