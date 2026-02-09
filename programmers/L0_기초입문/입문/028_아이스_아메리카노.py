# 아이스 아메리카노
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120819
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 09. 09:50:06

def solution(money):
    answer = []
    cnt = money // 5500
    change = money % 5500
    answer.extend([cnt, change])
    return answer