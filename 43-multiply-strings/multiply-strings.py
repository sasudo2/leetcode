class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # The maximum length of the result can't exceed len(num1) + len(num2)
        res = [0] * (len(num1) + len(num2))

        # Reverse both strings to iterate from right to left (ones, tens, hundreds...)
        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                # Multiply individual digits
                digit_product = int(n1) * int(n2)

                # Add to the correct position in the result array (handling previous carries)
                pos = i + j
                res[pos] += digit_product

                # Handle carry over to the next position
                res[pos + 1] += res[pos] // 10
                res[pos] %= 10

        # Strip any trailing zeros from the end of the list and reverse back
        while len(res) > 1 and res[-1] == 0:
            res.pop()

        # Convert the array of digits back into a final string
        return "".join(str(d) for d in reversed(res))
