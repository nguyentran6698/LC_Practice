def solution(skills):
    skill = sorted(skills)
    fast = len(skill) - 1
    slow = 0
    s = skill[slow] + skill[fast]
    sum = skill[slow] * skill[fast]
    slow += 1
    fast -= 1
    for _ in range(1,len(skill) // 2):
        print(sum)
        if skill[slow] + skill[fast] != s:
            return -1
        sum += skill[slow] * skill[fast]
        slow += 1
        fast -= 1
    return sum
skill = [3,2,5,1,3,4]
print(solution(skill))
