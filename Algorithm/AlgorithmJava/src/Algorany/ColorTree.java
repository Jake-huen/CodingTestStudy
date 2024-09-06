package Algorany;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class ColorTree {

    static int Q;
    static ArrayList<Integer> answer;

    static class Node {
        int m_id;
        int p_id;
        int color;
        int cur_depth;
        int max_depth;
        Set<Integer> cost;

        Node(int m_id, int p_id, int color, int cur_depth, int max_depth, Set<Integer> cost) {
            this.m_id = m_id;
            this.p_id = p_id;
            this.color = color;
            this.cur_depth = cur_depth;
            this.max_depth = max_depth;
            this.cost = cost;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Q = Integer.parseInt(br.readLine());
        ArrayList<Node> cur = new ArrayList<>();
        for (int i = 0; i < Q; i++) {
            String[] s = br.readLine().split(" ");
            if (s[0].equals("100")) { // 노드 추가
                int m_id = Integer.parseInt(s[1]); // 고유 번호
                int p_id = Integer.parseInt(s[2]); // 부모 노드 번호 -1이면
                int color = Integer.parseInt(s[3]); // 색깔
                int max_depth = Integer.parseInt(s[4]); // 최대 깊이
                Node node = new Node(m_id, p_id, color, 1, max_depth, new HashSet<>(color));
                if (p_id == -1) {
                    cur.add(node);
                } else {
                    for (Node n : cur) {
                        if (n.m_id == p_id) {
                            if (n.cur_depth < n.max_depth) {
                                n.cur_depth += 1;
                                n.cost.add(node.color);
                                cur.add(node);
                            }
                            break;
                        }
                    }
                }
            } else if (s[0].equals("200")) { // 색깔 변경
                // 서브 트리 내 모든 노드의 색깔 변경
                int m_id = Integer.parseInt(s[1]); // 고유 번호
                int color = Integer.parseInt(s[2]); // 바꿀 색깔
                for (Node n : cur) {
                    if (n.m_id == m_id) { // 부모 노드
                        Queue<Node> q = new LinkedList<>();
                        q.add(n);
                        n.color = color;
                        n.cost = new HashSet<>(color);
                        while (!q.isEmpty()) {
                            Node now = q.poll();
                            for (int idx = 0; idx < cur.size(); idx++) {
                                if (cur.get(idx).p_id == now.m_id) {
                                    q.add(cur.get(idx));
                                    cur.get(idx).color = color;
                                    cur.get(idx).cost = new HashSet<>(color);
                                }
                            }
                        }
                    }
                }

            } else if (s[0].equals("300")) { // 색깔 조회
                int m_id = Integer.parseInt(s[1]); // 고유 번호
                for (int idx = 0; idx < cur.size(); idx++) {
                    if (cur.get(idx).m_id == m_id) {
                        System.out.println(cur.get(idx).color);
                    }
                }
            } else if (s[0].equals("400")) { // 점수 조회
                int answer = 0;
                for (int idx = 0; idx < cur.size(); idx++) {
                    int temp = cur.get(idx).cost.size();
                    answer += (temp * temp);
                }
                System.out.println(answer);
            }
        }
    }
}
//15
//100 1 -1 1 3
//100 2 1 2 1
//100 3 2 3 2
//400
//100 4 1 1 3
//100 5 4 3 2
//400
//200 4 4
//100 6 4 5 2
//300 1
//300 5
//300 6
//400
//200 2 4
//400

//5
//15
//1
//4
//5
//23
//16