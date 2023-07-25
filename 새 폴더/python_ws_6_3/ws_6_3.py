# ws_6_3.py

# 아래 함수를 수정하시오.
def intersection_sets(set1, set2):
    set7 = set1.intersection(set2)
    return set7

result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result) # {3}