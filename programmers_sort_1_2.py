from itertools import *
from functools import reduce

def solution(numbers):
    # str_list = list(str(x) for x in numbers)
    # print(str_list)
    
    # list_str = list(map(lambda x : (reduce(lambda x ,y : str(x) + str(y) ,x)), permutations(numbers, len(numbers)) ))
    
    numbers = list(map(str, numbers))
    print("numbers : " , numbers)
    # 문자열의 경우 곱하기를 할 경우 똑같이 복사가 된다
    # sort 경우 key를 통해 기준을 정할 수 있다
    # 3을 곱한 이유는 1000이하의 숫자여 그렇고 
    numbers.sort(key=lambda x: x*3, reverse=True)
    print("numbers2222222 : " , numbers)
    print("numbers33333 : " ,     str(''.join(numbers)))
    
    

    return ''



numbers1 = [6,10,2]
numbers2 = [3, 30, 34, 5, 9]

print("11 :  " , solution(numbers1))
# print("22 " , solution(numbers2))

