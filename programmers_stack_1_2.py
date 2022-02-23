def solution(p, l):
    r = [0] * len(p)
    r[l] = 1
    v = []
    
    while p :
        m = max(p)
        n = p.pop(0)
        r_n = r.pop(0)
        if m is n:
            v.append(r_n)
        else :
            p.append(n)
            r.append(r_n)
            
    return v.index(1) + 1

# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     print("queue : ", queue)
#     while True:
#         cur = queue.pop(0)
#         print("cur : ", cur)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer


p = [2, 1, 3, 2]
print("result : " , solution( p , 2))

p = [1, 1, 9, 1, 1, 1]
print("result : " , solution( p , 0))