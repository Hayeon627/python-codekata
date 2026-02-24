# 인덱스 바꾸기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120895
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 24. 10:57:54

def solution(my_string, num1, num2):
    answer = list(my_string)
    answer[num1], answer[num2] = answer[num2], answer[num1]
            
    return ''.join(answer)