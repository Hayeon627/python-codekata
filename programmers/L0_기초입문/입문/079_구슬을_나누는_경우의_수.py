# 구슬을 나누는 경우의 수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120840
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 01. 16:04:58

def solution(balls, share):
    numerator = 1
    denominator = 1
    
    for a, b in zip(range(balls, balls-share, -1), range(share, 0, -1)):
        numerator *= a
        denominator *= b
        
    answer = numerator // denominator         # 조합은 정수로 나오기 때문에 정수 나눗셈 사용
    return answer