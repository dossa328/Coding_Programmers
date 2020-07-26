'''
문제명 : 서울에서 김서방 찾기

문제: String형 배열 seoul의 element중 Kim의 위치 x를 찾아,
김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요.
seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

제한조건 : seoul은 길이 1 이상, 1000 이하인 배열입니다.
seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
'Kim'은 반드시 seoul 안에 포함되어 있습니다.

링크 : https://programmers.co.kr/learn/courses/30/lessons/12919

basic code

def solution(seoul):
    answer = ''
    return answer
'''


def solution(seoul):
    # 텍스트 미리 저장
    out_text1 = "김서방은 "
    out_text2 = "에 있다"
    # Kim 인덱스 저장
    index_kim = seoul.index("Kim")
    # 문자열 합치기
    answer = out_text1 + str(index_kim) + out_text2
    # 리턴
    return answer
    # print(answer)


solution(["Jane","Kim"])