# 짝수 홀수 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120824
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 11. 09:42:05

def solution(num_list):
    odd = 0
    even = 0
    
    for n in num_list:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    answer = [even, odd]
    
    return answer