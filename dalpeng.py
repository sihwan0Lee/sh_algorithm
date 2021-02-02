
def solution(n, words):
    words_set = set([words[0]])
    prev_words = words[0]

    for i in range(1, len(words)):
        if (prev_words[-1] != words[i][0]) or words[i] in words_set:
            return [(i % n)+1, (i//n)+1]
        words_set.add(words[i])
        prev_words = words[i]
    return [0, 0]


# print(solution(3, ["tank", "kick", "know", "wheel",
    # "land", "dream", "mother", "robot", "tank"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))


def solution(n, words):
    word_set = set([words[0]])
    prev_words = words[0]

    for i in range(1, len(words)):
        if (prev_words[-1] != words[i][0]) or words[i] in words_set:
            