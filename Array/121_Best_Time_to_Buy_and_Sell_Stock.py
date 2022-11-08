from typing import List

# 短線波段一次 all in 交易
# 不能賣空 (short), 當日沖銷 (day trading)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # using Kadane's Algorithm
        # fast = buy 
        # slow = sell
        # diff = fast - slow , cross_day_trading = buy (today) - sell (next-day)
        cross_day_trading_profit, max_profit, buy = 0, 0, prices.pop(0)
        while prices:
            sell, buy = buy, prices.pop(0)
            cross_day_trading_profit = max(0, cross_day_trading_profit + buy - sell)
            max_profit = max(max_profit, cross_day_trading_profit)
        return max_profit
            

# prices = [2, 4, 1]
# prices = [7,6,4,3,1]
prices = [7, 1, 5, 3, 6, 4]
ans = Solution().maxProfit(prices)
print(ans)



def Kadane1(A):
    max_local, max_globe = 0,0
    for a in A:
        max_local = max(0, max_local + a)
        max_globe = max(max_local , max_globe)
    return max_globe

def Kadane2(A):
    max_local = max_globe = A.pop(0)
    for a in A:
        max_local = max(a, max_local + a)
        if max_local > max_globe:
            max_globe = max_local
    return max_globe

test_array = [-6, 4, -2, 3, -2]
print(f'Kadane alg 1 : {Kadane1(test_array)}') # 5
print(f'Kadane alg 2 : {Kadane2(test_array)}') # 5