# 한 번만 등장한 문자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120896
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 07. 28. 02:57:57

def solution(s):
    unique_chars = sorted([char for char in s if s.count(char) == 1])
    return "".join(unique_chars)
