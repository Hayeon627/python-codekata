# 순서쌍의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120836
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 05. 15:42:35

def solution(n):
    nums = 0
    
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i * i == n:
                nums += 1
            else:
                nums += 2
            
    return nums