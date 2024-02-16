# Find out pairs with given sum value of an array
# arr = [5, 7, 4, 3, 9, 8, 19, 21]
# sum=17


# Time complexity is O(n^2) as we are using a nested for loop
def find_pairs_nested_loop(arr, sum):
    
    n = len(arr)

    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == sum:
                print("Values of pair are", arr[i], "&", arr[j])


# We are using single while loop, it means time complexity is O(n)
# Overall, time complexity is O(nlogn)
# Space complexity O(1) as we are not using any space
def find_pairs(arr, sum):
    arr.sort() # Time complexity O(nlogn)
    left=0
    right=len(arr)-1
    while(left<=right):
        if(arr[left]+arr[right]>sum):
            right=right-1
        elif(arr[left]+arr[right]<sum):
            left=left+1
        elif(arr[left]+arr[right]==sum):
            print("Values of pair are", arr[left], "&", arr[right])
            right=right-1
            left=left+1


if __name__ == "__main__":
    arr = [5, 7, 4, 3, 9, 8, 19, 21]
    find_pairs_nested_loop(arr=arr, sum=17)
    find_pairs(arr=arr, sum=17)

