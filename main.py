from typing import List
from numba import njit, prange
from numpy import int64


@njit(fastmath=True)
def rabbit_hole(array: List[int64], primary: List[int64], secondary: List[int64], row: int64, size: int64) -> int64:
    cases = int64(0)
    next_row = row + 1

    for column in array:
        primary_val = row + column
        secondary_val = row - column

        if primary_val not in primary and secondary_val not in secondary:

            if next_row == size:
                return 1

            arr2 = [x for x in array if x != column]
            primary.append(primary_val)
            secondary.append(secondary_val)

            cases += rabbit_hole(arr2, primary, secondary, next_row, size)

            primary.pop()
            secondary.pop()

    return cases


@njit(parallel=True)
def n_queens(size: int64) -> int64:
    total = int64(0)

    mid = size // 2

    results = [0 for _ in range(mid)]

    for n in prange(mid):
        results[n] = rabbit_hole([int64(x) for x in range(size) if x != n], [int64(n)], [int64(-n)], int64(1), size)

    for res in results:
        total += res

    total *= 2

    if mid != size / 2:
        total += rabbit_hole([int64(x) for x in range(size) if x != mid], [int64(mid)], [int64(-mid)], int64(1), size)

    return total


if __name__ == "__main__":
    from time import time

    start = time()
    solutions = n_queens(16)
    diff = time() - start

    print(f"I found {solutions} ways in {diff} seconds")
