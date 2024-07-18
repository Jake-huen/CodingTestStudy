package Algorany;

public class RevealNumber {
    public int solution(int num) {
        int answer = 0;
        for (int i = 1; i <= num; i += 2)
            if (num % i == 0)
                answer++;

        return answer;
    }

    public static void main(String[] args) {
        RevealNumber rn = new RevealNumber();
        rn.solution(15);
    }
}
