# main.py

# 아래 함수를 수정하시오.
def find_min_max(mm):
    list_m = list(mm)
    list_s = list_m.sort()
    a= min(list_m)
    b= max(list_m)
    result = a, b
    return result

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)