# 최댓값 만들기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120862
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 23. 09:41:24

# def solution(numbers):
#     answer = 0
#     for i in numbers:
#         if i > answer:
#             answer 
#     return answer

def solution(numbers):
    answer = numbers[0] * numbers[1]
    n = len(numbers)
    
    for i in range(n):
        for j in range(i + 1, n):
            product = numbers[i] * numbers[j]
            if product > answer:
                answer = product
                
    return answer