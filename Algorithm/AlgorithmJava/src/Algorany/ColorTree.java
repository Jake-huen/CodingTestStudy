package Algorany;

import java.util.*;
import java.io.*;

public class ColorTree {
    static final int MAX_ID = 100005; // ID의 최대값
    static final int COLOR_MAX = 5;   // 색깔의 최대값
    static int Q;

    static class Node {
        int id = 0;
        int color = 0;
        int lastUpdate = 0; // 노드가 추가된 시점 또는 색깔 변경 시점
        int maxDepth = 0;    // 노드가 가질 수 있는 최대 깊이
        int parentId = 0;    // 부모 노드 ID
        List<Integer> childIds = new ArrayList<>(); // 자식 노드 ID 목록
    }

    static Node[] nodes = new Node[MAX_ID]; // 모든 노드를 저장
    static boolean[] isRoot = new boolean[MAX_ID]; // 루트 여부를 체크

    // Node 배열 초기화
    static {
        for (int i = 0; i < MAX_ID; i++) {
            nodes[i] = new Node();
        }
    }

    // 해당 노드가 자식 노드를 가질 수 있는지 확인
    static boolean canMakeChild(Node curr, int needDepth) {
        if (curr.id == 0) return true; // 루트인 경우
        if (curr.maxDepth <= needDepth) return false; // 깊이 초과 시
        return canMakeChild(nodes[curr.parentId], needDepth + 1);
    }

    // 특정 노드의 현재 색깔을 가져옴 (lazy update 방식)
    static int[] getColor(Node curr) {
        if (curr.id == 0) return new int[]{0, 0}; // 루트인 경우
        int[] info = getColor(nodes[curr.parentId]);
        if (info[1] > curr.lastUpdate) {
            return info; // 부모 색깔이 더 최신일 경우
        } else {
            return new int[]{curr.color, curr.lastUpdate}; // 현재 노드의 색깔이 최신인 경우
        }
    }

    // 트리의 점수를 계산
    static Object[] getBeauty(Node curr, int color, int lastUpdate) {
        if (lastUpdate < curr.lastUpdate) { // 현재 노드의 색깔이 최신인 경우 업데이트
            lastUpdate = curr.lastUpdate;
            color = curr.color;
        }

        int result = 0;
        Set<Integer> uniqueColors = new HashSet<>(); // 고유한 색상들을 저장
        uniqueColors.add(color);

        // 자식 노드들 순회
        for (int childId : curr.childIds) {
            Node child = nodes[childId];
            Object[] subResult = getBeauty(child, color, lastUpdate);
            result += (Integer) subResult[0];
            uniqueColors.addAll((Set<Integer>) subResult[1]); // 자식 노드에서 받은 고유 색상 추가
        }

        result += uniqueColors.size() * uniqueColors.size(); // 고유 색상 개수의 제곱을 더함
        return new Object[]{result, uniqueColors};
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Q = Integer.parseInt(br.readLine());
        HashMap<Integer, Node> cur = new LinkedHashMap<>();

        // 쿼리 처리
        for (int i = 1; i <= Q; i++) {
            String[] s = br.readLine().split(" ");
            if (s[0].equals("100")) { // 노드 추가
                int m_id = Integer.parseInt(s[1]); // 고유 번호
                int p_id = Integer.parseInt(s[2]); // 부모 노드 번호, -1이면 루트 노드
                int color = Integer.parseInt(s[3]); // 색깔
                int max_depth = Integer.parseInt(s[4]); // 최대 깊이

                if (p_id == -1) {
                    isRoot[m_id] = true; // 루트 노드 설정
                }

                // 자식 노드를 추가할 수 있는지 확인
                if (isRoot[m_id] || canMakeChild(nodes[p_id], 1)) {
                    nodes[m_id].id = m_id;
                    nodes[m_id].color = color;
                    nodes[m_id].maxDepth = max_depth;
                    nodes[m_id].parentId = isRoot[m_id] ? 0 : p_id;
                    nodes[m_id].lastUpdate = i;
                    if (!isRoot[m_id]) {
                        nodes[p_id].childIds.add(m_id); // 부모에 자식 추가
                    }
                }

            } else if (s[0].equals("200")) { // 색깔 변경
                int m_id = Integer.parseInt(s[1]); // 고유 번호
                int color = Integer.parseInt(s[2]);
                nodes[m_id].color = color;
                nodes[m_id].lastUpdate = i; // 업데이트 시점 갱신

            } else if (s[0].equals("300")) { // 색깔 조회
                int m_id = Integer.parseInt(s[1]); // 고유 번호
                System.out.println(getColor(nodes[m_id])[0]);

            } else if (s[0].equals("400")) { // 색깔 조회
                int beauty = 0;
                for (int idx = 1; idx < MAX_ID; idx++) {
                    if (isRoot[idx]) {
                        beauty += (Integer) getBeauty(nodes[idx], nodes[idx].color, nodes[idx].lastUpdate)[0];
                    }
                }
                System.out.println(beauty);
            }
        }
    }
}
