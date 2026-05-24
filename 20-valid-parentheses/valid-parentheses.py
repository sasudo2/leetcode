class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = {')':'(', '}':'{', ']':'['}
        stack = []
        for x in s:
            if valid_dict.get(x) == None:
                stack.append(x)
            else:
                if len(stack) != 0:
                    if stack[-1] == valid_dict.get(x):
                        stack.pop(-1)
                    else:
                        return False
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False