package Algorany;

import java.util.*;
import java.io.*;

public class Terminal {
    static int n, answer = 0;
    static Integer[][] timeTable;
    static int[] arr;
    static Integer min_departure = 246060999, max_arrive = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        arr = new int[24 * 60 * 60 * 1000];
        n = Integer.parseInt(br.readLine());
        timeTable = new Integer[n][2];
        for (int i = 0; i < n; i++) {
            StringTokenizer str = new StringTokenizer(br.readLine());
            timeTable[i][0] = convertTimeToMS(str.nextToken()); // 출발 시간
            //System.out.println("timeTable = " + timeTable[i][0]);
            min_departure = Math.min(min_departure, timeTable[i][0]);
            timeTable[i][1] = convertTimeToMS(str.nextToken()); // 도착 시간
            //System.out.println("timeTable = " + timeTable[i][1]);
            max_arrive = Math.max(max_arrive, timeTable[i][1]);
            arr[timeTable[i][0]] += 1;
            arr[timeTable[i][1]] -= 1;
        }

//        System.out.println("min_departure = " + min_departure);
//        System.out.println("max_arrive = " + max_arrive);
        int total = 0;
        for (int i = min_departure; i <= max_arrive; i++) {
            total += arr[i];
            answer = Math.max(answer, total);
        }
        System.out.println(answer);
    }

    public static Integer convertTimeToMS(String time) {
        String[] splitedTime = time.split(":");
        int minute = Integer.parseInt(splitedTime[1]) + Integer.parseInt(splitedTime[0]) * 60;
        int second = Integer.parseInt(splitedTime[2].split("\\.")[0]) + minute * 60;
        return second * 1000 + Integer.parseInt(splitedTime[2].split("\\.")[1]);
    }
}
