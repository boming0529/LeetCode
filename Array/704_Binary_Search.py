from typing import List

class Solution:
    def search(self, nums: List[int], target: int, L : int=0) -> int:
        # Using Top-Down DP
        # Time Complexity : O(logN)
        if target > nums[-1] or target < nums[0]: return -1
        n: int = len(nums)
        mid: int = n // 2
        if nums[mid] == target:
            return L + mid
        elif nums[mid] < target: 
            nums = nums[mid:]
            L += mid
        else:
            nums = nums[:mid]
        return self.search(nums, target, L)

# OJ Case
args = [-1,0,3,5,9,12]
target = 9
ans = Solution().search(args, target)
assert ans == 4 ,"error"

args = [-1,0,3,5,9,12]
target = 0
ans = Solution().search(args, target)
assert ans == 1 ,"error"

# edge case , boundary case
args = [-1,0,3,5,9,12]
target = -1
ans = Solution().search(args, target)
assert ans == 0, "error"

args = [-1,0,3,5,9,12]
target = 12
ans = Solution().search(args, target)
assert ans == 5, "error"

args = [3]
target = 3
ans = Solution().search(args, target)
assert ans == 0, "error"

# inside not find case
args = [-1,0,3,5,9,12]
target = -12
ans = Solution().search(args, target)
assert ans == -1, "error"

args = [-1,0,3,5,9,12]
target = -22
ans = Solution().search(args, target)
assert ans == -1, "error"



# args = [-1,0,3,5,9,12]
# target = 7
# ans = Solution().search(args, target)
# print(ans)
# assert ans == -1, "error"
