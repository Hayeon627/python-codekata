# 최댓값 만들기(1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 01. 22. 09:43:53

def solution(numbers):
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    return answer