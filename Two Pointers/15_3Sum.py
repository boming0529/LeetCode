from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def merge(l, r):
            ans = []
            while l and r:
                ans.append(r.pop(0) if l[0] > r[0] else l.pop(0))
            return ans + r if len(r) else ans + l

        def sortMerge(arr):
            if len(arr) < 2:
                return arr
            mid = len(arr) // 2
            return merge(sortMerge(arr[:mid]), sortMerge(arr[mid:]))
        
        nums = sortMerge(nums)
        ans = []
        for _ in range(len(nums)-2):
            target = nums.pop(0)
            # print(target)
            m = len(nums)
            prefix, last = 0, -1
            # while prefix < m-1 and ~last < m-1:
            while prefix + ~last + 1 < m:
                add = nums[last] + nums[prefix]
                # print([target, nums[last], nums[prefix]])
                if add == -target:
                    # print('in')
                    if -target > 0:
                        if [nums[last], nums[prefix], target] not in ans:
                            ans.append([nums[last], nums[prefix], target])
                    else:
                        if [target, nums[prefix], nums[last]] not in ans:
                            ans.append([target, nums[prefix], nums[last]])
                    prefix += 1
                elif -target > add:
                    prefix += 1
                else:
                    last -= 1
        return ans


numbers =  [-1,0,1,2,-1,-4]
ans = Solution().threeSum(numbers) # [[2,-1,-1],[-1,0,1]]
print(ans)

numbers = [0,1,1]
ans = Solution().threeSum(numbers) # []
print(ans)

numbers = [0,0,0]
ans = Solution().threeSum(numbers) # [[0,0,0]]
print(ans)

# error
numbers = [0,0,0, 0]
ans = Solution().threeSum(numbers) # [[0,0,0]]
print(ans)

numbers = [1,2,-2,-1]
ans = Solution().threeSum(numbers) # []
print(ans)

numbers = [-2,0,1,1,2]
ans = Solution().threeSum(numbers) # [[-2,0,2],[-2,1,1]]
print(ans)
