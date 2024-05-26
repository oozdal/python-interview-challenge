# Code Everyday: May 26, 2024
# Write a Python function that takes a list of integers as input
# and returns the maximum product that can be obtained from multiplying
# any three integers in the list.


class Solution:
    def maxProduct(self, nums: list) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
    

def testSolution1():
    nums=[-10, -9, 5, 6, 7, 8, -2, -4, -1, 2]
    sol = Solution()
    return sol.maxProduct(nums) # returns 720

def testSolution2():
    nums=[-10, -9, -2, -4, -1, 2]
    sol = Solution()
    return sol.maxProduct(nums) # returns 180

def testSolution3():
    nums=[2, 3, 5, 7]
    sol = Solution()
    return sol.maxProduct(nums) # return 105


print(testSolution1())
print(testSolution2())
print(testSolution3())