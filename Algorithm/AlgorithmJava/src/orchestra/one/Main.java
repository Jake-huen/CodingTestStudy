package orchestra.one;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Main T = new Main();
        System.out.println(T.solution(1));
    }
    public static boolean isProductEqual(int num, int n) {
        String numStr = Integer.toString(num);

        int frontProduct = 1;
        int backProduct = 1;

        for (int i = 0; i < n; i++) {
            frontProduct *= Character.getNumericValue(numStr.charAt(i));
            backProduct *= Character.getNumericValue(numStr.charAt(i + n));
        }

        return frontProduct == backProduct;
    }

    public int solution(int num) {
        int answer = 0;
        char[] numstr = Integer.toString(num).toCharArray();

        if(numstr.length%2==0){ // 길이가 짝수인 경우
            int start = (int) Math.pow(10, numstr.length/2 - 1);
            int end = (int) Math.pow(10, numstr.length/2);

            for (int i = start; i < end; i++) {
                if (isProductEqual(i, numstr.length/2)) {
                    return i;
                }
            }
        } else{
            answer = (int) Math.pow(10,numstr.length)+1;
        }

        return answer;
    }
}
