from typing import List
from functools import reduce
import operator

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # xor 
        # 利用 xor 性質, 自反, 交換率
        # https://leetcode.com/problems/missing-number/solutions/1585333/python-the-best-explanation-bitwise-and-sum/?languageTags=python&topicTags=bit-manipulation
        # ex:
        # [3,0,1] => (3 ^ 0 ^ 1)
        # [0,1,2,3] => 0 ^ 1 ^ 2 ^ 3
        # [0,1,2,3] ^ [3,0,1]
        # 0 ^ 1 ^ 2 ^ 3 ^ (3 ^ 0 ^ 1)
        # 0 ^ 0 ^ 1 ^ 1 ^ 2 ^ 3 ^ 3
        # 0 ^ 0 ^ 2 ^ 0
        # 2
        ans: int = len(nums)        
        for i in range(len(nums)):
            ans ^= i ^ nums[i]
        return ans


        # Xor-ing
        # @@ 
        n = len(nums)
        return reduce(operator.xor, nums) ^ [n, 1, n+1, 0][n % 4]

        # Sum
        n = len(nums)
        sum = 0
        for num in nums:
            sum += num
        return (0 + n) * (n+1) // 2 - sum

        # using Python Set difference
        return (set(range(len(nums)+1)) - set(nums)).pop()


import random

# OJ Case 
arr = [3,0,1]
ans = Solution().missingNumber(arr)
should_Be = 2
assert ans == should_Be, f'error m: {should_Be}, ans: {ans}'

# general test case.
time = 0
while time < 10:
    n = random.randint(1,10**4)
    arr = [ele for ele in range(n)]
    m = random.randint(0,n-1)
    arr.pop(m)
    random.shuffle(arr)

    ans = Solution().missingNumber(arr)
    assert ans == m, f'error m: {m}, ans: {ans}'
    time += 1
    print(time)

# boundary case
arr = [0,1,2,3]
ans = Solution().missingNumber(arr)
assert ans == 4, 'error'

arr = [1,2,3,4]
ans = Solution().missingNumber(arr)
assert ans == 0, 'error'

arr = [0]
ans = Solution().missingNumber(arr)
assert ans == 1, 'error'

arr = [1]
ans = Solution().missingNumber(arr)
assert ans == 0, 'error'