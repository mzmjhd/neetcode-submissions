import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sub = re.sub('[\\W_]', '', s.lower())
        p1 = 0
        p2 = len(sub) - 1
        while (p1 < p2):
            if sub[p1] != sub[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True