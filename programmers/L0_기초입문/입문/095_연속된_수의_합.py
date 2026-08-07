# 연속된 수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120923
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 07. 13:55:03

def solution(num, total):
    answer = []
    first = 0
    if num % 2 == 1:
        first = (total // num) - (num - 1) // 2
    else:
        first = (total // num + 1) - (num // 2)
    for i in range(num):
        answer.append(first + i)
    return answer