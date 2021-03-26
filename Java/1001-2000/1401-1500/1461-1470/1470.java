class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] snum = new int[2*n];
        int j=0;
        for(int i=0;i<n;i++) {
            snum[j++] = nums[i];
            snum[j++] = nums[i+n];
        }
        return snum;
    }
}