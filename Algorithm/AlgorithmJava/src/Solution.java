import java.util.Arrays;

class Solution {

    public String[] solution(String[] players, String[] callings) {
        String[] answer = new String[players.length];
        for(int i=0;i<callings.length;i++){
            int index = Arrays.asList(players).indexOf(callings[i]);
            String first = players[index-1];
            String second = players[index];
            players[index-1] = second;
            players[index] = first;
        }
        for(int i=0;i<players.length;i++){
            answer[i] = players[i];
        }
        return answer;
    }

    public static void main(String[] args) {

    }
}