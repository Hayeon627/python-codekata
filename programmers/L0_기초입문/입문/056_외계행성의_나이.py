# 외계행성의 나이
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120834
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 03. 12. 16:53:08

def solution(age):
    answer = ''
    for a in str(age):
        answer += chr(int(a) + ord('a'))
    return answer

def solution(age):
    return "".join([chr(int(a) + ord('a')) for a in str(age)])

def solution(age):
    return "".join(map(lambda a: chr(int(a) + ord('a')), str(age)))

