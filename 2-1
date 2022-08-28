def solution(L, x): 
    # L = [20, 37, 58, 72, 91], x = 65
    if L[0] > x:
        L.insert(0,x)
        return L

    if L[-1] < x:
        L.insert(len(L),x)
        return L

    
    for i in range (0, len(L)):
        if L[i] > x:

            L.insert(i,x)
            answer = L
            break
        
            


    return answer
