def pivotInteger(n: int) -> int:
    left = 0
    nums = list(range(1, n + 1))
    sum_nums = sum(nums)
    for k, v in enumerate(nums):
        left = left + v
        if left == sum_nums - left + v:
            return k + 1
    return -1


pivotInteger(8)


# 1 2 3 4 5 6 7 8

# 1 2 3 4 5 6 7 8

# 1 2 3 4 5 6
# 6 7 8
