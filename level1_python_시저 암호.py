'''
문제명 : 시저 암호

문제: 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다. z는 1만큼 밀면 a가 됩니다.
문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

제한조건 : 공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.

링크
https://programmers.co.kr/learn/courses/30/lessons/12926

basic code

def solution(s, n):
    answer = ''
    return answer
'''
'''
print(ord("a"))  97
print(ord("z"))  122
print(ord("A"))  65
print(ord("Z"))  90
print(ord(" "))  32
'''


def solution(s, n):
    return shift(s, n)


def shift(array, n):
    # _array = array.split()
    answer = ''
    # for 로 입력받은 array 요소 하나씩 받아와서
    for i in array:
        # ord 로 아스키코드로 변환
        _i = ord(i)
        # 그 아스키코드가 32면 패스
        if _i == 32:
            pass
        # 아닐 경우 & 대문자라면 아래 계산 적용
        elif i.istitle() and _i+n >= 91:
            _i = 65+_i+n-91
        # 소문자면 아래 계산 적용
        elif not i.istitle() and _i+n >= 123:
            _i = 97+_i+n-123
        # 그 외에는 입력된 n 값 계산
        else:
            _i = ord(i) + n
        # 계산 결과를 answer에 추가
        answer = answer + chr(_i)
    # answer를 리턴
    return answer


# print(solution("abc", 25))
