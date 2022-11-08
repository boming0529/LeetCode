# -*- coding: utf-8 -*-
from typing import List
from collections import deque

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_local, max_globe, buy = 0 , 0, prices.pop(0)
        pre_day_profit = 0
        profit = deque([0, 0])
        for price in prices:
            sell, buy = buy, price
            diff = buy - sell
            pre_day_profit = max_local
            max_local = max(0, max_local + diff)

            if max_local - pre_day_profit < 0: # 趨勢反轉
                print(profit, pre_day_profit, )
                if pre_day_profit > 0 and pre_day_profit == max(pre_day_profit, profit[1]):
                    print('inside %d' % (pre_day_profit) )
                    profit.appendleft(pre_day_profit) 
            
            max_globe = max(max_globe, max_local)
            print(max_local, profit[0] + profit[1], max_globe)
        if max_local > 0 and max_local == max(max_local, profit[1]):
            print(profit, max_local)
            profit.appendleft(pre_day_profit-max_local) 

        return max(max_globe, profit[0] + profit[1])


# prices = [3,3,5,0,0,3,1,4] # 6
# prices = [2, 4, 1] # 2
# prices = [1,2,3,4,5] # 4
# prices = [7,6,4,3,1] # 0
# prices = [1] # 0
prices = [7, 1, 5, 3, 6, 4] # 7
ans = Solution().maxProfit(prices)
print(ans)