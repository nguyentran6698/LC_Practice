def solution(intervals):
    intervals.sort(key=lambda x: x[1])
    taken = 0
    x = intervals[0][0]
    for (begin, end) in intervals:
        if begin >= x:
            taken += 1
            x = end
    return len(intervals) - taken