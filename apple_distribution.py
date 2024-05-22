# Suppose we are given an array of apples as well as an array of boxes.
# Each elemnt in the apple array is number of apples in a container.
# Each box is in the boxes array is number of apples that certain box can store.
# Meaning, we are given 3 boxes, and one box can store 5 apples, the other one can store 1 apple,
# and the last one can store 8 apples.
# How many boxes do we needf to store all of the apples?


class Solution:
    @staticmethod
    def find_boxes(apples: list, boxes: list) -> int:
        total_apples = sum(apples)
        boxes.sort(reverse=True)

        number_of_boxes = 1

        for box in boxes:        
            if total_apples <= box:
                total_apples -= box
            else:
                number_of_boxes += 1
                total_apples -= box

        return number_of_boxes
    

def test_solution():

    apples = [2, 1, 4, 3]
    boxes = [5, 1, 8]

    return Solution.find_boxes(apples, boxes)

print(test_solution())