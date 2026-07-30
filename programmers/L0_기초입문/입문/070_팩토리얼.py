# 팩토리얼
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120848
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 07. 31. 00:38:50

def solution(n):
    fact = 1
    i = 0
    while n >= fact:
        i += 1
        fact = i * fact
    answer = i - 1
    return answer