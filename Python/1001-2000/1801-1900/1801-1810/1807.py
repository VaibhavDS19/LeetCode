class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = dict()
        for k in knowledge:
            d[k[0]] = k[1]
        n = len(s)
        sr = ''
        l = []
        i = 0
        while i < n:
            while i < n and s[i] != '(':
                l.append(s[i])
                i += 1
            if i < n:
                i += 1
                while i < n and s[i] != ')':
                    sr += s[i]
                    i += 1
                i += 1
                if sr in d.keys():
                    for ch in d[sr]:
                        l.append(ch)
                else:
                    l.append('?')
                sr = ''
        return ''.join(l)
