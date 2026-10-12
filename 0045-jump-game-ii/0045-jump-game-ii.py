class Solution(object):
    def jump(self, nums):
        jumps = 0
        current_end = 0   # farthest index reachable with the current number of jumps
        farthest = 0      # farthest index reachable with one more jump
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps
        