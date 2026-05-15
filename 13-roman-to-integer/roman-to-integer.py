class Solution:
    def romanToInt(self, s: str) -> int:
        length = len(s)
        dict1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
        dict2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        number = 0
        x = 0
        while x < length:
            if s[x:x+2] in dict2:
                number += dict2[s[x:x+2]]
                x += 2
            else:
                number += dict1[s[x]]
                x += 1

        return number
