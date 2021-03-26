class Solution {
    public int[] plusOne(int[] digits) {
        int c=1, n=digits.length, i;
        for(i=n-1;i>=0;i--) {
            digits[i] += c;
            c = digits[i]/10;
            digits[i] %= 10;
        }
        if(c==0) return digits;
        int[] digit = new int[n+1];
        digit[0] = 1;
        for(i=0;i<n;i++) {
            digit[i+1] = digits[i];
        }
        return digit;
    }
}