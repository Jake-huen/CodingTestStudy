import java.util.*;

public class ranking {

    public static int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        HashMap<String, Integer> nameMap = new HashMap<>();
        for(int i=0;i<name.length;i++){
            nameMap.put(name[i],yearning[i]);
        }
        for(int i=0;i<photo.length;i++){
            int ans = 0;
            for(int j=0;j<photo[i].length;j++){
                String temp = photo[i][j];
                if (nameMap.get(temp) != null) {
                    ans+=nameMap.get(temp);
                }
            }
            answer[i] = ans;
        }
        return answer;
    }

    public static void main(String[] args) {
        String[] name = {"may", "kein", "kain", "radi"};
        int[] yearning = {5, 10, 1, 3};
        String[][] photo = {{"may", "kein", "kain", "radi"},{"may", "kein", "brin", "deny"}, {"kon", "kain", "may", "coni"}};
        System.out.println(solution(name,yearning,photo));
    }
}
