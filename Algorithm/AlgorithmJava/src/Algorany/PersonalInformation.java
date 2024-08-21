package Algorany;

import java.util.*;

public class PersonalInformation {

    public int[] solution(String today, String[] terms, String[] privacies) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = 0; i < privacies.length; i++) {
            String[] temp = privacies[i].split(" ");
            String[] date = temp[0].split("\\.");
            int year = Integer.parseInt(date[0]);
            int month = Integer.parseInt(date[1]);
            int day = Integer.parseInt(date[2]);
            String rank = temp[1];
            for (String term : terms) {
                String[] ttemp = term.split(" ");
                String rrank = ttemp[0];
                int mmonth = Integer.parseInt(ttemp[1]);
                if (rank.equals(rrank)) {
                    month += mmonth;
                    if (month > 12) {
                        year += (month - 1) / 12;
                        month = (month - 1) % 12 + 1;
                    }
                    if (day == 1) {
                        day = 28;
                        month -= 1;
                    } else {
                        day -= 1;
                    }

                }
            }
            int intToday = Integer.parseInt(today.replaceAll("\\.", ""));
            String strYear = String.valueOf(year);
            String strMonth = String.valueOf(month);
            String strDay = String.valueOf(day);
            if (String.valueOf(month).length() == 1) {
                StringBuilder sb = new StringBuilder();
                sb.append("0");
                sb.append(strMonth);
                strMonth = sb.toString();
            }
            if (String.valueOf(day).length() == 1) {
                StringBuilder sb = new StringBuilder();
                sb.append("0");
                sb.append(strDay);
                strDay = sb.toString();
            }
            int intTemp = Integer.parseInt(strYear + strMonth + strDay);
//            System.out.println("intToday = " + intToday);
//            System.out.println("intTemp = " + intTemp);
            if (intToday > intTemp) {
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
        System.out.println();
        p.solution("2020.01.01",
                new String[]{"Z 3", "D 5"},
                new String[]{"2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"});
        System.out.println();
        p.solution("2020.10.15",
                new String[]{"A 100"},
                new String[]{"2018.06.16 A", "2008.02.15 A"});
    }
}
