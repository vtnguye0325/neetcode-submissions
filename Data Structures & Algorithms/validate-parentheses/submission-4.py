class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <2:
            return False;
        if s[0] not in ["(","{","["]:
            return False;
        stack = []
        for bracket in s:
            if bracket in ["(","{","["]:
                stack.append(bracket)
            else:
                if len(stack) ==0:
                    return False
                if bracket == ")":
                    if not stack.pop() == "(":
                        return False
                elif bracket == "}":
                    if not stack.pop() == "{":
                        return False
                else:
                    if not stack.pop() == "[":
                        return False
        if len(stack)==0:
            return True
        return False
