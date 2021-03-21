class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] count = new int[101];
        int[] countTo = new int[101];
        for (int num : nums) {
            count[num]++;
            countTo[num]++;
        }

        for (int i = 1; i < count.length; i++) {
            countTo[i] += countTo[i - 1];
        }

        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            res[i] = countTo[nums[i]] - count[nums[i]];
        }
        return res;
    }
}