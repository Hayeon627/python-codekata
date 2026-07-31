# 영어가 싫어요
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120894
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 07. 31. 18:30:31

def solution(numbers):
    answer = 0
    num_dict = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}
    for word, num in num_dict.items():
        numbers = numbers.replace(word, num)
    answer = int(numbers)
    return answer