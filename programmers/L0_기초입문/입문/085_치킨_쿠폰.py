# 치킨 쿠폰
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120884
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 04. 17:19:39

def solution(chicken):
    answer = 0
    while chicken >= 10:
        coupon = chicken // 10
        answer += coupon
        chicken = coupon + (chicken % 10)
    return answer