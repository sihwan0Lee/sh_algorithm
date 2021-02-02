def solution(clothes):
    closet = {}
    result = 1
    for element in clothes:
        key = element[1]
        value = element[0]
        if key in closet:
            closet[key].append(value)

        else:
            closet[key] = [value]
    print(closet)
    for key in closet.keys():
        print(key)
        result = result * (len(closet[key])+1)
    return result - 1


print(solution([["yellow_hat", "headgear"], [
      "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
