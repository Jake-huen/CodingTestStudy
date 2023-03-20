import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int[] dx = { 0, 1, 0, -1 };
    static int[] dy = { 1, 0, -1, 0 };

    static int[] map;
    static boolean[] check;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String s = bf.readLine();
        StringTokenizer stk = new StringTokenizer(s, " ");
        int h = Integer.parseInt(stk.nextToken());
        int w = Integer.parseInt(stk.nextToken());
        map = new int[h * w];

        for (int i = 0; i < h; i++) {
            s = bf.readLine();
            stk = new StringTokenizer(s, " ");
            for (int j = 0; j < w; j++) {
                map[i * w + j] = Integer.parseInt(stk.nextToken());
            }
        }
        check = new boolean[h * w];

        Queue<Integer> quex = new LinkedList<>();
        Queue<Integer> quey = new LinkedList<>();

        int ans1 = 0;
        int ans2 = 0;
        while (true) {
            int ans = 0;
            quex.clear();
            quey.clear();
            quex.add(0);
            quey.add(0);
            for (int i = 0; i < h * w; i++) {
                check[i] = false;
            }

            while (!quex.isEmpty()) {
                int nowx = quex.poll();
                int nowy = quey.poll();
                int now = nowx * w + nowy;

                if (!check[now]) {
                    check[now] = true;
                    if (map[now] == 1) {
                        map[now] = 2;
                        ans++;
                    } else if (map[now] == 0) {
                        for (int t = 0; t < 4; t++) {
                            int nowdx = nowx + dx[t];
                            int nowdy = nowy + dy[t];
                            int next = nowdx * w + nowdy;
                            if (0 <= nowdx && nowdx < h && 0 <= nowdy && nowdy < w && !check[next]) {
                                quex.add(nowdx);
                                quey.add(nowdy);
                            }
                        }
                    }
                }
            }
            for (int i = 0; i < h * w; i++) {
                if (map[i] == 2) {
                    map[i] = 0;
                }
            }

            if (ans == 0) {
                System.out.println(ans1 + " " + ans2);
                return;
            }
            ans2 = ans;
            ans1++;
        }
    }

}