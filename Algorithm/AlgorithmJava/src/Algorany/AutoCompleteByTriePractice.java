package Algorany;

public class AutoCompleteByTriePractice {

    public int solution(String[] words) {
        int answer = 0;
        Trie trie = new Trie();
        for (int i = 0; i < words.length; i++) {
            trie.insert(words[i]);
        }
        for (int i = 0; i < words.length; i++) {
            answer += trie.query(words[i]);
        }
        return answer;
    }

    static class Trie {
        boolean isleafNode = true; // 리프노드 여부
        Trie[] subTrie = new Trie[26]; // 알파벳 26개 포함시키기

        void insert(String key) {
            int index = 0;
            Trie trie;
            if (this.subTrie[charToNumber(key.charAt(index))] == null) {
                trie = this.subTrie[charToNumber(key.charAt(index))] = new Trie();
                // 등록된적 있는 노드이기 때문에 노드를 하나 더 추가하면서 리프노드가 아니게 됨.
                trie.isleafNode = false;
            }
            index += 1;
        }

        int query(String key) {
            int sameCharCount = 1, index = 0;
            Trie trie = this.subTrie[charToNumber(key.charAt(index))];
            index++;
            while (index < key.length()) {
                int next = charToNumber(key.charAt(index));
                if (trie.isleafNode) {
                    break;
                }
                sameCharCount += 1;
                trie = trie.subTrie[next];
                index += 1;
            }
            return sameCharCount;
        }

        int charToNumber(char c) {
            return c - 'a';
        }
    }
}
