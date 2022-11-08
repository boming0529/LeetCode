from typing import List

# 短線波段多次交易(麻雀策略), 可當日沖銷 (day trading)
# 不能賣空 (short)

# 解答提供了三種方式
# Brute Force : 暴力解
# Peak Valley Approach (Greedy): 峰谷法
# Simple One Pass (Greedy): 找正差值和 
# Suggested Read : 
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/803206/PythonJSJavaGoC%2B%2B-O(n)-by-DP-Greedy-%2B-Visualization

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 註解備註 : 找正差值和(跟著趨勢做多, 買漲不買跌) > 連續最大正差值得和(因為連續天因下股市下跌沒有賺到波段利益)
        # kadane's Algorithm --> 目前的解法比較像 botoom-up DP + iteration
        # long_profit = 0
        short_profit, buy = 0, prices[0]
        pre_day_profit = 0
        other_strategy = 0
        for quote in prices:
            sell, buy = buy, quote
            profit = buy - sell
            pre_day_profit = short_profit
            short_profit = max(0, short_profit + profit)
            if pre_day_profit < short_profit:
                other_strategy += short_profit - pre_day_profit
            # long_profit = max(long_profit, short_profit)
        return other_strategy #max(long_profit, other_strategy)

    def maxProfit2(self, prices: List[int]) -> int:
        # Simple One Pass : 可以化簡上面的處理方式
        # short_profit = 0
        buy = prices.pop(0)
        # pre_day_profit = 0
        other_strategy = 0
        for quote in prices:
            sell, buy = buy, quote
            profit = buy - sell
            # pre_day_profit = short_profit
            # short_profit = max(0, short_profit + profit)
            # if pre_day_profit < short_profit:
            #     other_strategy += short_profit - pre_day_profit
            if profit > 0:
                other_strategy += profit
            
        return other_strategy

    
# prices = [2, 4, 1]
# prices = [7,6,4,3,1]
# prices = [1]
prices = [7, 1, 5, 3, 6, 4]
ans = Solution().maxProfit2(prices)
print(ans)