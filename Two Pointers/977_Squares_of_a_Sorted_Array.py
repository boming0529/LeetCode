from typing import List
from collections import deque

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # using Two Pointer Approach
        # TC : O(n), PS: O(n)
        prefix, last = 0, -1
        ans = deque([])
        while (prefix + 1) + (~last+1) <= len(nums) + 1:
            if nums[prefix] * nums[prefix] >= nums[last] * nums[last]:
                ans.appendleft(nums[prefix] * nums[prefix])
                prefix += 1
            else:
                ans.appendleft(nums[last] * nums[last])
                last -= 1
        return ans

nums = [-4,-1,0,3,10]
ans = Solution().sortedSquares(nums) #[0,1,9,16,100]
print(ans)

nums = [-7,-3,2,3,11]
ans = Solution().sortedSquares(nums) #[4,9,9,49,121]
print(ans)

nums = [-7,-3]
ans = Solution().sortedSquares(nums) #[9,49]
print(ans)

nums = [0]
ans = Solution().sortedSquares(nums) #[0]
print(ans)

nums = [-10000,-1,0,3,10000]
ans = Solution().sortedSquares(nums) #[0,1,9,100000000,100000000]
print(ans)


nums = [-10000,-9999,-7,-5,0,0,10000]
ans = Solution().sortedSquares(nums) #[0,0,25,49,99980001,100000000,100000000]
print(ans)