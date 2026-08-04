# 로그인 성공?
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120883
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 04. 16:37:23

def solution(id_pw, db):
    for id, pw in db:
        if id == id_pw[0]:
            if pw == id_pw[1]:
                answer = 'login'
                break
            else:
                answer = 'wrong pw'
                break
        answer = 'fail'
    return answer