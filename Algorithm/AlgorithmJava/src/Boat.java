import java.util.*;

public class Boat {

    public static void main(String[] args) {
        Boat T = new Boat();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> crane = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            crane.add(sc.nextInt());
        }
        int m = sc.nextInt();
        ArrayList<Integer> boxWeight = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            boxWeight.add(sc.nextInt());
        }
        System.out.print(T.Solution(n, crane, m, boxWeight));
    }

    private int Solution(int n, ArrayList<Integer> crane, int m, ArrayList<Integer> boxWeight) {
        /**
         한계에 비슷한 크레인에 박스를 배당하는게 좋음.
         => 먼저 박스들을 내림차순으로 정렬한 다음에 젤 높은 것부터 처리
         */
        Collections.sort(crane, Collections.reverseOrder());
        Collections.sort(boxWeight, Collections.reverseOrder());

        if (boxWeight.get(0) > crane.get(0)) { // 아예 처리못하는거 있을 때
            return -1;
        }
        int answer = 0;
        while (!boxWeight.isEmpty()) {
            int idx = 0;
            for (int i = 0; i < n; ) {
                if (boxWeight.size() == idx) {
                    break;
                }
                else if (boxWeight.get(idx) <= crane.get(i)) { //
                    boxWeight.remove(idx);
                    i += 1; // 다음 크레인이 다음 박스 처리하도록
                } else if (boxWeight.get(idx) > crane.get(i)) {
                    idx += 1; // 처리 안되는 박스라면 크레인이 다음 무게의 박스 처리하도록 하기
                }
            }
            answer += 1;
        }
        return answer;
    }

}
