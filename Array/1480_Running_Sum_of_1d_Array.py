from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # using in-place
        # Time Complexity : O(n)
        # Space Complexity : O(1) 
        for idnx in range(1, len(nums)):
            nums[idnx] += nums[idnx-1]
        return nums[:]

# OJ
arg = [1,1,1,1,1]
ans = Solution().runningSum(arg)
print(ans)

arg = [3,1,2,10,1]
ans = Solution().runningSum(arg)
print(ans)

# boundary case 
arg = [0]
ans = Solution().runningSum(arg)
print(ans)

arg = [1000000, -1000000]
ans = Solution().runningSum(arg)
print(ans)