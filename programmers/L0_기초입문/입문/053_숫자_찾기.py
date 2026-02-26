# 숫자 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120904
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 26. 09:40:14

def solution(num, k):
    answer = str(num).find(str(k))
    return answer + 1 if answer != -1 else -1