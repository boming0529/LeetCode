from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int, idx: int =0) -> int:
        # Using python overload + Recursion + Binary Search
        # Time Complexity : O(log(n))
        # Space Complexity : O(n)
        n = len(nums)
        if n == 1: return idx + (0 if nums[0] >= target else 1)
        if nums[0] > target: return idx
        if nums[-1] < target: return n

        mid = n // 2
        if nums[mid] == target:
            return idx + mid
        elif target < nums[mid]:
            return self.searchInsert(nums[:mid],target, idx)
        else:
            return self.searchInsert(nums[mid:],target,idx + mid)
        

        
# Online Judge Case
arg = [-1,0,1,3,5,6]
ans = Solution().searchInsert(arg, 5)
assert ans == 4, 'error'

arg = [1,3,5,6]
ans = Solution().searchInsert(arg, 2)
assert ans == 1, 'error'



arg = [-1,0,1,3,5,6]
ans = Solution().searchInsert(arg, 7)
assert ans == 6, 'error'

# Boundary Case
arg = [1]
ans = Solution().searchInsert(arg, 5)
assert ans == 1, 'error'

arg = [1]
ans = Solution().searchInsert(arg, -5)
assert ans == 0, 'error'

# lose test
arg = [1]
ans = Solution().searchInsert(arg, 1)
assert ans == 0, 'error'

arg = [1,3,5]
ans = Solution().searchInsert(arg, 4)
assert ans == 2, 'error'

