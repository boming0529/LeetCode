from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 備註犯錯, 這題我採用了 two point approach
        # 一開始蠻順利的, 但是後來我設了幾個 edge case 或 broundary case 明顯的發現問題
        # 必須改用其他方式

        # using Two Pass Hashtable 
        # Time Complexity : O(n~2n)
        # Space Complexity : O(n)
        if len(nums) < 2:
            return 0 if nums[0] == 0 else -1
        
        postfix_sum = nums[:]
        for i in range(2, len(nums) + 1):
            postfix_sum[-i] += postfix_sum[-i+1]

        if postfix_sum[1] == 0:
            return 0

        indx = 0
        prefix_sum = nums[0]  
        for j in range(2, len(nums)):
            
            if prefix_sum == postfix_sum[j]:
                return j - 1
            else:
                indx += 1
                prefix_sum += nums[indx]
                if len(nums) - (indx+1) == 1 and prefix_sum == 0:
                    return indx+1
        return -1


# OJ
args = [1,7,3,6,5,6]
ans = Solution().pivotIndex(args)
print(ans)

# broundary case
args = [-200,1,-1]
ans = Solution().pivotIndex(args)
print(ans)

args = [2,1,-1]
ans = Solution().pivotIndex(args)
print(ans)


args = [0,0,1,-1,2]
ans = Solution().pivotIndex(args)
print(ans)


args = [0,-1000,1000,-3]
ans = Solution().pivotIndex(args)
print(ans)