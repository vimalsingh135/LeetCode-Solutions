class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product = 1

            # Compute digit product
            for digit in str(n):
                product *= int(digit)

            if product % t == 0:
                return n

            n += 1