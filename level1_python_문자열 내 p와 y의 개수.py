'''
문제명 : 문자열 내 p와 y의 개수

문제: 대문자와 소문자가 섞여있는 문자열 s가 주어집니다.
s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요.
'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다.
단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

제한조건 : a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
a와 b의 대소관계는 정해져있지 않습니다.

링크 : https://programmers.co.kr/learn/courses/30/lessons/12916

basic code

def solution(s):
    answer = True

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True
'''


def solution(s):
    # 입력받은 모든 문자열 upper (대문자화)
    up_s = s.upper()
    # y 와 p의 개수를 센다음, 각 저장
    count_y = up_s.count('Y')
    count_p = up_s.count('P')
    # 비교에 따라 True, False를 return
    if count_p == count_y:
        return True
    elif not count_p == count_y:
        return False


print(solution("pPoooy"))