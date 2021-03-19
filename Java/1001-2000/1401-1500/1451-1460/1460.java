class Solution {
    public boolean canBeEqual(int[] target, int[] arr) {
        if (target.length != arr.length)
            return false;
        int a[] = new int[1001];
        int n = target.length;
        for (int i = 0; i < n; i++) {
            a[target[i]]++;
            a[arr[i]]--;
        }
        for (int i = 1; i < 1001; i++) {
            if (a[i] != 0) {
                return false;
            }
        }
        return true;
    }
}