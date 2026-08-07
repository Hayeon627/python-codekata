# 연속된 수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120923
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 07. 13:57:24

def solution(num, total):
    answer = []
    first = (total // num) - ((num - 1) // 2)
    for i in range(num):
        answer.append(first + i)
    return answer