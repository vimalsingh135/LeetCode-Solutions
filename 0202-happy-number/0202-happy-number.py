class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def digit_sum(x):
            total = 0
            while x > 0:
                d = x % 10
                x //= 10
                total += d * d
            return total

        slow = n
        fast = digit_sum(n)

        while fast != 1 and slow != fast:
            slow = digit_sum(slow)
            fast = digit_sum(digit_sum(fast))

        return fast == 1