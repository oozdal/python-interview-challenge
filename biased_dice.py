# Bags of biased dice
# Assume that you roll two separate dice from two bags, each containing three biased dice.

# bag1 = [[1,2,3,6,6,6], [1,2,3,4,4,6], [1,2,3,3,3,5]]
# bag2 = [[2,2,3,4,5,6], [3,3,3,4,4,5], [1,1,2,4,5,5]]

# Pick one dice from each bag randomly; roll both dice
# Success if the dice outcomes add up to 8; otherwise, failure

# Question: Implement a Python function roll_biased_dice(n, bag1, bag2) that simulates rolling two biased dice 
# from bags bag1 and bag2 respectively, n times. Each bag contains three dice with different probabilities of 
# rolling a particular number. The function should return two dictionaries: results containing the probabilities 
# of rolling a sum of 8 for each possible combination of dice rolls, and others containing the probabilities of 
# rolling a sum other than 8 for each combination. Ensure that the total probability across all combinations sums up to 1.0.


import random


class Solution:

    @staticmethod
    def roll_biased_dice(n, bag1: list, bag2: list):
        results = {}
        others = {}
        for i in range(n):
            bag_index1 = random.randint(0, 2)
            dice_index1 = random.randint(0, 5)
            bag_index2 = random.randint(0, 2)
            dice_index2 = random.randint(0, 5)

            point1 = bag1[bag_index1][dice_index1]
            point2 = bag2[bag_index2][dice_index2]
            total_sum = point1 + point2

            key = '%s_%s' % (point1, point2)

            if total_sum == 8:
                results[key] = results.get(key, 0) + 1
            else:
                others[key] = others.get(key, 0) + 1

        # Normalization using dictionary comprehension
        results = {k: v/n for k, v in results.items()}
        others = {k: v/n for k, v in others.items()}

        return results, others
    

def test_prob_sum():
    """
    This test function ensures that the total probability across all combinations sums up to 1.
    """

    bag1 = [[1,2,3,6,6,6], [1,2,3,4,4,6], [1,2,3,3,3,5]]
    bag2 = [[2,2,3,4,5,6], [3,3,3,4,4,5], [1,1,2,4,5,5]]
    results, others = Solution.roll_biased_dice(10000, bag1, bag2)
    total_prob = '{:.1f}'.format(sum(list(results.values())) + sum(list(others.values())))
    assert total_prob == '1.0'

    return total_prob


def testSolution():
    bag1 = [[1,2,3,6,6,6], [1,2,3,4,4,6], [1,2,3,3,3,5]]
    bag2 = [[2,2,3,4,5,6], [3,3,3,4,4,5], [1,1,2,4,5,5]]
    return Solution.roll_biased_dice(100000, bag1, bag2)


print('Total Probability:', test_prob_sum())
results, *_ = testSolution()
print(results) # returns {'6_2': 0.03741, '3_5': 0.06165, '5_3': 0.01274, '4_4': 0.02519, '2_6': 0.00881}


