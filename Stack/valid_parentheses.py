class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return False

        stack = []
        p_map = {")": "(", "]": "[", "}": "{"}

        for p in s:
            # If p in open parentheses
            if p in p_map.values():
                stack.append(p)
                continue

            if len(stack) == 0:
                return False

            if stack[-1] == p_map[p]:
                stack.pop()
                continue

            return False

        return len(stack) == 0
