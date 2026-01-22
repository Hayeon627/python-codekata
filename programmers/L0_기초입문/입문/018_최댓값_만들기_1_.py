# 최댓값 만들기(1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 01. 22. 11:45:22

# 정렬을 이용하는 방법
def solution(numbers):
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    return answer

# 반복문을 이용하는 방법
def solution(numbers):
    max1 = 0
    max2 = 0
    
    for n in numbers:
        if n > max1:
            max2 = max1
            max1 = n
        elif n > max2:
            max2 = n
            
    answer = max1 * max2
    return answer