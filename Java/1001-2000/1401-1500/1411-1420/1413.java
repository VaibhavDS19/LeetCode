class Solution {
    public int minStartValue(int[] nums) {
        int min = 999999, sum = 0;
        for (int i : nums) {
            sum += i;
            if (sum < min) {
                min = sum;
            }
        }
        if (min < 1) {
            return min * -1 + 1;
        }
        return 1;
    }
}