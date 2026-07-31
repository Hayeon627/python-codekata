# 이진수 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120885
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 07. 31. 18:22:17

def solution(bin1, bin2):
    answer = []
    carry = 0  # 올림수
    
    b1 = list(bin1)
    b2 = list(bin2)
    
    # 두 이진수 중 한 곳에 글자가 남아있거나, 더해야 할 올림수(carry)가 있다면 계속 반복합니다.
    while b1 or b2 or carry:
        num1 = int(b1.pop()) if b1 else 0
        num2 = int(b2.pop()) if b2 else 0
        total = num1 + num2 + carry
        answer.append(str(total % 2))
        carry = total // 2
    
    answer = ''.join(reversed(answer))
    return answer


# 내장함수
def solution(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:]
