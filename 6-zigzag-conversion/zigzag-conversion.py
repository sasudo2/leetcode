class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output_string = ""
        for i in range(numRows):
            x = i
            step1 = (numRows-1)*2-i*2
            step2 = i*2
            if x>=len(s):
                break
            output_string = output_string + s[x]
            while True:
                
                if(0 < step1):
                    x += step1
                    if(x >= len(s)):
                        break
                    output_string += s[x]
                if (0 <  step2):
                    x += step2
                    if(x>=len(s)):
                        break
                    output_string += s[x]

                if step1 == 0 and step2 == 0:
                    break
        if len(s) != len(output_string):
            output_string = s
        return output_string
   