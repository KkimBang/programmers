# def solution(phone_book):
#     answer = True
    
#     d = dict()
    
#     for num in phone_book:
#         d[num] = d.get(num, len(num))
    
#     # print( d.items())
    
#     for index, value in enumerate(d.items()):
#         # print(f"i : {index} , v : {value}")
#         for inner_index, inner_value in enumerate(d.items()):
#             if index == inner_index:
#                 continue;
#             else:
#                 if inner_value[1] > value[1]:
#                     str = inner_value[0][0: value[1]]
#                     if value[0] == str:
#                         answer = False
#     return answer
# import operator
# def solution(phone_book):
#     answer = True
    
#     d = dict()
#     l = list()
    
#     for num in phone_book:
#         d[num] = d.get(num, len(num))
        
#     sd = sorted(d.items(), key=operator.itemgetter(0))
#     sorted_list = list()
#     print(sd)
#     for key in d.keys():
#         sorted_list.append(key[0:sd[0][1]])
#     print(sorted_list)
#     if "119" in sorted_list:
#         print("yes!!")
    
#     # for index, value in enumerate(d.items()):
#     #     # print(f"i : {index} , v : {value}")
#     #     for inner_index, inner_value in enumerate(d.items()):
#     #         if index == inner_index:
#     #             continue;
#     #         else:
#     #             if inner_value[1] > value[1]:
#     #                 str = inner_value[0][0: value[1]]
#     #                 if value[0] == str:
#     #                     answer = False
#     return answer


def solution(phone_book):
    answer = True
    hash_map = {}
    
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    print("  hash_map : " ,   hash_map)
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            print("temp : " ,temp)
            if temp in hash_map and temp != phone_number:
                answer = False
    
    return answer

phone_book1 = ["119", "97674223", "1195524421"]
phone_book2 = ["123","456","789"]
phone_book3 = ["12","123","1235","567","88"]
r = solution(phone_book1)
print("result : " , r)
# r =solution(phone_book2)
# print("result : " , r)
# r =solution(phone_book3)
# print("result : " , r)