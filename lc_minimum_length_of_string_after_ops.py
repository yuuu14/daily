from typing import (
    List,
    Tuple,
    Optional,
)
from collections import (
    Counter,
    deque,
    defaultdict,
)
import pprint


class Solution:
    def minimumLength(self, s: str) -> int:
        # axaxaxa    
        counter = Counter(s)

        res = sum(1 if v & 1 else 2 for v in counter.values())

        return res

    def __call__(self, foo: callable, **kwargs: dict):
        return foo(**kwargs)
        

def main():
    solution = Solution()

    args = dict(
        s = "aa",
    )
    results = solution(solution.minimumLength, **args)
    pprint.pp(results)


if __name__ == "__main__":
    main()






