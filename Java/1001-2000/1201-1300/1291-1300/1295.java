class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for (int i : nums) {
            if (isEvenDigit(i)) {
                count++;
            }
        }
        return count;
    }

    public boolean isEvenDigit(int n) {
        if ((n >= 10 && n < 100) || (n >= 1000 && n < 10000) || (n == 100000))
            return true;
        return false;
    }
}