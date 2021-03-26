class Solution {
    public int mySqrt(int x) {
        if (x == 0 || x == 1)
            return x;
        int n = 0, b = 1, e = x;
        while (b <= e) {
            int mid = b + (e - b) / 2;

            if (mid == x / mid)
                return mid;
            else if (mid < x / mid) {
                n = mid;
                b = mid + 1;
            } else
                e = mid - 1;
        }
        return n;
    }
}