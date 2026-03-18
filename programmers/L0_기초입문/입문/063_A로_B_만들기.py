# A로 B 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120886
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 03. 18. 11:14:36

def solution(before, after):
    if sorted(before) == sorted(after): # 알파벳 순으로 자동 정렬됨
        return 1
    return 0