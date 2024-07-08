package Algorany;

import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class FileSearch {

    static int n;
    static ArrayList<ArrayList<String>> files = new ArrayList<>();
    // 숫자열이 알파벳보다 앞에, 알파벳은 대문자가 앞에
    // 문자열을 비교하는 중 숫자가 있을 경우, 그 다음에 오는 숫자를 최대한 많이 묶어 한 단위로 비교

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb;
        n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            files.add(new ArrayList<>());
        }
        for (int i = 0; i < n; i++) {
            String s = br.readLine();

            for (int j = 0; j < s.length(); j++) {
                sb = new StringBuilder();
                if ('0' <= s.charAt(j) && s.charAt(j) <= '9') { // 숫자일 경우
                    while (j < s.length() && '0' <= s.charAt(j) && s.charAt(j) <= '9') {
                        sb.append(s.charAt(j));
                        j += 1;
                    }
                    j -= 1; // 위에서 더해줬기 때문에 뺴줌
                } else { // 문자일 경우
                    sb.append(s.charAt(j));
                }
                files.get(i).add(sb.toString());
            }
        }

//        for (ArrayList<String> file : files) {
//            System.out.println("file = " + file);
//        }
        Collections.sort(files, new Comparator<ArrayList<String>>() {
            @Override
            public int compare(ArrayList<String> o1, ArrayList<String> o2) {
                int len1 = o1.size();
                int len2 = o2.size();
                int i = 0, j = 0;
                for (; i < len1 && j < len2; i++, j++) {
                    if (o1.get(i).equals(o2.get(j))) { // 2개의 경우가 같을 때
                        continue;
                    }

                    // 숫자인지 판단
                    boolean isNumO1 = isNum(o1.get(i));
                    boolean isNumO2 = isNum(o2.get(j));

                    // 둘 다 숫자인 경우
                    if (isNumO1 && isNumO2) {
                        BigInteger s1 = new BigInteger(o1.get(i));
                        BigInteger s2 = new BigInteger(o2.get(j));
                        int comparison = s1.compareTo(s2);
                        if (comparison == 0) {
                            // 숫자가 같다면 0의 갯수가 작은순
                            return o1.get(i).length() - o2.get(j).length();
                        } else {
                            return comparison;
                        }


                    } else if (!isNumO1 && !isNumO2) { // 둘다 문자인 경우
                        char c1 = o1.get(i).charAt(0);
                        char c2 = o2.get(j).charAt(0);

                        int n1 = c1 - 'a' >= 0 ? c1 - 'a' : c1 - 'A';
                        int n2 = c2 - 'a' >= 0 ? c2 - 'a' : c2 - 'A';

                        boolean isUpper1 = c1 - 'a' < 0;
                        boolean isUpper2 = c2 - 'a' < 0;

                        //둘다 대문자 or 둘다 소문자
                        if ((isUpper1 && isUpper2) || (!isUpper1 && !isUpper2)) {
                            return n1 - n2;
                        }
                        //c1 소문자, c2대문자
                        if (!isUpper1 && isUpper2) {
                            //c1,c2가 같은 문자
                            if (n1 == n2)
                                return 1;

                            //다른 문자일 경우
                            return n1 - n2;
                        }
                        //c1 대문자 , c2소문자
                        if (isUpper1 && !isUpper2) {
                            //c1,c2가 같은 문자일 경우
                            if (n1 == n2)
                                return -1;

                            //다른 문자일 경우
                            return n1 - n2;
                        }
                    } else if (!isNumO1 && isNumO2) {
                        // o1 문자, o2 숫자
                        return 1;
                    } else if (isNumO1 && !isNumO2) {
                        return -1;
                    }
                }

                if (len1 > i) { // o1 길이가 아직 남아있는 경우
                    return 1;
                }
                if (len2 > j) {
                    return -1;
                }
                return 0; // 아예 같음
            }
        });

        sb = new StringBuilder();
        for (ArrayList<String> file : files) {
            StringBuilder sb2 = new StringBuilder();
            for(String s : file){
                sb2.append(s);
            }
            sb.append(sb2);
            sb.append("\n");
        }
        System.out.println(sb.toString());

    }

    private static boolean isNum(String s) {
        if ('0' <= s.charAt(0) && '9' >= s.charAt(0)) {
            return true;
        } else {
            return false;
        }
    }


}
