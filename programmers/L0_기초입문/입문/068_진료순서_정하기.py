# 진료순서 정하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120835
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 07. 31. 00:23:15

def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    # sorted : 원본 유지 / .sort : 원본 변환
    answer = [sorted_emergency.index(x) + 1 for x in emergency]
    return answer