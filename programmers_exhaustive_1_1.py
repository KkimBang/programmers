def solution(answers):
    su_po = [[1,2,3,4,5],[2, 1, 2, 3, 2, 4, 2, 5] , [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] ]
    count = [0,0,0]
    answer = []
    
    for i, a in enumerate(answers):
        for r in range(3):
            if su_po[r][i % len(su_po[r])] == a:
                count[r] += 1
                
    for i in range(3):
        if count[i] == sorted(count, reverse=True)[0]:
            answer.append(i + 1)
            
    print([i + 1 for i ,v in enumerate(count) if v == max(count) ]  )
    return answer






answers1 = [1,2,3,4,5]
answers2 = [1,3,2,4,2]

print("result1 : " , solution(answers1))

print("result2 : " , solution(answers2))