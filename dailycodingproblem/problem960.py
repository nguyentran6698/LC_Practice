def solution(paths):
    mx = 0
    for i in range(len(paths)):
        if i > mx:
            return False
        mx = max(i + paths[i], mx)
        if mx == len(paths) - 1:
            return True


print(solution([1, 2, 1, 0, 0]))
