# 숨어있는 숫자의 덧셈 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120864
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 07. 28. 04:47:48

def solution(my_string):
    answer = 0
    temp = ""  # 연속된 숫자를 저장할 임시 문자열
    
    for char in my_string:
        if char.isdigit():  # 숫자라면 임시 문자열에 추가
            temp += char
        else:               # 문자라면 지금까지 쌓인 숫자를 더함
            if temp:
                answer += int(temp)
                temp = ""   # 임시 문자열 초기화
                
    if temp:  # 문자열이 숫자로 끝났을 경우 마지막 숫자 처리
        answer += int(temp)
        
    return answer
