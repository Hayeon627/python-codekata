# 캐릭터의 좌표
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120861
# 알고리즘: 기초
# 작성자: 김하연
# 작성일: 2026. 08. 01. 16:20:59

def solution(keyinput, board):
    x, y = 0, 0
    max_x = board[0] // 2
    max_y = board[1] // 2
    move = {'up':(0, 1), 'down':(0, -1), 'left':(-1, 0), 'right':(1, 0)}
    
    for key in keyinput:
        dx, dy = move[key]
        if -max_x <= x + dx <= max_x and -max_y <= y + dy <= max_y:
            x += dx
            y += dy
    
    answer = [x, y]
    return answer