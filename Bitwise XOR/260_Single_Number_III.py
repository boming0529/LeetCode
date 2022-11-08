from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # xor-ing
        # https://leetcode.com/problems/single-number-iii/solutions/1827748/python-bitwise-with-explanation-in-comments/?q=bitwise&orderBy=most_relevant
        xor = 0
        for num in nums:
            xor ^= num
        lsb = xor & (-xor)
        grp_set = 0
        for num in nums:
            if lsb & num:
                grp_set ^= num
        return [grp_set, xor^grp_set]


        # using Hash Table
        # th = {}
        # while nums:
        #     num = nums.pop()
        #     th[num] = th.get(num, 0) + 1
        #     if th[num] == 2:
        #         th.pop(num)
        # itera = iter(th)
        # return [next(itera), next(itera)]

        # using two pointer
        targe = 2*sum(set(nums)) - sum(nums)
        asd = list(set(nums))
        asd.sort()
        first, last = 0, -1
        while first + ~last + 1 < len(asd):
            addiation = asd[first] + asd[last]
            if targe == addiation:
                return [asd[first], asd[last]]
            elif addiation > targe:
                last -= 1
            else:
                first += 1
            

# test case
# OJ 
arr = [1,2,1,3,2,5]
ans = Solution().singleNumber(arr)
ans.sort()
assert ans == [3,5], 'error'

arr = [-1,0]
ans = Solution().singleNumber(arr)
ans.sort()
assert ans == [-1,0], 'error'

arr = [0,1]
ans = Solution().singleNumber(arr)
ans.sort()
assert ans == [0,1], 'error'