def increase_user(name):
    user = {'name' : name}
    return user


def create_user(name, age, address):
    user = {'name' : name, 'age' : age, 'address' : address}
    return user

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

print(list(map(increase_user, name)))
print(list(map(create_user, name, age, address)))
