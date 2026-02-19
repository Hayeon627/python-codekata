# 개미 군단
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120837
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 19. 09:51:23

def solution(hp):
    generals = hp // 5
    hp %= 5
    soldiers = hp // 3
    hp %= 3
    workers = hp
    return generals + soldiers + workers
