# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 01. 20. 09:46:00

def solution(n, k):
    if n < 10:
        answer = n * 12000 + k * 2000
    else:
        answer = n * 12000 + (k - (n//10)) * 2000
    return answer