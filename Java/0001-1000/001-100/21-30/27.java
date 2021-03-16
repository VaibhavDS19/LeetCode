class Solution {
    public int removeElement(int[] nums, int val) {
        int swap, now = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[now] = nums[i];
                now += 1;
            }
        }
        return now;
    }
}