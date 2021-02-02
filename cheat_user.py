def solution(user_id, banned_id):
    conclusion = []
    answer = []
    sol = []
    for user in user_id:
        for ban in banned_id:
            pair = []
            pair.append(user)
            pair.append(ban)
            if len(pair[0]) == len(pair[1]):
                nopair = 0
                for i in range(len(pair[0])):
                    #print(user, ban)
                    if pair[0][i] == pair[1][i]:
                        continue
                    elif pair[0][i] != pair[1][i]:
                        if pair[1][i] == '*':
                            nopair += 1
                        elif pair[1][i] != '*':
                            nopair -= 1
                    #print("다른 철자들 갯수: ", nopair)
                count = 0
                for star in pair[1]:
                    if star == '*':
                        count += 1
                        #print(pair[1], count, nopair)
            #print(count, nopair)
            if int(nopair) == int(count):
                answer.append(pair[0])
                # print(set(answer))
    for i in answer:
        if i not in sol:
            sol.append(i)
    sol = list(set(sol))
    sol2 = sorted(sol, key=len)
    # print(sol2)
    # 순서쌍 만들기
    # for i in range(len(banned_id)):
    #    for s in sol:
    #        if len(s) == len(banned_id[i]):
    #            conclusion.append(s)
    #            print(conclusion)
    return len(sol2)-1


print(solution(["frodo", "fradi", "crodo",
                "abc123", "frodoc"], ["fr*d*", "abc1**"]))
