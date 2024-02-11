# Write a Python Program to Count the frequency of words appearing in a string
# Example
# Ozer loves eating apple and mango. Her sister also loves eating apple and mango.

# Solution 1
def find_freq_sol1(string: str):

    words = string.split()
    d = {}

    for i in words:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i] + 1
            
    return d            


# Solution 2
def find_freq_sol2(string: str):

    words = string.split()
    d = {}

    for i in words:
        d[i] = d.get(i, 0) + 1
            
    return d            


if __name__ == "__main__":
    print(find_freq_sol2("Ozer loves eating apple and mango. Her sister also loves eating apple and mango"))

