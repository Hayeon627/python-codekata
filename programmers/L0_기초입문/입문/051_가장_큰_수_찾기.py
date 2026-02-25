# 가장 큰 수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120899
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 25. 16:29:43

def solution(array):
    n_max = 0
    i_max = 0
    for i in range(len(array)):
        if array[i] > n_max:
            n_max = array[i]
            i_max = i
    answer = [n_max, i_max]
    return answer

# 내장함수
def solution(array):
    n_max = max(array)
    i_max = array.index(n_max)
    return [n_max, i_max]

# max + enumerate
def solution(array):
    n_max, i_max = max((v, i) for i, v in enumerate(array))
    return [n_max, i_max]
