package Algorany;

import java.util.*;

public class fourHigh {
    class Node {
        String s;
        int n;

        Node(String s, int n) {
            this.s = s;
            this.n = n;
        }
    }


    // 올바른 문자열인지
    public boolean isRight(String s) {
        if (s.startsWith("+")) {
            return false;
        } else {
            int star = 0;
            int plus = 0;
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '+') {
                    plus += 1;
                } else if (s.charAt(i) == '*') {
                    star += 1;
                }
            }
            if (star * 2 == plus) {
                return true;
            }
            return false;
        }
    }

    // n으로 나올 수 있는 문자열
    public Set<String> cases(int n) {
        HashMap<String, Integer> check = new HashMap<>();
        Set<String> result = new LinkedHashSet<>();
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node("", n));
        while (!queue.isEmpty()) {
            Node curNode = queue.poll();
            if (curNode.n == 1) {
                check.put(curNode.s, 1);
                result.add(curNode.s);
                continue;
            }
            if (curNode.n % 3 == 0) {
                int isFirst = check.getOrDefault("*" + curNode.s, 0);
                if(isFirst == 0){
                    queue.add(new Node("*" + curNode.s, curNode.n / 3));
                    check.put("*" + curNode.s, 1);
                }
            }
            int isFirst = check.getOrDefault("+" + curNode.s, 0);
            if(isFirst == 0){
                queue.add(new Node("+" + curNode.s, curNode.n - 1));
                check.put("+" + curNode.s, 1);
            }
        }
        return result;
    }

    public int solution(int n) {
        int answer = 0;
        Set<String> result = cases(n);
        for (String s : result) {
            //System.out.println(s);
            if (isRight(s)) {
                answer += 1;
            }
        }
        // System.out.println("answer = " + answer);
        return answer;
    }

}
