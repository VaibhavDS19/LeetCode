class Solution {
    public int strStr(String haystack, String needle) {
        int i = 0, n = haystack.length() - needle.length();
        for (; i <= n; i++) {
            if (haystack.startsWith(needle, i))
                return i;
        }
        return -1;
    }
}