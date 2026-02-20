# 주사위의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120845
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 20. 09:24:36

def solution(box, n):
    answer = 1
    for i in box:
        answer *= i // n
    return answer