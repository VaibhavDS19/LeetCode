class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s = set(ransomNote)
        for ch in s:
            if magazine.count(ch) < ransomNote.count(ch):
                return False
        return True
