class Solution {
    public double average(int[] salary) {
        int sum = 0, max = 0, min = 10000000;
        for (int i : salary) {
            if (i > max) {
                max = i;
            }
            if (i < min) {
                min = i;
            }
            sum += i;
        }
        return (double) (sum - max - min) / (salary.length - 2.0);
    }
}