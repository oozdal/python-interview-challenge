# Write a Python Program to find out common letters between two strings
# Example
# 1) NAINA
# 2) REEENE


def find_common_letter(str1: str = "NAINA", str2: str = "REEENE"):
    s1 = set(str1)
    s2 = set(str2)

    common_letter =  s1.intersection(s2)

    return common_letter

if __name__ == "__main__":
    print(find_common_letter())

