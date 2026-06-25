class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Edge case handling for LeetCode's 32-bit signed integer limits
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        dividend_sign = 1
        divisor_sign = 1
        if dividend < 0:
            dividend_sign = -1
            dividend = dividend * -1
        if divisor < 0:
            divisor_sign = -1
            divisor = divisor * -1

        N = 32
        A = 0
        M = divisor
        Q = dividend
        mask = 0xffffffff
        
        for n in range(N):
            # FIX 1: In a masked system, check the 32nd bit to see if A is "negative"
            is_A_negative = (A & 0x80000000) != 0

            # Both paths shift left together
            leftmost_bit = (Q >> 31) & 1
            Q = (Q << 1) & mask
            A = (A << 1) & mask
            A = (A + leftmost_bit) & mask

            if is_A_negative:
                A = (A + M) & mask
            else:
                A = (A - M) & mask

            # FIX 2 & 3: Check if the new A is negative, and update Q (not A!)
            if (A & 0x80000000) != 0:
                Q = Q & 0xfffffffe      # Set Q's last bit to 0
            else:
                Q = Q | 1               # Set Q's last bit to 1

        # Final correction step for non-restoring division
        if (A & 0x80000000) != 0:
            A = (A + M) & mask
        
        # Apply the signs
        if dividend_sign == divisor_sign:
            return Q
        else:
            return Q * -1