from collections import Counter

part1 = ["leo", "kiki", "eden"]
part2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
part3 = ["mislav", "stanko", "mislav", "ana"]
comp1= ["eden", "kiki"]
comp2= ["josipa", "filipa", "marina", "nikola"]
comp3= ["stanko", "ana", "mislav"]


def solution(participant, completion):
    d = dict()
    for p in participant:
        d[p] = d.get(p, 0) + 1
        
    for c in completion:
        d[c] -= 1
        if d[c] == 0:
            del d[c]
        
    return list(d.keys()).pop()

solution(part1, comp1)

solution(part2, comp2)

solution(part3, comp3)

# def solution(participant, completion):
#     print( collections.Counter(participant))
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     print(answer)
#     return list(answer.keys())[0]