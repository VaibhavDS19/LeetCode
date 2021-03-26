class Solution {
    public int reverse(int x) {
        int i=x, j=0, k=0;
        if(i<0 && i==-2147483648) return 0;
        if(i<0) i*=-1;
        while(i>0) {
            k++;
            j = j*10 + i%10;
            i/=10;
            if(k==9) {
                if(j>214748364 && i>0) return 0;
                if(i==214748364 && i<=7) continue;
            }
        }
        if(x<0) j*=-1;
        return j;
    }
}