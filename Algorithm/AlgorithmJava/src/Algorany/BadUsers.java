package Algorany;

import java.util.*;

public class BadUsers {

    String[] userIds;
    String[] bannedIds;
    HashSet<HashSet<String>> result = new HashSet<>();

    public int solution(String[] user_id, String[] banned_id) {
        userIds = user_id;
        bannedIds = banned_id;

        dfs(new HashSet<String>(), 0);

        return result.size();
    }

    public void dfs(HashSet<String> hashSet, int depth) {
        if (depth == bannedIds.length) {
            result.add(hashSet);
            return;
        }

        for (int i = 0; i < userIds.length; i++) {
            if(hashSet.contains(userIds[i])){
                continue;
            }
            if(check(userIds[i], bannedIds[depth])){
                hashSet.add(userIds[i]);
                dfs(new HashSet<>(hashSet), depth+1);
                hashSet.remove(userIds[i]);
            }
        }
    }


    public boolean check(String a, String b) {
        if (a.length() != b.length()) {
            return false;
        }
        int n = a.length();
        for (int i = 0; i < n; i++) {
            if (a.charAt(i) == b.charAt(i) || b.charAt(i) == '*') {
                continue;
            } else {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        BadUsers badUsers = new BadUsers();
        System.out.println(badUsers.solution(new String[]{"frodo", "fradi", "crodo", "abc123", "frodoc"}, new String[]{"*rodo", "*rodo", "******"}));
    }
}
