package Algorany;

import java.util.*;

public class JadenCase {
    public String solution(String s) {
        String answer = "";

        String[] divided = s.split(" ");
        for (String now : divided) {
            answer += now.substring(0, 1).toUpperCase();
            answer += now.substring(1, now.length()).toLowerCase();
            answer += " ";
        }

        return answer;
    }
}
