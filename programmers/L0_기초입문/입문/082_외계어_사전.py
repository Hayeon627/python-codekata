# 외계어 사전
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120869
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 01. 16:44:01

def solution(spell, dic):
    for word in dic:
        if set(word) == set(spell):
            return 1
    return 2