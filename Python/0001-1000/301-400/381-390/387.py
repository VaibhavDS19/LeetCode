class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_letters = sorted(set(s), key=s.index)
        for letter in unique_letters:
            if s.count(letter) == 1:
                return s.index(letter)
        return -1
