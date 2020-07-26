'''
문제명 : 두 정수 사이의 합

문제: 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

제한조건 : a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
a와 b의 대소관계는 정해져있지 않습니다.

링크 : https://programmers.co.kr/learn/courses/30/lessons/12912

basic code

def solution(a, b):
    answer = 0
    return answer
'''


def solution(a, b):
    # 최소값
    _min = min(a, b)
    # 최대값
    _max = max(a, b)
    # 초기화
    answer = 0
    # 만약 a랑 b가 같으면? a 리턴
    if a == b:
        return a
    # 아닌 모든 경우
    else:
        # for loop min에서 max+1 까지
        for i in range(_min, _max + 1):
            # 합산
            answer = answer + i
            # 리턴
        return answer

# print(solution(3,5))


