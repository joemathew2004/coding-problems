"""
Find the maximum number of times you can form the word "balloon" 
using the characters in a given string.
"""

from collections import Counter

def max_number_of_balloons(text):
    count = Counter(text)
    return min(
        count['b'],
        count['a'],
        count['l'] // 2,
        count['o'] // 2,
        count['n']
    )

if __name__ == "__main__":
    text = "loonbalxballpoon"
    result = max_number_of_balloons(text)
    print(result)