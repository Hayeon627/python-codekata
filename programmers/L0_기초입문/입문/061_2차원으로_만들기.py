# 2차원으로 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120842
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 03. 17. 17:09:31

def solution(num_list, n):
    answer = [[]]
    for i in range(len(num_list)):
        group_idx = i // n
        if group_idx >= len(answer):
            answer.append([])
        answer[group_idx].append(num_list[i])
    return answer

def solution(num_list, n):
    return [num_list[i:i + n] for i in range(0, len(num_list), n)]
