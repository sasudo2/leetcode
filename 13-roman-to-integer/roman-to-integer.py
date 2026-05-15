class Solution:
    def romanToInt(self, s: str) -> int:
        l = list(s)
        number = 0
        while l:
            found = False
            if len(l) >= 2:
                if l[0] == "C"  and l[1] == "M":
                    l.pop(0)
                    l.pop(0)
                    number += 900
                    found = True
                elif l[0] == "C" and l[1] == "D":
                    l.pop(0)
                    l.pop(0)
                    number += 400
                    found = True
                elif l[0] == "X" and l[1] == "C":
                    l.pop(0)
                    l.pop(0)
                    number += 90
                    found = True
                elif l[0] == "X" and l[1] == "L":
                    l.pop(0)
                    l.pop(0)
                    number += 40
                    found = True
                elif l[0] == 'I' and l[1] == 'X':
                    l.pop(0)
                    l.pop(0)
                    number += 9
                    found = True
                elif l[0] == 'I' and l[1] == 'V':
                    l.pop(0)
                    l.pop(0)
                    number += 4
                    found = True
                else:
                    pass
                
            if found == False:
                num = l.pop(0)
                if num == "M":
                    number += 1000
                elif num == "D":
                    number += 500
                elif num == "C":
                    number += 100
                elif num == 'L':
                    number += 50
                elif num == "X":
                    number += 10
                elif num == "V":
                    number += 5
                elif num == "I":
                    number += 1
        return number
