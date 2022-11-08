from typing import List

# 題目來源：
# Two pointer (also known as 'sliding window')
# https://guides.codepath.com/compsci/Two-pointer-%28also-known-as-%27Sliding-Window%27%29

# 分析問題與備註：
# https://leetcode.com/problems/minimum-size-subarray-sum/solutions/520204/python-3-o-n-and-o-nlogn-two-pointer-and-binary-search/?languageTags=python3
# 本題有更佳的解題方式
# Time Complexity : O(n logn) Binary Search
# Time Complexity : O(n)      Two Pointer

class Solution:
    def minSubArrayLenByTwoPointer(self, s: int, nums: List[int]) -> int:
        # 不錯的中文解說 ：
        # LeetCode 刷題 pattern - Sliding Window
        # https://blog.techbridge.cc/2019/09/28/leetcode-pattern-sliding-window/
        i = 0
        res = len(nums)+1
        sums = 0
        count = 0
        for j in range(len(nums)):
            sums += nums[j]
            while sums >=s:
                res = min(res, j-i+1)
                if res == 1 : break
                sums -= nums[i]
                i+=1
                count += 1
        print(f'count : {count}')
        return res if res<len(nums)+1 else 0

    # 大於等於都可以
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # find target number by kadane's Alg + flst slow points 
        # TC : O(2n-1), SC: O(1~m) m<n , m 比target 大的 element
        if not nums: return 0 
        L, R = 0, 1
        local_max = nums[0]
        local_min_len, global_mix_len = 1 , float("inf")
        if nums[L] >= target:
            global_mix_len = 1
        count = 0
        while R < len(nums) and L < len(nums) - 1 and global_mix_len != 1:
            if nums[R] >= target:
                global_mix_len = 1
                continue
     
            # local_max = max(nums[R], local_max + nums[R])
            local_max = local_max + nums[R]
            local_min_len += 1
            # print(L, R, nums[L],nums[R],local_max, local_min_len, global_mix_len)
            # if nums[R] > target:
            #     nums.append(0) # 補一個虛擬的值給 R+2 位置
            #     L, R, local_max, local_min_len = R+1, R+2, nums[R+1], 0
            if local_max >= target:
                # if local_max == target:
                global_mix_len = min(global_mix_len, local_min_len)
                local_max = local_max - nums[L] - nums[R]
                L += 1
                local_min_len -= 2
            else:
                R += 1
            count += 1
        print(f'count : {count}')

        return global_mix_len if global_mix_len != float("inf") else 0

    # 部落格的題目稍微不同, 這邊是等於
    def findTargetMinLenSubarray(self, nums: List[int], target : int) -> int:
        # find target number by kadane's Alg + flst slow points 
        # TC : O(n^2), SC: O(1~m) m<n , m 比target 大的 element
        if not nums: return 0 
        L, R = 0, 1
        local_max = nums[0]
        local_min_len, global_mix_len = 1 , float("inf")
        if nums[L] == target:
            global_mix_len = 1
        
        while R < len(nums) and L < len(nums) - 1 and global_mix_len != 1:
            if nums[R] == target:
                global_mix_len = 1
                continue
     
            local_max = max(nums[R], local_max + nums[R])
            local_min_len += 1
            print(L, R, nums[L],nums[R],local_max, local_min_len, global_mix_len)
            if nums[R] > target:
                nums.append(0) # 補一個虛擬的值給 R+2 位置
                L, R, local_max, local_min_len = R+1, R+2, nums[R+1], 0
            elif local_max >= target:
                if local_max == target:
                    global_mix_len = min(global_mix_len, local_min_len)
                local_max = local_max - nums[L] - nums[R]
                L += 1
                local_min_len -= 2
            else:
                R += 1

        return global_mix_len if global_mix_len != float("inf") else 0


# arr = [2,3,1,2,4,3]
import random
arr = [e for e in range(1, 7)] * 2 
random.shuffle(arr)
print(arr)
ans = Solution().minSubArrayLenByTwoPointer(7, arr) # 2
print(ans)

# arr2 = [2,3,1,2,4,3]
ans = Solution().minSubArrayLen(7, arr) # 2
print(ans)


# error :

# arr = [1,2,3,4,5]
# ans = Solution().minSubArrayLen(arr, 11) # 3
# print(ans)

# arr = [10, 2, 3]
# ans = Solution().minSubArrayLen(6, arr) # 3
# print(ans)

# arr = [1,1,1,1,7]
# ans = Solution().minSubArrayLen(7, arr) # 3
# print(ans)