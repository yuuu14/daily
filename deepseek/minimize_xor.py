

from llm_template import *

def get_formatted_prompt():
    function_name = "find_num_with_min_XOR"
    description = r"""Given num1, num2, find num3 with following condictions:
- binary repr of num3 and num2 have the same number of 1
- $num3 := \arg \min(min3 \XOR min1)$"""
    parameters = [
        Param(
            name="num1",
            type="int",
            description="Positive integer",
        ),
        Param(
            name="num2",
            type="int",
            description="Positive integer",
        ),
    ]
    returns = [
        Param(
            name="num3",
            type="int",
            description="Result",
        )
    ]
    print(formatted_prompt(function_name, description, parameters, returns))


def find_num_with_min_XOR(num1, num2):
    s = bin(num2).count('1')
    c = bin(num1).count('1')
    
    if c == s:
        return num1
    elif c > s:
        # Unset (c - s) least significant set bits
        k = c - s
        for i in range(0, 60):
            if (num1 >> i) & 1:
                num1 &= ~(1 << i)
                k -= 1
                if k == 0:
                    break
        return num1
    else:
        # Set (s - c) least significant unset bits
        k = s - c
        for i in range(0, 60):
            if not (num1 >> i) & 1:
                num1 |= (1 << i)
                k -= 1
                if k == 0:
                    break
        return num1
    

args = dict(
    num1=123,
    num2=12313,
)

print(find_num_with_min_XOR(**args))