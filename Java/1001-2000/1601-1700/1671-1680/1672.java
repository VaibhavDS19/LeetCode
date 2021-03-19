class Solution {
    public int maximumWealth(int[][] accounts) {
        int max = 0, sum = 0;
        for (int[] j : accounts) {
            sum = 0;
            for (int i : j) {
                sum += i;
            }
            if (sum > max)
                max = sum;
        }
        return max;
    }
}