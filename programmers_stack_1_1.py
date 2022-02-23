from collections import deque
from functools import reduce

def solution(p, s):
    answer = []
    q = deque(map(lambda x , y: int((100 - x) / y)  + 1 if (100 - x) % y > 0 else int((100 - x) / y) , p, s ))
    f = 0 ; i = 0
    while q:
        n = q.popleft()
        if f >= n:
            i += 1
        else:
            if i is not 0:
                answer.append(i)
                i = 0
            f = n
            q.appendleft(n)
    answer.append(i)
    return answer

# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         print(" p : ", p , " s : " , s)
#         print("?????? : ' " , (p-100)//s)
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]



p = [93, 30, 55]
s = [1, 30, 5]
print("result1 : ",  solution(p ,s))


# p = [95, 90, 99, 99, 80, 99]
# s = [1, 1, 1, 1, 1, 1]

# print("result2 : ",  solution(p ,s))
