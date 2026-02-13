# 옷가게 할인 받기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120818
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 13. 09:50:22

def solution(price):
    if price >= 500000:
        discount = 0.2
    elif price >= 300000:
        discount = 0.1
    elif price >= 100000:
        discount = 0.05
    else:
        discount = 0
    answer = int(price * (1-discount))
    return answer