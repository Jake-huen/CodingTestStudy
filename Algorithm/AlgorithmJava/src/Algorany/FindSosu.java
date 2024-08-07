package Algorany;

public class FindSosu {
    int l;
    int[] result;
    int answer = 0;
    int[] temp;
    boolean[] visited;

    public int solution(String numbers) {
        l = numbers.length();
        temp = new int[l];
        result = new int[l];
        for (int i = 0; i < l; i++) {
            temp[i] = numbers.charAt(i) - 48;
        }
        visited = new boolean[l];
        dfs(0);
        // System.out.println(answer);
        return answer;
    }

    public void dfs(int depth) {
        if (depth == l) {
            String ans = "";
            for (int i = 0; i < l; i++) {
                ans += String.valueOf(result[i]);
            }
            // System.out.println(ans);
            if (isValid(Integer.parseInt(ans))) {
                answer += 1;
            }
            return;
        }
        for (int i = 0; i < l; i++) {
            if (!visited[i]) {
                result[depth] = temp[i];
                visited[i] = true;
                dfs(depth + 1);
                visited[i] = false;
            }
        }
    }

    public boolean isValid(int n) {
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        FindSosu findSosu = new FindSosu();
        findSosu.solution("17");
    }
}
