package Algorany;

import java.util.*;

public class GwangMulKaeGi {

    int d;
    ArrayList<Integer> result;
    ArrayList<ArrayList<Integer>> cases;
    int[] p;

    public int solution(int[] picks, String[] minerals) {
        p = picks;
        int answer = Integer.MAX_VALUE;
        int len = minerals.length;
        int temp= 0;
        for(int pick : picks){
            temp +=pick;
        }
        d = Math.min(len / 5 + 1, temp);
        result = new ArrayList<>();
        cases = new ArrayList<>();
        dupperm(0);
        for (ArrayList<Integer> aCase : cases) {
            int piro = 0;
            for (int i = 0; i < aCase.size(); i++) {
                int pick = aCase.get(i); // 곡괭이 종류
                for (int j = i * 5; j < Math.min(minerals.length, (i + 1) * 5); j++) {
                    String mineral = minerals[j]; // 광물 종류
                    if (pick == 0) { // 다이아 곡괭이
                        if (mineral.equals("diamond")) {
                            piro += 1;
                        } else if (mineral.equals("iron")) {
                            piro += 1;
                        } else {
                            piro += 1;
                        }
                    } else if (pick == 1) { // 철 공괭이
                        if (mineral.equals("diamond")) {
                            piro += 5;
                        } else if (mineral.equals("iron")) {
                            piro += 1;
                        } else {
                            piro += 1;
                        }
                    } else { // 돌 곡괭이
                        if (mineral.equals("diamond")) {
                            piro += 25;
                        } else if (mineral.equals("iron")) {
                            piro += 5;
                        } else {
                            piro += 1;
                        }
                    }
                }
            }
            answer = Math.min(answer, piro);
        }
        System.out.println(answer);
        return answer;
    }

    public void dupperm(int depth) {
        if (depth == d) {
            int[] temp = new int[3];
            for (Integer integer : result) {
                temp[integer] += 1;
                if (temp[integer] > p[integer]) { // 넘치는 경우
                    return;
                }
            }
            cases.add(new ArrayList<>(result));
            return;
        }
        for (int i = 0; i < 3; i++) { // 3가지 중복 조합
            result.add(i);
            dupperm(depth + 1);
            result.remove(result.size() - 1);
        }
    }

    public static void main(String[] args) {
        GwangMulKaeGi s = new GwangMulKaeGi();
        s.solution(new int[]{1, 3, 2}, new String[]{"diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"}); // 12
    }
}
