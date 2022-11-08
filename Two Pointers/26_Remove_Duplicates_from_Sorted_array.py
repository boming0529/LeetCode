# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        remove_count = 0
        fast, slow = None, None
        for i in range(len(nums)):
            fast = nums[i-remove_count]
            if fast == slow:
                nums.pop(i-remove_count)
                remove_count += 1
            slow = fast
        return len(nums)