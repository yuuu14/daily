prompt = """
Please complete a function in python.
function_name: get_common_in_prefix, input_parameters: a: List[int], b: List[int], return: List[int].
description: input List a and b are permutation of n with length of n, your task is to comstruct List c with length of n, where c[i] is the size of common elements of a[:i+1] and b[:i+1], and return c.
"""


class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size + 1)
    
    def update(self, index, value=1):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index
    
    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

def get_common_in_prefix(a, b):
    n = len(a)
    pos_a = {x: i for i, x in enumerate(a)}
    pos_b = {x: i for i, x in enumerate(b)}
    elements = [(pos_a[x], pos_b[x]) for x in range(1, n+1)]
    elements.sort()  # Sort by pos_a[x]
    
    ft = FenwickTree(n)
    c = [0] * n
    ptr = 0
    for i in range(n):
        while ptr < n and elements[ptr][0] <= i:
            q = elements[ptr][1] + 1  # 1-based indexing
            ft.update(q)
            ptr += 1
        count = ft.query(i + 1)  # Query up to i+1
        c[i] = count
    return c

print(get_common_in_prefix(
    a=[1,2,3,4,5],
    b=[5,4,2,3,1],
))