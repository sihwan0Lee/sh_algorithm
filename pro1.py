def solution(n):
    count = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            i += j
            if i == n:
                count += 1
                break
            elif i > n:
                break
    return count


print(solution(15))
