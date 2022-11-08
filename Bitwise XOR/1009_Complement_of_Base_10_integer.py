# 本題同 476. Number Complement

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Time Complexity : O(logN)
        # Space Compexity : O(1)
        if n == 0: return 1

        m = n
        all_one_bit = 0
        while m:
            all_one_bit <<= 1 
            all_one_bit |= 1
            m >>= 1
        return n ^ all_one_bit

#OJ test case 
# 0 <= n < 10^9
ans = Solution().bitwiseComplement(5)
assert ans == 2 , 'error'

ans = Solution().bitwiseComplement(7)
assert ans == 0, 'error'

ans = Solution().bitwiseComplement(10)
assert ans == 5, 'error'


# Boundary Case
ans = Solution().bitwiseComplement(0)
assert ans == 1, 'error'

ans = Solution().bitwiseComplement(1000000000)
assert ans == 73741823, 'error'