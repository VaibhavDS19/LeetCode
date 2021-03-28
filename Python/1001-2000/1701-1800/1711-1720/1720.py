class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        l = [first]
        for i in encoded:
            first = first ^ i
            l.append(first)
        return l
