def solution(new_id):
    answer = []
    new_id = new_id.lower()

    for i in new_id:
        if i.isalnum() or i == '-' or i == '.' or i == '_':
            answer.append(i)

    print(answer)
    if answer[0] == ".":
        answer = answer[1:]
    elif


print(solution("...!@BaT#*..y.abcdefghijklm"))
