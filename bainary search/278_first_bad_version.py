# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= 1501

class Solution:
    def firstBadVersion(self, n: int, low: int = 0, ht: dict = {}) -> int:
        # Top-Down DP (Recursion) + Binary Search
        # Time Complexity : O(lng(n))
        # Space Complexity : O(log(n))
        if n == 1 : return 1

        mid = (n+low) // 2
        #mid = n + (n-low)//2 # python not overflow, but from a good habis
        if ht.get(str(mid), None) == None:
            ht.update({
                str(mid): isBadVersion(mid),
            })
        if ht.get(str(mid)): # True
            if ht.get(str(mid-1), None) == None:
                ht.update({
                    str(mid-1): isBadVersion(mid-1),
                })
            if ht.get(str(mid)) ^ ht.get(str(mid-1)):
                return mid
            n = mid
            
        else: # False
            if ht.get(str(mid+1), None) == None:
                ht.update({
                    str(mid+1): isBadVersion(mid+1),
                })
            if ht.get(str(mid)) ^ ht.get(str(mid+1)):
                return mid+1
            low = mid
                
        return self.firstBadVersion(n, low, ht)

# OJ
# n = 5 
# ans = Solution().firstBadVersion(5)
# assert ans == 4 , 'error'

# n = 1
# ans = Solution().firstBadVersion(1)
# assert ans == 1 , 'error'

# n = 5 
ans = Solution().firstBadVersion(2408)
assert ans == 1501 , 'error'