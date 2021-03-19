class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int count = 0, rvk = 0;
        if (ruleKey.equals("color"))
            rvk = 1;
        else if (ruleKey.equals("name"))
            rvk = 2;
        for (List<String> l : items) {
            if ((l.get(rvk)).equals(ruleValue)) {
                count++;
            }
        }
        return count;
    }
}