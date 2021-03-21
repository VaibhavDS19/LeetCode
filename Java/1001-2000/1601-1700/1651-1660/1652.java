class Solution {
    public int[] decrypt(int[] code, int k) {
        int n = code.length, sum = 0, i = 1;
        int[] res = new int[n];
        if (k == 0) {
            return res;
        }
        if (k > 0) {
            for (i = 0; i < k; i++) {
                sum += code[i];
            }
            for (i = 0; i < n; i++) {
                sum -= code[i];
                sum += code[(i + k) % n];
                res[i] = sum;
            }
        } else {
            k *= -1;
            for (i = n - 1; i > n - 1 - k; i--) {
                sum += code[i];
            }
            for (i = 0; i < n; i++) {
                res[i] = sum;
                sum += code[i];
                sum -= code[(i - k + n) % n];
            }
        }
        return res;
    }
}