package Algorany;

import java.io.*;
import java.util.*;

public class Lamp {
    static int n, m, k;
    static String str[];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        str = new String[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            str[i] = st.nextToken();
        }
        st = new StringTokenizer(br.readLine());
        k = Integer.parseInt(st.nextToken());

        Map<String, Integer> arr = new HashMap<>();
        for (int i = 0; i < n; i++) {
            arr.put(str[i], arr.getOrDefault(str[i], 0) + 1);
        }

        List<String> keySet = new ArrayList<>(arr.keySet());
        keySet.sort(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return arr.get(o2).compareTo(arr.get(o1));
            }
        });

        for (String temp : keySet) {
            if (isPossibleLight(temp, k)) {
                // System.out.println(temp);
                System.out.println(arr.get(temp));
                return;
            }
        }
        System.out.println(0);
    }

    // 1. 0의 갯수가 k보다 작아야함 2. 0의 갯수%2 == k%2
    public static boolean isPossibleLight(String arr, int k) {
        int zeroCount = 0;
        for (int i = 0; i < arr.length(); i++) {
            if (arr.charAt(i) == '0') {
                zeroCount += 1;
            }
        }
        if (zeroCount > k) {
            return false;
        }
        if (zeroCount % 2 != k % 2) {
            return false;
        }
        return true;
    }
}
