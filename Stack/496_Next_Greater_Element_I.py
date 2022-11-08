from typing import List
from collections import deque


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Using Stack
        th = {}
        max_local = 0
        while nums2:
            num2 = nums2.pop()
            th


# OJ Test Case 
