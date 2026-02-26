# 숫자 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120904
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 02. 26. 09:38:25

def solution(num, k):
    str_num = str(num)
    str_k = str(k)
    index = str_num.find(str_k)
    answer = index + 1 if index != -1 else -1
    return answer