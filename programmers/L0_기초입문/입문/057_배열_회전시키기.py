# 배열 회전시키기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120844
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 03. 13. 09:51:02

def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer = [numbers[-1]] + numbers[:-1]
    else:
        answer = numbers[1:] + [numbers[0]]          
    return answer
# [numbers[-1]] 대괄호로 묶는 이유 :
# +를 사용하기 위해서는 데이터 타입이 같아야 함.
# 똑같이 리스트 형태로 만들어준 뒤에 합칠 수 있음