# Write a Python Program to convert two lists into a dictionary and then to a tuple

# Example
# list1 = ["Ali", "Mehmet", "Sarah"]
# list2 = [8434231, 57453523, 78632342]


def convert_list_to_dict(list1: list = ["Ali", "Mehmet", "Sarah"], 
                         list2: list = [8434231, 57453523, 78632342]):
    
    return dict(zip(list1, list2)) 


def dict_to_tuple(dict: dict):
    for i in dict.items():
        print(i)


if __name__ == "__main__":
    
    dict = convert_list_to_dict()
    print(dict)
    dict_to_tuple(dict)

