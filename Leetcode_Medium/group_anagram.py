from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            if tuple(count) in result:
                result[tuple(count)].append(s)
            else:
                 result[tuple(count)] = s

        return result.values()

print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))