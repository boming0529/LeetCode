class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Using One Pass Hash Table
        # Time Complexity : O(n)
        # Space Complexity : O(2n)
        ht_s = {}
        ht_t = {}
        for i in range(len(s)):
            # if hash table get is none
            if ht_s.get(s[i], None) == None:
                ht_s.update({
                    s[i]: t[i]
                })
            else: # check conflict
                if ht_s.get(s[i]) != t[i]:
                    return False

            if ht_t.get(t[i], None) == None:
                ht_t.update({
                    t[i]: s[i]
                })
            else:
                if ht_t.get(t[i]) != s[i]:
                    return False

        return True