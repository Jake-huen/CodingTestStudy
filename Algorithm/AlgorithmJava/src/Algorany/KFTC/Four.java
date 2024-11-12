package Algorany.KFTC;

public class Four {
    public static void main(String[] args) {
        String s = "[na][ba[ca]]";
        long l = 3;
        long r = 14;
        System.out.println(extractSubstring(s, l, r));
    }

    public static String extractSubstring(String s, long l, long r) {
        StringBuilder result = new StringBuilder();
        decompress(s, 0, l, r, result, 0);
        return result.toString();
    }

    private static long decompress(String s, int index, long l, long r, StringBuilder result, long currentLength) {
        while (index < s.length()) {
            char c = s.charAt(index);

            if (c == '[') {
                int closeIndex = findClosingBracket(s, index);
                String content = s.substring(index + 1, closeIndex);
                long contentLength = getContentLength(content);

                // Check if the content is within the range we care about
                if (currentLength + contentLength >= l) {
                    // Recursively process only the needed part
                    decompress(content, 0, l, r, result, currentLength);
                }
                currentLength += contentLength;
                index = closeIndex + 1;
            } else {
                if (currentLength >= l && currentLength <= r) {
                    result.append(c);
                }
                currentLength++;
                index++;
            }

            if (currentLength > r) break;
        }
        return currentLength;
    }

    private static int findClosingBracket(String s, int openIndex) {
        int balance = 1;
        int index = openIndex + 1;
        while (balance > 0 && index < s.length()) {
            if (s.charAt(index) == '[') balance++;
            else if (s.charAt(index) == ']') balance--;
            index++;
        }
        return index - 1;
    }

    private static long getContentLength(String content) {
        // Simulate decompression to find the total length of the decompressed content
        long length = 0;
        for (int i = 0; i < content.length(); i++) {
            if (content.charAt(i) == '[') {
                int closeIndex = findClosingBracket(content, i);
                length += getContentLength(content.substring(i + 1, closeIndex));
                i = closeIndex;
            } else {
                length++;
            }
        }
        return length;
    }
}

