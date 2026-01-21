# 짝수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120831
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 01. 21. 09:20:31

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            answer += i
    return answer