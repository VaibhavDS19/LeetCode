class Solution {
    public int numIdenticalPairs(int[] nums) {
        int[] mp = new int[101];
        int count = 0;
        for (int i : nums) {
            count += mp[i];
            mp[i]++;
        }
        return count;
    }
}