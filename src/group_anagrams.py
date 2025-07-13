"""
Group all anagrams together from a list of strings.
"""

from collections import defaultdict

def group_anagrams(strs):
    anagram_groups = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        anagram_groups[key].append(word)

    for group in anagram_groups.values():
        print(' '.join(group))

if __name__ == "__main__":
    # Example usage
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    group_anagrams(strs)