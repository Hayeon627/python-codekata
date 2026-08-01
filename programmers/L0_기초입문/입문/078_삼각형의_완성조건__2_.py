# 삼각형의 완성조건 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120868
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 01. 15:51:20

def solution(sides):
    answer = 0
    for i in range(max(sides)-min(sides)+1, max(sides)+1):
        answer += 1
    for i in range(max(sides)+1, min(sides)+max(sides)):
        answer += 1
    return answer