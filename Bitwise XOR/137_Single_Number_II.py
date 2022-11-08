from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Using Python Set Diffance
        # return (3*sum(set(nums)) - sum(nums)) // 2

        # Usgin Python collections.Counter
        # for key, coun in Counter(nums).items():
        #     if coun == 1 : return key 

        # Using Two Pass Hash Table 
        # ht = {}
        # for num in nums:
        #     ht[num] = ht.get(num, 0) + 1
        # for k,v in ht.items():
        #     if v == 1: return k

        # Improvemet Two Pass Hash Table = One Pass Hash Table
        # ht = {}
        # while nums:
        #     num = nums.pop() 
        #     ht[num] = ht.get(num, 0) + 1
        #     if ht[num] == 3:
        #         ht.pop(num)
        # return next(iter(ht))

        # Using Xor-ing
        # https://lenchen.medium.com/leetcode-137-single-number-ii-31af98b0f462
        seen_once = seen_twice = 0
        for num in nums:
            seen_once = ~ seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)
        return seen_once

# OJ:
arr = [-2,-2,-2,6]
ans = Solution().singleNumber(arr)
assert ans == 6, 'error'

arr = [-3,-3,3,3,3,-3,4]
ans = Solution().singleNumber(arr)
assert ans == 4, 'error'

arr = [3]
ans = Solution().singleNumber(arr)
assert ans == 3, 'error'

arr = [0,1,0,1,0,1,99]
ans = Solution().singleNumber(arr)
assert ans == 99, 'error'