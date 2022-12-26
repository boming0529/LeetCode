class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Using One Pass Hash Table
        # Time Complexity : O(n)
        # Space Complexity : O(2n)
        ht_s = {}
        ht_t = {}
        for _s, _t in zip(s,t):
            # if hash table get is none
            if ht_s.get(_s, None) == None:
                if _t in ht_s.values():
                    return False
                ht_s.update({
                    _s: _t
                })
            else: # check conflict
                if ht_s.get(_s) != _t:
                    return False
                

            # if ht_t.get(t[i], None) == None:
            #     ht_t.update({
            #         t[i]: s[i]
            #     })
            # else:
            #     if ht_t.get(t[i]) != s[i]:
            #         return False

        return True