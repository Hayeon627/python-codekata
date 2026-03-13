# 배열 회전시키기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120844
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 03. 13. 09:49:06

def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer = [numbers[-1]] + numbers[:-1]
    else:
        answer = numbers[1:] + [numbers[0]]          
    return answer