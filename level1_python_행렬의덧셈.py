#-*- coding:utf-8 -*-
'''
문제명 : 행렬의 덧셈

문제: 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

제한조건 : 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

링크 : https://programmers.co.kr/learn/courses/30/lessons/12950?language=python3

basic code

def solution(arr1, arr2):
    answer = [[]]
    return answer
'''

# 기본적으로 주어지는 함수 solution
def solution(arr1, arr2):
    # 함수 내 함수 addlist, 리스트를 만들어준다
    def addlists(a, b):
        # lambda(임시함수)로 인자 x,y를 주고 x+y 기능 정의 및 매핑으로 인자 a,b(arr1, arr2)를 받음
        # map을 통해 각 a,b에 lambda 작업 실시
        # 그냥 리턴하면 object값을 주기에 list로 받음
        return list(map(lambda x, y: x + y, a, b))
    # lambda(임시함수)로 인자 x,y를 주고 addlist 호출 기능 정의(매개변수 x,y) 및 매핑으로 리스트 arr1, arr2를 받음
    return list(map(lambda x, y: addlists(x, y), arr1, arr2))
