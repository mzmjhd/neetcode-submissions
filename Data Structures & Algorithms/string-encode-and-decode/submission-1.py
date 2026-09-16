import re

class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""
        for n in strs:
         s = s + n + "%20"   
        return s
    def decode(self, s: str) -> List[str]:
        strs = re.split("%20", s)
        strs.pop(-1)
        return strs