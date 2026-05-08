class Solution:
    def myAtoi(self, s: str) -> int:
        try:
            s = s.lstrip()
            integer = ""
            if s[0] == "-":
                integer = "-"
                s = s[1:]
            elif s[0] == "+":
                s = s[1:]

            for x in s:
                if x.isdigit():
                    integer += x
                else:
                    break

            if integer == "" or integer == "-":
                integer = "0"

            integer = int(integer)
            if integer > 2147483647:
                integer = 2147483647
            if integer < -2147483648:
                integer = -2147483648
            return integer
        except:
            return 0