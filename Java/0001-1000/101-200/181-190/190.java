public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int s = 0;
        for (int i = 0; i < 32; i++) {
            s = (s << 1) + (n >> i & 1);
        }
        return s;
    }
}