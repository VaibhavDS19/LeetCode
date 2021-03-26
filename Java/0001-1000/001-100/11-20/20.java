class Solution {
    public boolean isValid(String s) {
        char[] c = new char[s.length()];
        int i = -1;
        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '{' || ch == '[') {
                c[++i] = ch;
            } else if (ch == ')') {
                if (i < 0 || c[i] != '(')
                    return false;
                i--;
            } else if (ch == '}') {
                if (i < 0 || c[i] != '{')
                    return false;
                i--;
            } else {
                if (i < 0 || c[i] != '[')
                    return false;
                i--;
            }
        }
        return i == -1;
    }
}