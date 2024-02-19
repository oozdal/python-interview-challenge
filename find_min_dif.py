# Find Minimum Difference between two elements of array
# arr = [5, 32, 45, 4, 12, 18, 25]
# Algorithm
# 1) Sort the elements of array
# 2) Initialise the first difference value to be largest. Start comparing the difference
# of first elements with it.
# 3) Compare elements with its adjacent element & keep track of minimum difference.


def find_min(arr: list = [5, 32, 45, 4, 12, 18, 25]):
    arr = sorted(arr) # Time complexity O(nlogn)
    size = len(arr)
    min_diff = 999_999

    for i in range(size-1): # Time complexity O(n)
        if arr[i+1] - arr[i] < min_diff:
            min_diff = arr[i+1] -  arr[i]
        return min_diff


if __name__ == "__main__":
    print(find_min())

