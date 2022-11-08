from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using Two Pointers approach
        # TC : O(n), SC: O(1)
        index, last_index = 0, -1
        n = len(numbers)
        while numbers[index] + numbers[last_index] != target and index != n and last_index != - n:
            if numbers[index] + numbers[last_index] > target:
                last_index -= 1
            elif numbers[index] + numbers[last_index] < target:
                index += 1
        return [index+1, n-~last_index]

numbers = [2,7,11,15]
ans = Solution().twoSum(numbers, 9) # [1,2]
print(ans)

numbers = [-3,-2,4]
ans = Solution().twoSum(numbers, 2) # [2,3]
print(ans)

numbers = [-1,0]
ans = Solution().twoSum(numbers, -3) # [1,2]
print(ans)