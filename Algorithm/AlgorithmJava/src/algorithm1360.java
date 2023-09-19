import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class algorithm1360 {
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N;
    static ArrayList<Node> list;

    static class Node {
        String str;
        int time;
        public Node(String str, int time) {
            this.str = str;
            this.time = time;
        }
    }

    static void input() throws IOException {
        st = new StringTokenizer(in.readLine());
        N = Integer.valueOf(st.nextToken());
        list = new ArrayList<>();

    }

    public static void main(String[] args) {
        // input();
        System.out.print(list.get(N).str);
    }
}