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
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        Ellipsis
        # dp[i] = dp[i - zero] + dp[i - one] i-zero>=0 i-one>=0

        MOD = int(1e9) + 7
        dp = {-1: 0, 0: 1}
        for i in range(1, low):
            dp[i] = (dp[max(i - zero, -1)] + dp[max(i - one, -1)]) % MOD
        sum = 0
        for i in range(low, high+1):
            dp[i] = (dp[i - zero] + dp[i - one]) % MOD
            sum = (sum + dp[i]) % MOD
        return sum


    def __call__(self, foo: callable, **kwargs: dict):
        return foo(**kwargs)
        

def main():
    solution = Solution()

    args = dict(
        low = 200, high = 200, zero = 10, one = 1
    )
    results = solution(solution.countGoodStrings, **args)
    print(results)


if __name__ == "__main__":
    main()






