# 피자 나눠 먹기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120815
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 03. 12. 16:42:28

# 라이브러리 사용
import math

def solution(n):
    return (n * 6 // math.gcd(n, 6)) // 6