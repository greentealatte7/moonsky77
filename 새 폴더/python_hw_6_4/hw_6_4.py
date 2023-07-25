# hw_6_4.py

# 아래 함수를 수정하시오.
def add_item_to_dict(dictionary, add_1, add_2):
    new_dict = dictionary.copy()
    new_dict.setdefault(add_1, add_2)
    return new_dict

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)