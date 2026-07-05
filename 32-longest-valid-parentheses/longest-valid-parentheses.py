class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = list(s)
        zero_list = []
        p1 = 0
        p2 = 1
        if len(s) < 2:
            return 0
        
        back = False
        while True:
            if p1 >= len(s):
                break
            elif s[p1] == ')':
                if p1 == 0 or s[p1-1] == ')':
                    zero_list.append(-1)
                    p1 += 1
                    p2 += 1 
                else:
                    p1 -= 1
                    p2 -= 1 
                    back = True
            elif s[p1] == '(' and p2 >= len(s):
                break
            elif s[p1] == '(' and s[p2] == ')':
                if back == False:
                    zero_list.append(0)
                    zero_list.append(0)
                    s.pop(p1)
                    s.pop(p1)
                else:
                    for i in range(1, len(zero_list)+1):
                        if zero_list[len(zero_list)-i] == 1:
                            zero_list[len(zero_list)-i] = 0
                            zero_list.append(0)
                            s.pop(p1)
                            s.pop(p1)
                            break
                        elif zero_list[len(zero_list)-i] == -1:
                            break
                    back = False
            elif s[p1] == '(' and s[p2] == '(':
                zero_list.append(1)
                p1 += 1
                p2 += 1

        longest = 0
        counter = 0
        for i in zero_list:
            if i == 0:
                counter += 1
                longest = counter if counter > longest else longest
            else:
                counter = 0

        return longest

 