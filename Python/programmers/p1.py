# 배열 회전, (100/100)


# 모범 답안:
def rotate(arr):
    return arr[-1:] + arr[:-1]

def solution(arrA, arrB):
    arrA_len = len(arrA)
    arrB_len = len(arrB)

    # 길이가 다른 배열은 회전해도 같아질 수 없으므로, early return
    if(arrA_len!=arrB_len):
        return False

    # arrA를 한칸씩 회전하며, arrB와 같은지 확인
    for _ in range(arrA_len):
        if arrA == arrB:
            return True
        arrA = rotate(arrA)
    return False




def rotate(arr):
    tmp = arr.pop(-1)
    arr.insert(0, tmp)
    return arr
        
def solution(arrA, arrB):
    for _ in range(len(arrA)):
        if rotate(arrA) == arrB:
            return True
    answer = False
    return answer

print(solution([7, 8, 10], [10, 7, 8]))