#!/usr/bin/env python3

def main():
    TARGET = 200
    COINS = [1, 2, 5, 10, 20, 50, 100, 200]
    pay_table = [[0 for _ in range(TARGET + 1)] for _ in COINS]

    pay_table[0] = [1 for _ in range(TARGET + 1)]

    for i, coin in enumerate(COINS[1:]):
        pay_table[i + 1] = [sum(pay_table[i][a - coin * j] for j in range(int(a / coin) + 1)) for a in range(TARGET + 1)]

    print(pay_table)

if __name__ == '__main__':
    main()