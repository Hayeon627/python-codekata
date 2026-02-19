# 가위 바위 보
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120839
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 19. 09:51:09

def solution(rsp):
    answer = ''
    
    for a in rsp:
        if a == '2':
            answer += '0'
        elif a == '0':
            answer += '5'
        else:
            answer += '2'
    
    return answer