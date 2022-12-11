import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list]:
        res = collections.defaultdict(int)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()
    # time complexity: O(n)
