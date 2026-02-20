# 문자열 정렬하기 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120850
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 20. 09:35:25

def solution(my_string):
    answer = []
    for a in my_string:
        if a.isdigit():
            answer.append(int(a))
    answer.sort()
    return answer