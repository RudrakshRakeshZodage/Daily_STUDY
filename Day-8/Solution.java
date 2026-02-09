class Solution {

    public int maxProfit(int[] p) {
        int mn = Integer.MAX_VALUE;
        int mx = 0;

        for (int x : p)     
            if (x < mn) mn = x;
            else mx = Math.max(mx, x - mn);
        
        return mx;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] prices = {7, 1, 5, 3, 6, 4};
        System.out.println(s.maxProfit(prices)); // Output: 5
    }
}
