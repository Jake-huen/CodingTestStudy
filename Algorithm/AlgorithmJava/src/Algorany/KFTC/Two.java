package Algorany.KFTC;

public class Two {

    public static boolean isCorrectAnswer(String correctAnswer, String userAnswer) {
        // 1. 대소문자 구분을 없애기 위해 소문자로 변환
        correctAnswer = correctAnswer.toLowerCase();
        userAnswer = userAnswer.toLowerCase();
        
        // 2. 정답 문자열을 한 글자씩 비교하기 위해 인덱스 사용
        int correctIndex = 0;
        int userIndex = 0;

        while (correctIndex < correctAnswer.length() && userIndex < userAnswer.length()) {
            char correctChar = correctAnswer.charAt(correctIndex);
            char userChar = userAnswer.charAt(userIndex);

            if (correctChar == ' ') {
                // 정답 문자열의 공백은 무시하고 넘어간다
                correctIndex++;
                continue;
            }

            if (userChar == ' ') {
                // 답안 문자열에 불필요한 공백이 포함되었을 경우 오답
                return false;
            }

            if (correctChar != userChar) {
                // 두 문자가 다르면 오답
                return false;
            }

            // 두 문자가 일치하면 다음 문자로 진행
            correctIndex++;
            userIndex++;
        }

        // 남은 문자가 정답 문자열에만 공백으로 있는 경우는 허용
        while (correctIndex < correctAnswer.length()) {
            if (correctAnswer.charAt(correctIndex) != ' ') {
                return false;
            }
            correctIndex++;
        }

        // 답안 문자열이 끝까지 비교된 경우에만 정답 처리
        return userIndex == userAnswer.length();
    }

    public static void main(String[] args) {
        // 테스트 케이스
        System.out.println(isCorrectAnswer("Nile river", "nileRiver")); // true
        System.out.println(isCorrectAnswer("Nile river", "N ileRiver")); // false
        System.out.println(isCorrectAnswer("Nile river", "NileRiver")); // true
        System.out.println(isCorrectAnswer("Nile river", "N ile River")); // false
    }
}



// 정답 문자열과 답안 문자열이 주어져. 답안이 정답에 해당하는지 여부를 리턴하는 문제야. 해당하는 조건은 다음과 같아. 
// 1. 대소문자는 신경쓰지 않는다. 
// 2. 정답 문자열의 띄어쓰기를 생략한 것은 신경쓰지 않는다. 
// 3. 정답 문자열에서 띄어쓰기를 잘못한 것은 오답이다. 

// 예를 들어서, Nile river가 정답일 때 nileRiver, nileRiver는 정답이지만 N ileRiver, N ilr River는 오답이야. 

// 처음에는 KMP 알고리즘을 생각했는데 띄어쓰기의 생략을 찾아낼 수 있지만 띄어쓰기 오류는 찾아내기 힘들것 같아서 투포인터를 통해 
// 하나씩 비교하는 방법을 채택하였습니다. 