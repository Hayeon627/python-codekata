# 다항식 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120863
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 06. 05:01:51

def solution(polynomial):
    answer = ''
    x_sum = 0
    n_sum = 0
    numlist = polynomial.split(' ')
    
    for a in numlist:
        if 'x' in a:
            if a == 'x':
                x_sum += 1
            else:
                x_sum += int(a[:-1])
        elif a != '+':
            n_sum += int(a)
            
    if x_sum == 1:
        if n_sum > 0:
            answer = 'x + ' + str(n_sum)
        else:
            answer = 'x'
    elif x_sum > 1:
        if n_sum > 0:
            answer = str(x_sum) + 'x + ' + str(n_sum)
        else:
            answer = str(x_sum) + 'x'
    else:
        answer = str(n_sum)

    return answer


# 더 효율적인 방법
def solution(polynomial):
    x_sum = 0
    n_sum = 0
    
    # 1. 계산부 (공백 제거 후 '+' 기준으로 나누면 연산자 처리가 필요 없어짐)
    for term in polynomial.replace(' ', '').split('+'):
        if 'x' in term:
            x_sum += 1 if term == 'x' else int(term[:-1])
        else:
            n_sum += int(term)
            
    # 2. 출력 조립부 (if-else 분기를 배열과 join으로 단일화)
    result = []
    if x_sum:
        result.append("x" if x_sum == 1 else f"{x_sum}x")
    if n_sum:
        result.append(str(n_sum))
        
    return " + ".join(result) if result else "0"
