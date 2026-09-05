class Solution {
    private int[][] memo;

    public int lengthOfLIS(int[] nums) {
        memo = new int [nums.length][nums.length + 1];
        return recurse(nums, 0, -1);
    }

    public int recurse(int[] nums, int i, int j) {
        if (i >= nums.length) return 0;
        if (memo[i][j + 1] != 0) return memo[i][j + 1];
        int len = recurse(nums, i + 1, j);
        if (j == -1 || nums[i] > nums[j]) {
            len = Math.max(len, 1 + recurse(nums, i + 1, i));
        }

        memo[i][j + 1] = len;
        return len;
    }
}
