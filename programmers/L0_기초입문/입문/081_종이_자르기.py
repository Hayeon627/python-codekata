# 종이 자르기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120922
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 01. 16:35:27

def solution(M, N):
    answer = M-1 + M * (N-1)
    return answer