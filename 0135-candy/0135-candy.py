class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        rating = [1] * n

        # left to right: handle the left neighbor
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                rating[i] = rating[i - 1] + 1

        # right to left: handle the right neighbor
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                rating[i] = max(rating[i], rating[i + 1] + 1)

        return sum(rating)
        