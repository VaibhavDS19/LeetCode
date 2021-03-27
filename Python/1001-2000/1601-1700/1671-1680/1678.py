class Solution:
    def interpret(self, command: str) -> str:
        n = len(command)
        i = 0
        l = []
        while i < n:
            if command[i] == 'G':
                i += 1
                l.append('G')
            elif command[i+1] == ')':
                i += 2
                l.append('o')
            else:
                i += 4
                l.append('a')
                l.append('l')
        return "".join(l)
