class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = [1]
        if rowIndex:
            r = rowIndex
            j = 1
            for i in range(1, rowIndex + 1):
                j *= i
                l.append(r//j)
                r *= (rowIndex - i)
        return l
