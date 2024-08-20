package Algorany;

import java.util.*;

public class PersonalInformation {

    public int[] solution(String today, String[] terms, String[] privacies) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = 0; i < privacies.length; i++) {
            String[] temp = privacies[i].split(" ");
            String[] date = temp[0].split("\\.");
            String year = date[0];
            String month = date[1];
            String day = date[2];
            String rank = temp[1];
            for (String term : terms) {
                String[] ttemp = term.split(" ");
                String rrank = ttemp[0];
                String mmonth = ttemp[1];
                if (rank.equals(rrank)) {
                    month += mmonth;
                    if (Integer.parseInt(month) > 12) {
                        year = String.valueOf(Integer.parseInt(year) + 1);
                    }
                    day = String.valueOf(Integer.parseInt(day) - 1);
                }
            }
            int intToday = Integer.parseInt(today.replaceAll("\\.", ""));
            int intTemp = Integer.parseInt(year + month + day);
            if (intToday <= intTemp) {
                answer.add(i + 1);
            }
        }
        int[] result = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            result[i] = answer.get(i);
            System.out.println(result[i]);
        }
        return result;
    }

    public static void main(String[] args) {
        PersonalInformation p = new PersonalInformation();
        p.solution("2022.05.19",
                new String[]{"A 6", "B 12", "C 3"},
                new String[]{"2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"});
        // [1,3]
    }
}
