# 합성수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120846
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 03. 16. 18:02:02

def solution(n):
    answer = []
    for i in range(1, n + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count >= 3:
            answer.append(i)
    return len(answer)

import math

def solution(n):
    answer = 0
    for i in range(4, n + 1): # 1, 2, 3은 합성수가 아니므로 4부터 시작
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                answer += 1
                break # 합성수임을 확인했으므로 더 이상 나눌 필요 없음
    return answer