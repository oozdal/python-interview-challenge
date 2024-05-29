# Given an array nums of n integers, find three integers in nums such that the sum is closest to a given target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

# For example:
# closest_three_sum([-1, 2, 1, -4], 1) should return 2 
# because the sum that is closest to the target (1) is (-1) + 2 + 1 = 2.


class Solution:
    def closest_three_sum(self, nums, target):
        nums.sort() # Sort the array to simplify the search
        closest_sum = float('inf')  # Initialize closest sum to infinity
        n = len(nums)

        for i in range(n-2):
            left = i + 1
            right = n - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
        
        return closest_sum
    


def testSolution():
    sol = Solution()
    return sol.closest_three_sum([-1, 2, 1, -4], 1) == 2


print(testSolution()) # returns True
