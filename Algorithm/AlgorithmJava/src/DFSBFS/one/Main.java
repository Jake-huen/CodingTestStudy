package DFSBFS.one;

class Node {
    int data;
    Node lt, rt;

    public Node(int val) {
        this.data = val;
        lt = rt = null;
    }
}

public class Main {

    public static void main(String[] args) {
        Main T = new Main();
        T.DFS(11);
    }

    private void DFS(int n) {
        if (n == 0) return;
        DFS(n / 2);
        System.out.print(n % 2);
    }
}
