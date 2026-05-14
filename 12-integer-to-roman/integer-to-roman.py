class Solution:
    def intToRoman(self, num: int) -> str:
        value = ""
        while num > 0:
            if num >= 1000:
                num -= 1000
                value += "M"
            elif num >= 500:
                if num - num%100 == 900:
                    num -= 900
                    value += "CM"
                else:
                    num -= 500
                    value += "D"
            elif num >= 100:
                if num - num%100 == 400:
                    num -= 400
                    value += "CD"
                else:
                    num -= 100
                    value += "C"
            elif num >= 50:
                if num - num%10 == 90:
                    num -= 90
                    value += "XC"
                else:
                    num -= 50
                    value += "L"
            elif num >= 10:
                if num - num%10 == 40:
                    num -= 40
                    value += "XL"
                else:
                    num -= 10
                    value += "X"
            elif num >= 5:
                if num == 9:
                    num -= 9
                    value += "IX"
                else:
                    num -= 5
                    value += "V"
            else:
                if num == 4:
                    num -= 4
                    value += "IV"
                else:
                    num -= 1
                    value += "I"
        return value