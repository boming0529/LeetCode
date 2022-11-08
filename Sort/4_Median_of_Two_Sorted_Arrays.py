# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def TheSplit(arr: List[int]) -> List[int]:
            if len(arr) < 2:
                return arr
            mid = len(arr) // 2
            return MergeSort(TheSplit(arr[:mid]), TheSplit(arr[mid:]))
        
        def MergeSort(l: List[int], r: List[int]) -> List[int]:
            ans = []
            while l and r:
                ans.append(l.pop(0) if r[0] > l[0] else r.pop(0))
            return ans+r if len(r) else ans+l
        
        nums = nums1 + nums2 
        n = len(nums)
        output = TheSplit(nums)
        ans = None
        if n % 2: # even
            median = n // 2
            ans = output[median]
        else: # odd
            pre = (n // 2) - 1
            posted = (n // 2) 
            ans = (output[pre] + output[posted]) / 2.0
            
        return ans