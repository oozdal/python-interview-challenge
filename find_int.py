# Problem
# Given an array with all integers from 1 to n
# except for one, write a function to return the missing integer.
# This can be done in O(n) time complexity and O(1) space complexity.

# Solution 1
def find_missing_int_naive(list: list):
    # space complexity O(n)
    missing_int_set = set(list)
    # space complexity O(n)
    int_set = {i for i in range(1, len(list)+ 2)}
    missing_int = int_set.difference(missing_int_set)
    iterator = iter(missing_int)
    return next(iterator)    


# Solution 2
def find_missing_int(list: list):
    missing_sum = sum(list)
    non_missing_sum = 0
    for i in range(1, len(list) + 2):
        non_missing_sum += i

    return non_missing_sum - missing_sum


# Solution 3
# n * (n + 1) / 2 === sum of all integers from 1..n
def find_missing_int_formula(list: list):
    n = len(list) + 1 # adding 1 as one of the integers is missing!
    sum_total = n * (n+1) // 2
    return sum_total - sum(list)


if __name__ == '__main__':
    missing_int = [1, 2, 6, 7, 9, 3, 4, 10, 8]
    print(find_missing_int_formula(missing_int))