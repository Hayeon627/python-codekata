# 컨트롤 제트
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120853
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 07. 31. 17:25:48

def solution(s):
    answer = 0
    nums = s.split()
    for i in range(0, len(nums)):
        if nums[i] == 'Z':
            answer -= int(nums[i-1])
        else:
            answer += int(nums[i])
    return answer