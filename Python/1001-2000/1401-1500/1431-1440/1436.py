class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src = set()
        dst = set()
        for path in paths:
            src.add(path[0])
            dst.add(path[1])
        return str(dst - src)[2:-2]
