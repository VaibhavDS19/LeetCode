class Solution {
    public int xorOperation(int n, int start) {
        int nx = 0;
        for (int i = 0; i < n; i++) {
            nx ^= start;
            start += 2;
        }
        return nx;
    }
}