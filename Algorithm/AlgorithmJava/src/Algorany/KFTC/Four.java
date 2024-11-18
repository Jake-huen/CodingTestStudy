package Algorany.KFTC;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Four {
    static String s; // 현재 처리 중인 문자열
    static long l; // 시작 인덱스 (1-based)
    static long r; // 종료 인덱스 (1-based)

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 예시 배열
        String[] examples = {
            "[ABC]", // 예시 1
            "[XYZ]", // 예시 2
            "[AB[CD]]", // 예시 3
            "[A[B[C[D]]]]", // 예시 4
            "[[[[[[[[[[[[[[[[[ABC]]]]]]]]]]]]]]]]]]]" // 예시 5 (길이가 긴 문자열)
        };

        // 각 예시에 대한 l과 r 값
        long[] lValues = {3, 2, 4, 5, 1234}; 
        long[] rValues = {5, 3, 5, 7, 1235}; 

        // 각 예시를 처리
        for (int i = 0; i < examples.length; i++) {
            s = examples[i]; // 현재 문자열
            l = lValues[i]; // 현재 l 값
            r = rValues[i]; // 현재 r 값
            String result = extractSubstring(s, l, r); // 부분 문자열 추출
            System.out.println("Example: " + s + " | Result: " + result); // 결과 출력
        }
    }

    // 주어진 문자열 s에서 l과 r에 해당하는 부분 문자열을 추출하는 메서드
    public static String extractSubstring(String s, long l, long r) {
        StringBuilder result = new StringBuilder(); // 결과를 저장할 StringBuilder
        extractSubstring(s, 0, l - 1, r - 1, result); // 0-based 인덱스에 맞춰 호출
        return result.toString(); // 결과 반환
    }

    // 문자열 s에서 현재 길이 currentLength를 기준으로 l과 r 범위에 해당하는 부분을 추출
    private static void extractSubstring(String s, long currentLength, long l, long r, StringBuilder result) {
        int index = 0; // 문자열의 현재 인덱스
        while (index < s.length()) {
            char c = s.charAt(index); // 현재 문자

            if (c == '[') { // 여는 괄호를 만났을 때
                int closeIndex = findClosingBracket(s, index); // 닫는 괄호의 인덱스를 찾음
                String content = s.substring(index + 1, closeIndex); // 괄호 안의 내용을 추출
                long contentLength = calculateLength(content); // 괄호 안의 내용의 길이를 계산

                // 문자열을 두 번 반복하는 구조이므로 총 길이가 두 배가 된다
                long repeatedLength = 2 * contentLength;

                // 현재 길이에 반복된 길이를 더했을 때 l보다 큰 경우
                if (currentLength + repeatedLength > l) {
                    // 범위 내에 속하면 필요한 부분만 추가
                    extractSubstring(content, currentLength, l, r, result); // 첫 번째 반복
                    if (currentLength + contentLength <= r) {
                        extractSubstring(content, currentLength + contentLength, l, r, result); // 두 번째 반복
                    }
                }
                currentLength += repeatedLength; // 현재 길이를 업데이트
                index = closeIndex + 1; // 다음 문자로 이동
            } else { // 여는 괄호가 아닐 경우
                // 현재 길이가 l과 r 범위에 속하면 결과에 추가
                if (currentLength >= l && currentLength <= r) {
                    result.append(c);
                }
                currentLength++; // 현재 길이를 증가
                index++; // 다음 문자로 이동
            }
            // 현재 길이가 r을 초과하면 반복 종료
            if (currentLength > r) break;
        }
    }

    // 주어진 문자열의 길이를 계산하는 메서드
    private static long calculateLength(String s) {
        long length = 0; // 길이 초기화
        int index = 0; // 현재 인덱스
        while (index < s.length()) {
            if (s.charAt(index) == '[') { // 여는 괄호를 만났을 때
                int closeIndex = findClosingBracket(s, index); // 닫는 괄호의 인덱스를 찾음
                String content = s.substring(index + 1, closeIndex); // 괄호 안의 내용을 추출
                length += 2 * calculateLength(content); // 내부 내용의 길이를 두 배로 계산하여 추가
                index = closeIndex + 1; // 다음 문자로 이동
            } else { // 여는 괄호가 아닐 경우
                length++; // 단일 문자 길이 계산
                index++; // 다음 문자로 이동
            }
        }
        return length; // 최종 길이 반환
    }

    // 여는 괄호에 대한 닫는 괄호의 인덱스를 찾는 메서드
    private static int findClosingBracket(String s, int openIndex) {
        int balance = 1; // 여는 괄호의 개수를 세기 위한 변수
        int index = openIndex + 1; // 여는 괄호 다음 인덱스부터 시작
        while (balance > 0 && index < s.length()) {
            if (s.charAt(index) == '[') balance++; // 여는 괄호를 만나면 개수 증가
            else if (s.charAt(index) == ']') balance--; // 닫는 괄호를 만나면 개수 감소
            index++; // 다음 문자로 이동
        }
        return index - 1; // 닫는 괄호의 인덱스 반환
    }
}
// 제가 푼 방식은 전체 문자열을 찾아냈습니다. [] 로 구성된 전체 문자열을 구한 뒤, 해당 문자열에서 l과 r을 통해서 substring하였습니다. 
// 그러나 이 방식은 문자열이 아주 길 때는 비효율적입니다. 따라서 전체 문자열을 찾지 않고 l과 r에 해당하는 부분만 추출해서 가져와야 합니다. 
// 그를 위해서 문자열의 길이를 이용합니다. 

// 먼저 해당 문자열에서 [ 를 만날 때 닫는 ] 가 어디에 나오는지 찾습니다. 
// 그리고 [] 내부의 문자열 길이를 구해서 해당 문자열의 범위가 l과 r 사이에 있는지 찾아야합니다. 


// 이 코드는 주어진 문자열에서 l과 r에 해당하는 부분 문자열을 효율적으로 추출합니다. 
// 중첩된 구조를 처리하기 위해 재귀적으로 호출하며, 각 괄호의 내용을 두 번 반복하여 길이를 계산합니다. 
// 전체 문자열을 생성하지 않고 필요한 부분만 추출하여 메모리 사용을 최적화합니다.