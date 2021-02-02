def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        for j in range(len(board)):
            #print(move, board[j])
            if board[j][move - 1] == 0:
                pass
            else:
                basket.append(board[j][move-1])
                board[j][move-1] = 0   # 이게 잘안되는듯. ==으로하면 안되고 = 으로해야함
                break

        print(basket)

    # 바스켓은 완성했고, 이제 같은애들만 뺴내면된다.

        if len(basket) >= 2 and basket[len(basket)-1] == basket[len(basket)-2]:
            basket.pop(-1)
            print(basket)
            basket.pop(-1)
            print(basket)
            answer += 1
            print(answer)
    return answer * 2


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
      4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
