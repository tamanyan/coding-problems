from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}",
            ")": None,
            "]": None,
            "}": None,
        }

        stack: List[str] = []

        for i in range(0, len(s)):
            if len(stack) > 0 and pairs[stack[-1]] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])

        return len(stack) == 0
        