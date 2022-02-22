from collections import Counter
from functools import reduce


def solution(clothes):
    answer = 0
    d = {}
    print("!! : ", [y for x, y in clothes])
    cnt = Counter([kind for name, kind in clothes])
    print("cnt : ", cnt.values())
    result = reduce(lambda x, y: x * (y+1), cnt.values(), 1) - 1
    print("result : ", result)
    # for item in clothes:
    #     if item[1] not in d:
    #         d[item[1]] = [item[0]]
    #     else:
    #         d[item[1]].append(item[0])
    # print("d : ", d)
    # l = []
    # for key, value in d.items():
    #     for i in range(len(d.items())):
    #         for item in value:
    #             l.append(item)
    return answer

# def solution(clothes):
#     clothes_type = {}

#     for c, t in clothes:
#         if t not in clothes_type:
#             clothes_type[t] = 2
#         else:
#             clothes_type[t] += 1
#     print("clothes_type : ", clothes_type)
#     cnt = 1
#     for num in clothes_type.values():
#         cnt *= num

#     return cnt - 1


clothes1 = [["yellowhat", "headgear"], [
    "bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["green", "pants"]]
clothes2 = [["crowmask", "face"], [
    "bluesunglasses", "face"], ["smoky_makeup", "face"]]

r = solution(clothes1)
print("result : ", r)
# r = solution(clothes2)
# print("result : ", r)
