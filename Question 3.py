class Solution:
    def makeValidParentheses(self, s: str) -> str:
        stack = []
        S = list(s)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    S[i] = ""
        for j in stack:
            S[j] = ""
        return "".join(S)
    #time complexity: O(n)
