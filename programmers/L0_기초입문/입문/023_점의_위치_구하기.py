# 점의 위치 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120841
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 04. 12:54:04

def solution(dot):
    a = dot[0]
    b = dot[1]
    
    if a > 0 and b > 0:
        return 1
    elif a < 0 and b > 0:
        return 2
    elif a < 0 and b < 0 :
        return 3
    else:
        return 4