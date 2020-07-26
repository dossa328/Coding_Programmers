'''
문제명 : 서울에서 김서방 찾기

문제: 수많은 마라톤 선수들이 마라톤에 참여하였습니다.
단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한조건 : 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.

링크 : https://programmers.co.kr/learn/courses/30/lessons/42576

basic code

def solution(participant, completion):
    answer = ''
    return answer
'''


# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for comp in completion:
#         participant.remove(comp)
#
#     return participant[0]


def solution(participant, completion):
    # 입력된 배열 sort
    participant.sort()
    completion.sort()
    # 서로 비교해서 요소가 같으면 패스, 다르면 리턴
    for i in range(len(completion)):
        if not participant[i] == completion[i]:
            return participant[i]
    # 끝까지 for 돌아서 다른게 없었다면 마지막에 남은사람이 탈락자 이므로 리턴
    return participant[-1]

print(solution(["leo", "kiki", "eden", "eden", "eden"], ["eden"]))
# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
# print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
