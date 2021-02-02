def solution(arr):
    l = []  # 인덱스 첫번쨰 수로 나눠진 것들의 나머지
    a = arr[0]
    a_yak = []
    # 첫번째수의 약수 구하기
    for i in range(1, a+1):
        if a % i == 0:
            a_yak.append(i)
    print("약수들", a_yak)
    # print(max(a_yak))

    # 전체 리스트 검증
    for i in arr:
        if i % (max(a_yak)) != 0:
            l = arr
            x = 1

        elif i % (max(a_yak)) == 0:
            l.append(i // (max(a_yak)))
            x = (max(a_yak))

    print(l)

    # 답
    a = 1
    for i in l:

        a *= i
    return a * x


print(solution([6, 3, 2, 7]))
print(solution([2, 6, 8, 14]))
