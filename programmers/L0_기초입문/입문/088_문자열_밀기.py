# 문자열 밀기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120921
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 04. 17:55:51

def solution(A, B):
    answer = -1
    for i in range(0, len(A)):
        if A == B:
            answer = i
            break
        A = A[-1] + A[:-1]
    return answer