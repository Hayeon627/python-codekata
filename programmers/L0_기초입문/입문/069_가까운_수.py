# 가까운 수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120890
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 07. 31. 00:27:45

def solution(array, n):
    array.sort()
    diff_list = [abs(num-n) for num in array]
    answer = array[diff_list.index(min(diff_list))]
    return answer