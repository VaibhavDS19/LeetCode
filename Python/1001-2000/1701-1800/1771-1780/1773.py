class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        i = 0
        c = 0
        if ruleKey == "color":
            i = 1
        elif ruleKey == "name":
            i = 2
        for l in items:
            if l[i] == ruleValue:
                c += 1
        return c
