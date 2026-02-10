# 모음 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120849
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 10. 09:41:05

def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for v in vowels:
        my_string = my_string.replace(v, '')
    return my_string