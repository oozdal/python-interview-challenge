
# Everyday 1 Coding Interview Question: May 27, 2024
# Question: Write a Python function called find_duplicates(nums) that takes in a list of integers nums 
# and returns a list containing all the elements that appear more than once in the list. The order of elements
# in the output list should be the same as their appearance in the input list. Ensure that the solution 
# runs in O(n) time complexity.

#find_duplicates([1, 2, 3, 1, 4, 2, 5])  # Output should be [1, 2]
#find_duplicates([1, 2, 3, 4, 5])        # Output should be []
#find_duplicates([1, 2, 2, 3, 3, 3])     # Output should be [2, 3]


class Solution:
    def find_duplicates(self, input: list) -> list:
        frequency = {}
        duplicates = []

        for key in input:
            if key in frequency:
                frequency[key] += 1
            else:
                frequency[key] = 1

        for freq in frequency:
            if frequency[freq] > 1:
                duplicates.append(freq)

        return duplicates


def testSolution1():
    sol = Solution()
    return sol.find_duplicates([1, 2, 3, 1, 4, 2, 5])  # Output should be [1, 2]


def testSolution2():
    sol = Solution()
    return sol.find_duplicates([1, 2, 3, 4, 5])        # Output should be []


def testSolution3():
    sol = Solution()
    return sol.find_duplicates([1, 2, 2, 3, 3, 3])     # Output should be [2, 3]


print(testSolution1())
print(testSolution2())
print(testSolution3())

