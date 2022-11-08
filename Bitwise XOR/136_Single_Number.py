from typing import List

# Suggested Read : https://ithelp.ithome.com.tw/articles/10213278

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using python set diffence
        return 2*sum(set(nums))- sum(nums)
        
        # bitwise xor
        ans = 0
        for num in nums:
            ans ^= num
        return ans
    
        


# OJ Case
arr = [2,2,1]
ans = Solution().singleNumber(arr)
assert ans == 1, "error"

arr = [4,1,2,1,2]
ans = Solution().singleNumber(arr)
assert ans == 4, "error"

arr = [1]
ans = Solution().singleNumber(arr)
assert ans == 1, "error"

# general test case 

arr = [-2,-2,2,2,0,0,1]
ans = Solution().singleNumber(arr)
assert ans == 1, "error"

arr = [-200,-200,200,200,0,0,10]
ans = Solution().singleNumber(arr)
assert ans == 10, "error"