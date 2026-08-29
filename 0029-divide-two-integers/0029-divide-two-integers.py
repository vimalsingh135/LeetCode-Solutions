class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        # Handle overflow edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of result
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp_divisor, num_shifts = divisor, 0
            # Double the divisor until it exceeds dividend
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_shifts += 1
            dividend -= temp_divisor
            quotient += (1 << num_shifts)

        return -quotient if negative else quotient