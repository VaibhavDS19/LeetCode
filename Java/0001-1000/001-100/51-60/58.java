class Solution {
    public int lengthOfLastWord(String s) {
        char[] c = s.toCharArray();
        int n = s.length() - 1, len = 0;
        while (n >= 0 && c[n] == ' ')
            n--;
        while (n >= 0 && c[n] != ' ') {
            len++;
            n--;
        }
        return len;
    }
}