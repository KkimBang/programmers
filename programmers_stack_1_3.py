def solution(length, weight, trucks):
    l = [0] * length
    delay = 0
    bridge = 0
    
    while trucks:
        t = trucks.pop(0)
        bridge += t - l.pop()
        if bridge > weight :
            l.append(0)
            trucks.insert(0, t)
            bridge -= t
        else:
            l.append(t)
        l.append(l.pop(0))
        delay += 1
    return length + delay


print("result  : " ,solution(2, 10 ,[7,4,5,6]))
print("result  : "  ,solution(100, 100 ,[10]))
print("result  : " , solution(100, 100 ,[10,10,10,10,10,10,10,10,10,10]))