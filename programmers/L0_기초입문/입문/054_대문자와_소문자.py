# 대문자와 소문자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120893
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 26. 09:45:42

# def solution(my_string):
#     answer = ''
#     for a in my_string:
#         if a.islower():
#             answer += a.upper()
#         else:
#             answer += a.lower()
#     return answer

def solution(my_string):
    answer = my_string.swapcase()
    return answer