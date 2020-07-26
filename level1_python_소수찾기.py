def solution(n):
    # 초기화
    answer = 0
    # 입력받은 숫자 +1 까지 for
    for i in range(1, n+1):
        # 나눈 나머지가 0이라면
        if n % i == 0:
            # 합산
            answer = answer + i
    # 합산 값 리턴
    return answer

print(solution(12))