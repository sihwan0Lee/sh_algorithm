def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort()
    print(s)
    for i in s:
        ii = i.split(',')
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
    return answer


#print(solution("{{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}"))
# print(solution("{{20,111},{111}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
