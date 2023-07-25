# ws_6_2.py

# 아래 함수를 수정하시오.
def get_value_from_dict(me_dict, namee):
    name2 = me_dict.get(namee)
    return name2

my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result) # Alice