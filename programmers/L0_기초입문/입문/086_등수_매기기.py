# 등수 매기기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120882
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 04. 17:27:38

def solution(score):
    answer = []
    mean = []
    for s in score:
        mean.append((s[0]+s[1])/2)
    sorted_mean = sorted(mean, reverse=True)
    answer = [sorted_mean.index(rank) + 1 for rank in mean]
    return answer