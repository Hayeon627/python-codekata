# 특이한 정렬
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120880
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 04. 18:23:34

def solution(numlist, n):
    answer = sorted(numlist, key=lambda x: (abs(x - n), -x))
    return answer