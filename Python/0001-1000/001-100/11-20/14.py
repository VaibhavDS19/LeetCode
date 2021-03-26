class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = ""
        if strs:
            for ch in strs[0]:
                for s in strs:
                    if not s.startswith(l+ch):
                        return l
                l += ch
        return l
