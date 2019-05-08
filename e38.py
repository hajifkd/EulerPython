#!/usr/bin/env python3

from itertools import permutations

def is_product(n):
    s = ''.join(n)
    for i in range(1, 6):
        base = int(s[:i])
        i_start = i
        for j in range(2, 9):
            target = base * j
            s_target = str(target)

            if s[i_start:].startswith(s_target):
                i_start += len(s_target)
            else:
                break
            
            if i_start == 9:
                return True
    
    return False

def main():
    n = max(filter(is_product, permutations("987654321")))
    print(''.join(n))

if __name__ == '__main__':
    main()