# 배열 두 배 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120809
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 12. 16:57:13

def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(n*2)
    return answer