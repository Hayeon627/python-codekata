# 제곱수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 10. 09:23:53

def solution(n):
    x = int(n ** 0.5)
    return 1 if x * x == n else 2