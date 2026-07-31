# 소인수분해
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120852
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 07. 31. 17:35:03

def solution(n):
    answer = []
    i = 2
    while i <= n:
        if n % i == 0:
            answer.append(i)
            n //= i
        else:
            i += 1
    answer = sorted(list(set(answer)))
    return answer