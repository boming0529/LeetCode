from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # region : Brvle Force , TC : O(n^2)
        # last = nums.pop()
        # max_product, process = last, [last]
        # while nums:
        #     last = nums.pop()
        #     process.append(1)
        #     for index in range(len(process)):
        #         process[index] = last * process[index]
        #         max_product = process[index] ^ ((process[index] ^ max_product) & -(process[index] < max_product))
        # return max_product
        # endregion

        # region : Kadane's Algorithm TC : O(n), SC : O(1)
        size = len(nums)
        product_left_to_right = nums
        product_right_to_left = nums[::-1]
        # update product of two kinds of subarray, 
		# one is extending from left to right, the other is from right to left
        for i in range(1, size):
            # extends from left hand side, if meets 0 then restart in-place by itself.
            product_left_to_right[i] *= (product_left_to_right[i-1] or 1)
            # extends from right hand side, if meets 0 then restart in-place by itself
            product_right_to_left[i] *= (product_right_to_left[i-1] or 1)
        return max(max(product_left_to_right), max(product_right_to_left))
        # endregion

        # region : another Kadane's Algorithm 
        dp = [ 0 for _ in nums ]
        dm = [ 0 for _ in nums ]
        dp[0] = nums[0]
        dm[0] = nums[0]
        for i in range(1,len(nums)) :
            dp[i] = max( dp[i-1]*nums[i], dm[i-1]*nums[i], nums[i] )
            dm[i] = min( dp[i-1]*nums[i], dm[i-1]*nums[i], nums[i] )
        return max(dp)
        # endregion 

        # region : another Kadane's Algorithm : Solution 
        # DP Solution by youtube 
        # https://www.youtube.com/watch?v=lXVy6YWFcRM
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res
        # endregion 

input = [0,2,3,-2,4,0]
ans = Solution().maxProduct(input)
print(ans)