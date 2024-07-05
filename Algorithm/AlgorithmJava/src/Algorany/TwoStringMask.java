package Algorany;

import java.util.*;
import java.io.*;

public class TwoStringMask {

    static String s1;
    static String s2;
    static String answer;

    public static class Node {
        int pos1, pos2;
        String result;

        Node(int pos1, int pos2, String result) {
            this.pos1 = pos1;
            this.pos2 = pos2;
            this.result = result;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s1 = br.readLine();
        s2 = br.readLine();

        if (s1.replace("*", "").equals(s2.replace("*", ""))) {
            answer = s1.replace("*", "");
        } else if (s1.equals("*")) {
            answer = s2.replace("*", "");
        } else if (s2.equals("*")) {
            answer = s1.replace("*", "");
        } else {
            answer = solution(s1, s2);
        }
        System.out.println(answer);
    }

    public static String solution(String s1, String s2) {
        Deque<Node> queue = new ArrayDeque<>();
        queue.add(new Node(0, 0, ""));
        String ret = s1 + s2;

        while (!queue.isEmpty()) {
            Node node = queue.pollFirst();

            if (node.pos1 == s1.length() && node.pos2 == s2.length()) { // s1과 s2를 끝까지 확인하였을 때
                if (ret.length() > node.result.length()) {
                    ret = node.result;
                }
                continue;
            } else if (node.pos1 == s1.length()) {
                String suffix = s2.substring(node.pos2).replace("*", "");
                String prefix = s2.substring(0, node.pos2).replace("*", "");
                if (node.result.endsWith(suffix) && !(suffix.length() > 0 && prefix.endsWith(suffix))) {
                    String result = node.result + suffix;
                    if (ret.length() > result.length()) {
                        ret = result;
                    }
                }
                continue;
            } else if (node.pos2 == s2.length()) {
                String suffix = s1.substring(node.pos1).replace("*", "");
                String prefix = s1.substring(0, node.pos1).replace("*", "");
                if (node.result.endsWith(suffix) && !(suffix.length() > 0 && prefix.endsWith(suffix))) {
                    String result = node.result + suffix;
                    if (ret.length() > result.length()) {
                        ret = result;
                    }
                }
                continue;
            }

            char ch1 = s1.charAt(node.pos1);
            char ch2 = s2.charAt(node.pos2);

            if (ch1 == ch2) {
                String result = ch1 == '*' ? node.result : node.result + ch1;
                queue.add(new Node(node.pos1 + 1, node.pos2 + 1, result));

                if (ch1 == '*') {
                    queue.add(new Node(node.pos1 + 1, node.pos2, result));
                    queue.add(new Node(node.pos1, node.pos2 + 1, result));
                }
            }
            if (ch1 == '*' && ch2 != '*') {
                String result = node.result + ch2;
                queue.add(new Node(node.pos1, node.pos2 + 1, result));
                queue.add(new Node(node.pos1 + 1, node.pos2 + 1, result));

                // '*'을 빈 문자열로 없애는 경우
                queue.add(new Node(node.pos1 + 1, node.pos2, node.result));
            }
            if (ch1 != '*' && ch2 == '*') {
                String result = node.result + ch1;
                queue.add(new Node(node.pos1 + 1, node.pos2, result));
                queue.add(new Node(node.pos1 + 1, node.pos2 + 1, result));

                // '*'을 빈 문자열로 없애는 경우
                queue.add(new Node(node.pos1, node.pos2 + 1, node.result));
            }
        }

        return ret.equals(s1 + s2) ? "-1" : ret;
    }
}
