def solution(strings, n):
    l = []
    l.append(strings[n])
    strings.pop(n)
    # print(l)

    strings.sort()  # 또다른 새로운 리스트생성.
    # print(strings)
    strings.insert(n, l[0])
    print(strings)


print(solution(["sun", "bed", "car"], 1))
