from functools import reduce

def solution(numbers):
    num_list = [str(n) for n in numbers]
    result = []
    visited = [0] * len(num_list)

    combi(0, [], num_list, result,visited )
    result = set(map(int, result))
    answer = 0
   
    for num in result:
        if chk_prime(num): 
            answer += 1 
    return answer

def chk_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
            
def combi(cnt, stack, list, result, visited):
    if cnt == len(list):
        return
    
    for i, v in enumerate(list):
        if visited[i] == 1:
            continue
        stack.append(v)
        result.append(reduce(lambda x,y : str(x)+str(y) , stack , ''))
        visited[i] = 1
        
        combi(cnt + 1, stack, list, result, visited)
        stack.pop()
        visited[i] = 0


numbers1 = "1231"

print("1 : " , solution(numbers1))