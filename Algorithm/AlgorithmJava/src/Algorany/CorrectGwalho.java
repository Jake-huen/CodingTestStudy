package Algorany;

import java.util.*;

public class CorrectGwalho {

    public int solution(String s) {
        int answer = -1;
        for (int i = 0; i < s.length(); i++) {

        }

        return answer;
    }

    public boolean dfs(String s) {
        if (s.length() <= 2) {
            if (s.equals("()") || s.equals("{}") || s.equals("[]")) {
                return true;
            } else {
                return false;
            }
        }
        char[] arr = s.toCharArray();
        if (arr[0] == '(' && arr[arr.length - 1] == ')') {
            StringBuilder sb = new StringBuilder();
            for (int i = 1; i < arr.length - 1; i++) {
                sb.append(arr[i]);
            }
            dfs(sb.toString());
        } else if (arr[0] == '[' && arr[arr.length - 1] == ']') {
            StringBuilder sb = new StringBuilder();
            for (int i = 1; i < arr.length - 1; i++) {
                sb.append(arr[i]);
            }
            dfs(sb.toString());
        } else if (arr[0] == '{' && arr[arr.length - 1] == '}') {
            StringBuilder sb = new StringBuilder();
            for (int i = 1; i < arr.length - 1; i++) {
                sb.append(arr[i]);
            }
            dfs(sb.toString());
        } else {
            return false;
        }
        return false;
    }

    public static void main(String[] args) {

    }
}
