def solution(s):
    # 정렬하고, reverse로 뒤집는다.
    return "".join(sorted(list(s), reverse=True))


print(solution("Zbcdefg"))