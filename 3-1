# 이진탐색 구현
def solution(L, x):
    
    low, up = 0, len(L) - 1
    idx = -1
    
    while low <= up:
        mid = (low + up) // 2
        if L[mid] == x:
            idx = mid
            break
        elif L[mid] < x:
            low = mid + 1
        elif L[mid] > x:
            up = mid - 1
    
    return idx
