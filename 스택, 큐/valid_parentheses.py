class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        stack = []
        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)
            elif bracket == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif bracket == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            elif bracket == "]":
                if len(stack) == 0 or stack.pop() != '[':
                    return False

        if len(stack) != 0:
            return False
        return True