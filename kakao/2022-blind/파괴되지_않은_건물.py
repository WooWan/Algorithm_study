def solution(board, skills):
    prefix = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    for skill in skills:
        type, skillRange, degree = skill[0], skill[1:5], skill[-1]

        x1,y1,x2,y2 = skillRange

        degree = -degree if type == 1 else degree

        prefix[x1][y1] += degree
        prefix[x2+1][y1] -= degree
        prefix[x1][y2+1] -= degree
        prefix[x2+1][y2+1] += degree

    for i in range(len(board)):
        for j in range(1, len(board[0])):
            prefix[i][j] += prefix[i][j-1]

    for i in range(1, len(board)):
        for j in range(len(board[0])):
            prefix[i][j] += prefix[i-1][j]

    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += prefix[i][j]
            if board[i][j] >= 1:
                count += 1
    return count

solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]	)