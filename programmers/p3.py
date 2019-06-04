# 2d list, bingo


# 모범 답안:
def solution(board, nums):
    n = len(board)
    vertical = [0 for _ in range(n)]
    horizontal = [0 for _ in range(n)]
    lu_diag = 0
    ru_diag = 0

    # 탐색을 O(1)로 하기 위해 nums를 set 자료구조로 변환
    nums = set(nums)
    for p in range(n):
        for q in range(n):
            if board[p][q] in nums:
                horizontal[q]+=1
                vertical[p]+=1
                if p == q:
                    lu_diag+=1
                if p + q == n - 1:
                    ru_diag += 1

    cnt = 0
    cnt += vertical.count(n)
    cnt += horizontal.count(n)
    if lu_diag == n:
        cnt += 1
    if ru_diag == n:
        cnt += 1
    return cnt











# accuracy 70, efficiency 0 = 70/100
def solution(board, nums):
    n = len(board)
    for y in range(n):
        for x in range(n):
            if board[y][x] in nums:
                board[y][x] = 0
    board_t = list(zip(*board))
    sumlist = []
    for y in range(n):
        sumlist.append(sum(board[y][:]))
        sumlist.append(sum(board_t[y][:]))
    diag1, diag2 = 0, 0
    for i in range(n):
        diag1 += board[i][i]
        diag2 += board[n-1-i][i]
    sumlist.extend([diag1, diag2])
    return sumlist.count(0)


print(solution([[11, 13, 15, 16], [12, 1, 4, 3], [10, 2, 7, 8], [5, 14, 6, 9]], [14, 3, 2, 4, 13, 1, 16, 11, 5, 15]))