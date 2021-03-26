class Solution {
    public int climbStairs(int n) {
        if (n <= 3)
            return n;
        int f1 = 2, f2 = 3, f3 = 4;
        for (int i = 4; i <= n; i++) {
            f3 = f1 + f2;
            f1 = f2;
            f2 = f3;
        }
        return f3;
    }
}