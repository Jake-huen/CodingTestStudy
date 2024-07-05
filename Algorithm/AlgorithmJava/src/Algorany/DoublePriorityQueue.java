package Algorany;

import java.util.*;

class DoublePriorityQueue {
    public static int[] solution(String[] operations) {
        int[] answer = new int[2];
        PriorityQueue<Integer> maxQueue = new PriorityQueue<>((o1, o2) -> {
            return o2 - o1;
        });
        PriorityQueue<Integer> minQueue = new PriorityQueue<>((o1, o2) -> {
            return o1 - o2;
        });
        Queue<Integer> queue = new LinkedList<>();
        for (String operation : operations) {
            String[] orders = operation.split(" ");
            if (orders[0].equals("I")) { // 큐에 주어진 숫자를 삽입합니다.
                maxQueue.add(Integer.parseInt(orders[1]));
                minQueue.add(Integer.parseInt(orders[1]));
            } else if (orders[0].equals("D") && orders[1].equals("1")) { // 큐에서 최댓값을 삭제합니다.
                int maxValue;
                if(!maxQueue.isEmpty()){
                    maxValue = maxQueue.poll();
                    if(!minQueue.isEmpty()){
                        minQueue.remove(maxValue);
                    }
                }
            } else { // 큐에서 최솟값을 삭제합니다.
                int minValue;
                if(!minQueue.isEmpty()){
                    minValue = minQueue.poll();
                    if(!maxQueue.isEmpty()){
                        maxQueue.remove(minValue);
                    }
                }
            }
        }
        if (minQueue.isEmpty() && maxQueue.isEmpty()) {
            answer[0] = 0;
            answer[1] = 0;
        } else {
            answer[0] = maxQueue.poll();
            answer[1] = minQueue.poll();
        }

        return answer;
    }

    public static void main(String[] args) {
        solution(new String[]{"I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"});
    }
}