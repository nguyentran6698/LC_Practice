def windown(array):
    left, right = None, None
    s = sorted(array)
    n = len(array)
    for i in range(n):
        if array[i] != s[i] and left is None:
            left = i
        elif array[i] != s[i]:
            right = i

    return left, right
