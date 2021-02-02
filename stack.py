n = int(input())
def solution(bracket):
    answer = []
    if bracket[0] == "(":
        for i in range(len(bracket)):
            # print(bracket[i])
            if bracket[i] == "(":
                answer.append(bracket[i])
                print(answer)
            elif bracket[i] == ")":
                answer.pop(-1)
                print(answer)
        if len(answer) == 0:
            print("True")
        else:
            print("False")
    else:
        print("False")


print(solution(")("))
