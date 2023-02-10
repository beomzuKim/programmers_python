# 피보나치순열 구하기 반복적 방법
def solution(x):
    
    f = [0, 1]
    for i in range(0, x):
        add = f[i+1] + f[i]
        f.append(add)
        
    answer = f[x]
    return answer
