package Algorany;

import java.util.*;

public class ListPhoneNumber {

    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        for (int i = 0; i < phone_book.length - 1; i++) {

            if (phone_book[i + 1].startsWith(phone_book[i])) {
                return false;
            }
        }
        // System.out.println(answer);
        return true;
    }

    public static void main(String[] args) {
        ListPhoneNumber listPhoneNumber = new ListPhoneNumber();
        listPhoneNumber.solution(new String[]{"119", "97674223", "1195524421"});
    }
}
