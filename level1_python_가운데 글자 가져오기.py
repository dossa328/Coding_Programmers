'''
문제명 : 가운데 글자 가져오기

문제: 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요.
단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

제한조건 : s는 길이가 1 이상, 100이하인 스트링입니다.

링크 : https://programmers.co.kr/learn/courses/30/lessons/12903

basic code

def solution(s):
    answer = ''
    return answer
'''


def solution(s):
    # 배열 길이 반으로 한다음, 2로 나누어 나머지 0, 1 에 맞게 중간 인덱스값 출력
    if len(s) % 2 == 0:
        result = s[int(len(s) / 2)-1] + s[int(len(s) / 2)]
        return result

    elif len(s) % 2 == 1:
        result = s[int(len(s) / 2)]
        return result


print(solution("abcde"))
print(solution("qwer"))
