# 길거리 가로등 전구


# 모범답안 1:
def solution(l, v):
    v.sort()
    ans = max(v[0], l - v[-1])
    for i in range(1, len(v)):
        ans = max(ans, (v[i] - v[i-1] + 1)//2)
    return ans

# 모범답안 2:
def solution(l, v):    
    n = len(v)
    answer = l
    v.sort()

    left, right = 0, l
    while(left <= right) :
        mid = (left + right) // 2

        # 맨 앞 가로등과 맨 뒤 가로등이 도로의 양 끝을 밝히는지 확인
        if v[0] - mid > 0 or v[n-1] + mid < l :
            left = mid + 1
            continue

        # 나머지 가로등으로 이분 탐색
        flag = False
        for i in range(1, n) :
            if v[i-1] + mid < v[i] - mid :
                flag = True
                break
        if flag :
            left = mid + 1
        else :
            answer = mid 
            right = mid - 1
    return answer












# 100/100
def solution(l, v):
    v.sort()
    Max = 0
    for x in range(len(v)-1):
        if v[x+1]-v[x] > Max:
            Max = abs(v[x]-v[x+1])
    ans = max(Max/2, v[0], l-v[-1])
    if ans%1:
        ans += 1
    return int(ans)

print(solution(15, [15, 5, 3, 7, 9, 14, 0]))





# 정확도 40, 효율성 25 = 65
def solution(l, v):
    v.sort()
    Max = max(v[0], l-v[-1])
    for x in range(len(v)-1):
        if v[x+1]-v[x] > Max:
            Max = abs(v[x]-v[x+1])
    ans = Max/2
    if ans%1:
        ans += 1
    return int(ans)

print(solution(15, [15, 5, 3, 7, 9, 14, 0]))





# 50/100
def solution(l, v):
    v.sort()
    Max = v[0]
    for x in range(len(v)-1):
        if v[x+1]-v[x] > Max:
            Max = abs(v[x]-v[x+1])
    return int(Max/2)+1

print(solution(15, [15, 5, 3, 7, 9, 14, 0]))