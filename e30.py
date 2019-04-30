#!/usr/bin/env python3

import itertools
import functools

def digits(ns):
    return functools.reduce(lambda x, y: x * 10 + y, ns, 0)

def main():
    N_UPPER = 9**5 * 5
    nums = [digits(ns) for ns in itertools.product(range(10), repeat=6) if digits(ns) == sum(n**5 for n in ns)]
    print(nums)
    print(sum(num for num in nums if num not in [0, 1]))


if __name__ == '__main__':
    main()