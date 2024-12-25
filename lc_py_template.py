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
    def some_problem(self, **kwargs: dict):
        return 42

    def __call__(self, foo: callable, **kwargs: dict):
        return foo(**kwargs)
        

def main():
    solution = Solution()

    args = dict(
        val=1,
    )
    results = solution(solution.some_problem, **args)
    print(results)


if __name__ == "__main__":
    main()






