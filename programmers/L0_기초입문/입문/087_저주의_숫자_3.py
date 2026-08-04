# 저주의 숫자 3
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120871
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 04. 17:41:33

def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1           
    return answer