from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def TheSplit(arr: List[int]) -> List[int]:
            n = len(arr)
            if n < 2:
                return arr
            mid = n // 2
            return MergeSort(TheSplit(arr[:mid]), TheSplit(arr[mid:]))
        
        def MergeSort(l: List[int], r: List[int]) -> List[int]:
            ans = []
            while l and r :
                ans.append(r.pop(0) if l[0] > r[0] else l.pop(0))
            return ans+r if len(r) else ans+l
        
        nums[:] = TheSplit(nums)