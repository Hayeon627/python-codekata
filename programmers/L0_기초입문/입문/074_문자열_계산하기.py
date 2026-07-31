# 문자열 계산하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120902
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 07. 31. 17:42:07

def solution(my_string):
    nums = my_string.split()
    answer = int(nums[0])
    for i in range(2, len(nums), 2):
        if nums[i-1] == '+':
            answer += int(nums[i])
        else:
            answer -= int(nums[i])
    return answer