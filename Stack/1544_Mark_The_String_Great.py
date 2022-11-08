class Solution:
    def makeGood(self, s: str) -> str:
        # Using fast slow pointer and bitwise trick and stack
        # stack
        #   +=   :  mean stack append
        #  [:-1] :  mean stack pop
        # Time Complexity : O(n)
        # Space Complexity : O(n) , where n is strgin len, create new good_str variable

        if len(s) < 2 : return s
        
        fast, slow = s[0], None
        good_str = ""
        for _char in s :
            slow, fast = fast, _char            
            if not ord(slow) ^ 32 ^ ord(fast) and len(good_str):
                good_str = good_str[:-1]
                fast = good_str[-1] if len(good_str) else fast
            else:
                good_str += fast

            # if good_str:

            #     if ord(slow) ^ (ord(slow) | ord(' ')) and ord(slow) ^ 32 ^ ord(fast):
            #         good_str += fast
            #         print("cur:",good_str)
            #     elif ord(slow) ^ (ord(slow) & ord('_')) and ord(slow) ^ 32 ^ ord(fast):
            #         good_str += fast
            #         print("cur:",good_str)
            #     else:
            #         print("The Same", fast)
            #         good_str = good_str[:-1]
            #         fast = good_str[-1] if len(good_str) else fast
            #         print("cur:",good_str)
            # else:
            #     good_str += fast
        return good_str

# OJ 
arg_str = "leEeetcode"
ans = Solution().makeGood(arg_str)
assert ans == 'leetcode', 'error'

arg_str = "s"
ans = Solution().makeGood(arg_str)
assert ans == 's', 'error'

arg_str = "abBAcC"
ans = Solution().makeGood(arg_str)
assert ans == '', 'error'


arg_str = "eabBAcdCDE"
ans = Solution().makeGood(arg_str)
assert ans == 'ecdCDE', 'error'

arg_str = "Pp"
ans = Solution().makeGood(arg_str)
assert ans == '', 'error'

arg_str = "ogHhGOoEOoeOfaNnAF"
ans = Solution().makeGood(arg_str)
print(ans)
assert ans == '', 'error'