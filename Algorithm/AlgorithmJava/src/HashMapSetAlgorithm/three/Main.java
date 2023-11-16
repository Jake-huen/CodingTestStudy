package HashMapSetAlgorithm.three;

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] mechul = new int[n];
        for (int i = 0; i < n; i++) {
            mechul[i] = sc.nextInt();
        }
        T.solution(n, k, mechul);
    }

    private void solution(int n, int k, int[] mechul) {
        List<Integer> result = new ArrayList<>();
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < k; i++) {
            map.put(mechul[i], map.getOrDefault(mechul[i], 0) + 1);
        }
        result.add(map.size());
        int lt = 0;
        int rt = k;
        while (rt < n) {
            map.put(mechul[rt], map.getOrDefault(mechul[rt], 0) + 1);
            map.put(mechul[lt], map.get(mechul[lt]) - 1);
            if (map.get(mechul[lt]) == 0) {
                map.remove(mechul[lt]);
            }
            result.add(map.size());
            rt += 1;
            lt += 1;
        }

        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i) + " ");
        }
    }
}
