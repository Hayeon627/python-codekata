# 피자 나눠 먹기 (3)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120816
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 04. 12:49:40

def solution(slice, n):
    answer = n // slice
    
    if n % slice > 0:
        answer += 1

    return answer