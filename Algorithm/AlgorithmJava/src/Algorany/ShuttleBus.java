package Algorany;

import java.util.*;

class ShuttleBus {

    public String solution(int n, int t, int m, String[] timetable) {
        String answer = "";
        int[] busTime = new int[n]; // 버스 오는 시간
        int lastTime = 0;
        busTime[0] = 60 * 9;
        for (int i = 1; i < n; i++) {
            busTime[i] = busTime[i - 1] + t;
        }

        // 작은게 먼저 나오게 하는 우선순위 큐
        PriorityQueue<Integer> pq = new PriorityQueue<>((o1, o2) -> {
            return o1 - o2;
        });

        for (String ti : timetable) {
            String[] splited = ti.split(":");
            // 사람이 오는 시간
            int time = Integer.parseInt(splited[0]) * 60 + Integer.parseInt(splited[1]);
            pq.add(time);
        }

        int total = 0;

        for (int i = 0; i < n; i++) {
            total = 0;
            while (!pq.isEmpty()) {
                int curTime = pq.peek();
                if (curTime <= busTime[i] && total < m) { // 아직 최대 수용인원을 채우지 않았을 때
                    total += 1;
                    pq.poll();
                } else {
                    break;
                }
                lastTime = busTime[i] - 1;
            }

        }

        if (total <= m) { // 마지막까지 했을 때 정원을 채우지 못한 경우
            lastTime = busTime[n - 1];
        }
        // System.out.println(lastTime);
        int intHour = lastTime / 60;
        int intMinute = lastTime % 60;
        String hour = "";
        String minute = "";
        if (intHour == 9) {
            hour = "09";
        } else {
            hour = String.valueOf(intHour);
        }
        if (intMinute < 10) {
            minute = "0" + String.valueOf(intMinute);
        } else {
            minute = String.valueOf(intMinute);
        }

        answer = hour + ":" + minute;
        System.out.println(answer);
        return answer;
    }

    public static void main(String[] args) {
        ShuttleBus shuttleBus = new ShuttleBus();
        shuttleBus.solution(1, 1, 5, new String[]{"08:00", "08:01", "08:02", "08:03"});
    }
}