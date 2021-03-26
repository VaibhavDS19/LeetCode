class Solution {
    public int[] replaceElements(int[] arr) {
        int n = arr.length, i, max = arr[n - 1];
        int[] nums = new int[n];
        nums[n - 1] = -1;
        for (i = n - 2; i >= 0; i--) {
            nums[i] = max;
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return nums;
    }
}