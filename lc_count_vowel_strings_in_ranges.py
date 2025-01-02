from typing import (
    List,
    Tuple,
    Optional,
)
from collections import (
    Counter,
    deque,
)


class Solution:
    @staticmethod
    def is_vowelStrings(s: str) -> int:
        return 1 if (s[0] in "aeiou" and s[-1] in "aeiou") else 0
    
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sums = [0] * (len(words) + 1)
        for i, word in enumerate(words, start=1):
            prefix_sums[i] = prefix_sums[i - 1] + Solution.is_vowelStrings(word)
        res = []
        for l, r in queries:
            res.append(prefix_sums[r+1] - prefix_sums[l])
        return res



    def __call__(self, foo: callable, **kwargs: dict):
        return foo(**kwargs)
        

def main():
    solution = Solution()

    args = dict(
        words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
    )
    results = solution(solution.vowelStrings, **args)
    print(results)


if __name__ == "__main__":
    main()






