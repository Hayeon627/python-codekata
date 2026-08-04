# 유한소수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120878
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 04. 18:12:54

def solution(a, b):
    answer = 0
    x, y = a, b
    
    # 유클리드 호제법
    while y > 0:
        x, y = y, x % y
    gcd = x
    
    b //= gcd
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
        
    if b == 1:
        answer = 1
    else:
        answer = 2
    return answer
