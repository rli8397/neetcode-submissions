class Solution {
    public boolean canPartition(int[] nums) {
        int total = 0;
        for (int i = 0; i < nums.length; i++){
            total += nums[i];
        }

        if (total % 2 == 0) {
            boolean[] ith_total = new boolean[total / 2 + 1];
            ith_total[0] = true;
            for (int i = 0; i < nums.length; i++) {
                for (int j = ith_total.length; j >= 0; j--) {
                    if (j + nums[i] < ith_total.length && ith_total[j]) {
                        ith_total[j + nums[i]] = true;
                    }
                }
            }
            return ith_total[ith_total.length - 1];
        }
        return false;
    }
}
