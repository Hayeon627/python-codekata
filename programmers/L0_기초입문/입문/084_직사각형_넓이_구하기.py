# 직사각형 넓이 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120860
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 04. 17:09:32

def solution(dots):
    x_dots = [dot[0] for dot in dots]
    y_dots = [dot[1] for dot in dots]
    answer = (max(x_dots) - min(x_dots)) * (max(y_dots) - min(y_dots))
    return answer