def solution(priorities, location):
    answer = 0
    while priorities != []:
        max_p = max(priorities)
        pop_n = priorities.pop(0)
        if max_p == pop_n:
            print(max_p, pop_n, priorities)
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
        else:
            priorities.append(pop_n)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1

    return answer


#print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
