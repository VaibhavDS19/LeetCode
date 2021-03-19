class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List l1 = new ArrayList();
        int max = 0;
        for (int i : candies) {
            if (i > max)
                max = i;
        }
        for (int i : candies) {
            l1.add(i + extraCandies >= max);
        }
        return l1;
    }
}