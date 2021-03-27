class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if ord(word[0]) > 95:
            for ch in word:
                if ord(ch) < 95:
                    return False
        else:
            if ord(word[1]) < 95:
                for ch in word[1:]:
                    if ord(ch) > 95:
                        return False
            else:
                for ch in word[1:]:
                    if ord(ch) < 95:
                        return False
        return True
