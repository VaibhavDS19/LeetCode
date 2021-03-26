class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1], [1, 1]]
        l = [1]
        if numRows == 1:
            return [ret[0]]
        if numRows == 2:
            return ret
        for i in range(3, numRows+1):
            l = [1]
            for j in range(1, i-1):
                l.append(ret[i-2][j-1] + ret[i-2][j])
            l.append(1)
            ret.append(l)
            i += 1
        return ret
