# 짝수는 싫어요
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120813
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 13. 09:44:09

def solution(n):
    answer = []
    for i in range(n+1):
        if i % 2 == 1:
            answer.append(i)
    return answer