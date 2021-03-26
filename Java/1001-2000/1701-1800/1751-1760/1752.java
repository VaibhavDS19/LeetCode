class Solution {
    public boolean check(int[] nums) {
        int n = nums.length, min = nums[0], i = 0;
        while (i < n - 1 && nums[i] <= nums[i + 1]) {
            i++;
        }
        i++;
        while (i < n - 1 && nums[i] <= nums[i + 1] && nums[i] <= min && nums[i + 1] <= min) {
            i++;
        }
        if (i == n - 1) {
            return nums[i] <= min;
        }
        return i > n - 1;
    }
}