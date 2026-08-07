# OX퀴즈
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120907
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 07. 13:33:17

def solution(quiz):
    answer = []
    correct = 0
    for q in quiz:
        nums = q.split(' ')
        if nums[1] == '+':
            correct = int(nums[0]) + int(nums[2])
        elif nums[1] == '-':
            correct = int(nums[0]) - int(nums[2])
        
        if correct == int(nums[-1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer