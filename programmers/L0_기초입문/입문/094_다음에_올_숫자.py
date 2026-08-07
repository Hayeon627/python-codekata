# 다음에 올 숫자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120924
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 07. 13:37:15

def solution(common):
    answer = 0
    if (common[1] - common[0]) == (common[2] - common[1]):
        answer = common[1] - common[0] + common[-1]
    else:
        answer = common[1] // common[0] * common[-1]
    return answer