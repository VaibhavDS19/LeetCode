class Solution {
    public int searchInsert(int[] nums, int target) {
        int mid, begin = 0, end = nums.length;
        while (true) {
            if (target < nums[0])
                return 0;
            if (target > nums[nums.length - 1])
                return nums.length;
            mid = (begin + end) / 2;
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] > target) {
                if (mid > 0 && nums[mid - 1] < target)
                    return mid;
                end = mid - 1;
            } else {
                if (mid < nums.length - 1 && nums[mid + 1] > target)
                    return mid + 1;
                begin = mid + 1;
            }
        }
    }
}