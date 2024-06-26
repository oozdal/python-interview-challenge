# Given a list of words: Words = ['Hire', 'Me', 'Uber']
# and a string S="HMUP"
# Write a function to determine if the string is an acronym of the list of words.

from typing import List


class Solution:

    @staticmethod
    def isAcronym(words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False

        for count, word in enumerate(words):
            if word[0] != s[count]:
                return False
        
        return True



def test_solution():
    """
    Test if the provided solution is correct.
    """

    words = ['Hire', 'Me', 'Uber']
    string="HMUP"

    return Solution.isAcronym(words, string) == False


print(test_solution())