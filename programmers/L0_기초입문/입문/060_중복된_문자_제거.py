# 중복된 문자 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120888
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 03. 16. 19:00:12

def solution(my_string):
    answer = ''
    for a in my_string:
        if a not in answer:
            answer += a
    return answer