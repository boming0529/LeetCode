import math

class Solution:
    def maximum69Number (self, num: int) -> int:
        # General Solution : Greedy Alg + fast/slow pointer
        # Time Compliexity : O(N)
        # Space Complexity : O(1)
        n = num
        fast = 0
        last = None
        while n:
            n, mod = divmod(n,10)
            if 1 ^ (mod & 1): # 6
                last = fast
            fast += 1
        if last == None:
            return num
        return num + (9-6) * 10 ** last


        # n = num
        # master = 0

        # bin_num = 0
        # while n:
        #     master = master << 1 | 1
        #     n, mod = divmod(n,10)
        #     print(n, mod)
        #     bin_num = bin_num << 1 | (mod & 1)
        # print(bin(bin_num))
        # diff = master ^ bin_num
        # print(bin(diff))
        # max_diff = diff.bit_length()
        # print(max_diff)
        # return int(str(bin(bin_num)).replace('0b', '')) * 9 + int(str(bin(bin_num)).replace('0b', '')) * 6

num = 9699
ans = Solution().maximum69Number(num)
print(ans)