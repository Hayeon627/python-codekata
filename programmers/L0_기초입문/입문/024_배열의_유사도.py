# 배열의 유사도
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120903
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 04. 12:59:07

def solution(s1, s2):
    s3 = set(s1) & set(s2)
    return len(s3)