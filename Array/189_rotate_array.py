# -*- coding: utf-8 -*-
# from typing import List # python version < 3.9 using 
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = n - (k % n)   
        nums[:] = nums[index:] + nums[:index]