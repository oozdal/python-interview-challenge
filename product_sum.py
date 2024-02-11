# Question
# Any two integers are chosen from a list and if the multiplication of those two chosen numbers 
# are greater than the summation of the elements from the list return True, otherwise False

# Solution 1
def is_product_greater_than_sum(numbers: list):
    """
    Checks if there exist any two distinct integers from the given list 
    whose product is greater than the sum of all integers in the list.

    Parameters:
    numbers (list of int): List of integers.

    Returns:
    bool: True if there exist two integers whose product is greater than the sum,
          otherwise False.
    """
    # Check if there are at least two numbers in the list
    if len(numbers) < 2:
        return False

    # Iterate through all pairs of distinct numbers in the list
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Check if the product of the current pair is greater than the sum of all numbers
            if numbers[i] * numbers[j] > sum(numbers):
                return True

    # If no such pair is found, return False
    return False


# Solution 2
def is_product_greater_than_sum_with_numpy(numbers):

    import numpy as np

    """
    Checks if there exist any two distinct integers from the given list 
    whose product is greater than the sum of all integers in the list.

    Parameters:
    numbers (list or numpy.ndarray): List or array of integers.

    Returns:
    bool: True if there exist two integers whose product is greater than the sum,
          otherwise False.
    """
    if len(numbers) < 2:
        return False

    numbers_array = np.array(numbers)
    product_of_pairs = np.multiply.outer(numbers_array, numbers_array)

    return np.any(product_of_pairs > numbers_array.sum())


if __name__ == "__main__":
    numbers_list = [2, 3, 4, 5, 6]
    print(is_product_greater_than_sum_with_numpy(numbers_list))  # Output: True
