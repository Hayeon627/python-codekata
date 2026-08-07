# 최빈값 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120812
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 07. 13:25:31

def solution(array):
    answer = 0
    cnt_dict = {}
    
    for i in array:
        cnt_dict[i] = cnt_dict.get(i, 0) + 1
    max_freq = max(cnt_dict.values())
    
    freq_count = 0
    for j in cnt_dict:
        if cnt_dict[j] == max_freq:
            answer = j
            freq_count += 1
    if freq_count > 1:
        answer = -1
        
    return answer


def solution(array):
    # 1. 집합(set)을 이용해 중복을 제거한 숫자 목록을 만듦
    unique_elements = list(set(array))
    
    # 2. 각 숫자의 등장 횟수를 기준으로 내림차순 정렬 (많이 나온 순서대로)
    unique_elements.sort(key=lambda x: array.count(x), reverse=True)
    
    # 3. 최빈값이 여러 개인지 확인 (-1 반환)
    if len(unique_elements) > 1 and array.count(unique_elements[0]) == array.count(unique_elements[1]):
        return -1
        
    # 4. 가장 많이 나온 숫자 반환
    return unique_elements[0]