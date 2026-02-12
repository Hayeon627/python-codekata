# 중앙값 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120811
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 12. 17:15:11

def solution(array):
    array.sort()
    answer = array[len(array)//2]
    return answer