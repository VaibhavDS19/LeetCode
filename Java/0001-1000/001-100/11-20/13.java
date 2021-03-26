class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int sum = 0, n = s.length();
        char[] rmn = s.toCharArray();
        for (int i = n - 1; i >= 0; i--) {
            switch (rmn[i]) {
            case 'I':
                sum += 1;
                break;
            case 'V':
                if (i > 0 && rmn[i - 1] == 'I') {
                    i--;
                    sum += 4;
                } else
                    sum += 5;
                break;
            case 'X':
                if (i > 0 && rmn[i - 1] == 'I') {
                    i--;
                    sum += 9;
                } else
                    sum += 10;
                break;
            case 'L':
                if (i > 0 && rmn[i - 1] == 'X') {
                    i--;
                    sum += 40;
                } else
                    sum += 50;
                break;
            case 'C':
                if (i > 0 && rmn[i - 1] == 'X') {
                    i--;
                    sum += 90;
                } else
                    sum += 100;
                break;
            case 'D':
                if (i > 0 && rmn[i - 1] == 'C') {
                    i--;
                    sum += 400;
                } else
                    sum += 500;
                break;
            case 'M':
                if (i > 0 && rmn[i - 1] == 'C') {
                    i--;
                    sum += 900;
                } else
                    sum += 1000;
                break;
            }
        }
        return sum;
    }
}