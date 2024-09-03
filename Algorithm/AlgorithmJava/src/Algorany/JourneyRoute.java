package Algorany;

import java.util.*;

public class JourneyRoute {

    //    private boolean[] visited;
//    private ArrayList<String> answer;
//    private int len;
//
//    public String[] solution(String[][] tickets) {
//        Map<String, List<String>> board = new HashMap<>();
//        answer = new ArrayList<>();
//        len = tickets.length;
//        visited = new boolean[tickets.length];
//
//        for (String[] ticket : tickets) {
//            board.computeIfAbsent(ticket[0], k -> new ArrayList<>()).add(ticket[1]);
//        }
//
//        for (Map.Entry<String, List<String>> entry : board.entrySet()) {
//            Collections.sort(entry.getValue());
//        }
//
//        dfs("ICN", "ICN", board, 0);
////        for (String string : answer) {
////            System.out.println(string);
////        }
//        Collections.sort(answer);
//        return answer.get(0).split(" ");
//    }
//
//    private void dfs(String start, String route, Map<String, List<String>> board, int cnt) {
//        if (cnt == len) {
//            answer.add(route);
//            return;
//        }
//
//        if (!board.containsKey(start)) {
//            return;
//        }
//
//        List<String> destinations = board.get(start);
//        Collections.sort(destinations);
//
//        for (int i = 0; i < destinations.size(); i++) {
//            String destination = destinations.get(i);
//            destinations.remove(destination);
//            dfs(destination, route + " " + destination, board, cnt+1);
//            destinations.add(destination);
//        }
//    }
    boolean[] visited;
    ArrayList<String> allRoute;

    public String[] solution(String[][] tickets) {
        String[] answer = {};
        int cnt = 0;
        visited = new boolean[tickets.length];
        allRoute = new ArrayList<>();

        dfs("ICN", "ICN", tickets, cnt);

        Collections.sort(allRoute);
        answer = allRoute.get(0).split(" ");

        return answer;
    }

    public void dfs(String start, String route, String[][] tickets, int cnt) {
        if (cnt == tickets.length) {
            allRoute.add(route);
            return;
        }

        for (int i = 0; i < tickets.length; i++) {
            String[] ticket = tickets[i];
            if (start.equals(ticket[0]) && !visited[i]) {
                visited[i] = true;
                dfs(tickets[i][1], route + " " + tickets[i][1], tickets, cnt + 1);
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) {
        JourneyRoute jr = new JourneyRoute();
        jr.solution(new String[][]{{"ICN", "JFK"}, {"HND", "IAD"}, {"JFK", "HND"}}); // ["ICN", "JFK", "HND", "IAD"]
    }
}
