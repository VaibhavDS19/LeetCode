class Solution {
    public int fib(int n) {
        if (n < 2)
            return n;
        int f1 = 0, f2 = 1, f3 = 0, i = 2;
        while (i <= n) {
            f3 = f1 + f2;
            f1 = f2;
            f2 = f3;
            n--;
        }
        return f3;
    }
}