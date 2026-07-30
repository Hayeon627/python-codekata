# 7의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120912
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 07. 31. 00:15:29

def solution(array):
    combined_str = "".join(map(str, array))
    answer = combined_str.count('7')
    return answer