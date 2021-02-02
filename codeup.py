def solution(N, stages):
    fail = {}
    count = {}
    stages.sort()

    for i in range(1, N+1):
        count[i] = stages.count(i)
    a = len(stages)
    for i in range(1, N+1):
        if count[i] != 0:
            fail[i] = count[i] / a
            a = a - count[i]

        else:
            fail[i] = 0
    print(fail)
    return sorted(fail, key=lambda z: fail[z], reverse=True)


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
