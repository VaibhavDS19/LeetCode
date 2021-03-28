class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for w in words:
            b = True
            for c in w:
                if c not in allowed:
                    b = False
            if b:
                count += 1
        return count
