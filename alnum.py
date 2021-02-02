def solution(s):
    answer = []
    for i in s:
        if i.isalnum():
            answer.append(i)
    return(answer)


print(solution("...!@BaT#*..y.abcdefghijklm"))
