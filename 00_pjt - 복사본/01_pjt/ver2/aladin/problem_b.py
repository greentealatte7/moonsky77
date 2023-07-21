import json
from pprint import pprint


def book_info(book, categories):
    pass
    ids = book['categoryId']
    
    category_names = []
    for id in ids:
        for category in categories:
            if category['id'] == id:
                category_names.append(category['name'])

    result = {
        'id': book['id'],
        'title': book['title'],
        'author' : book['author'],
        'priceSales' : book['priceSales'],
        'description' : book['description'],
        'cover' : book['cover'],
        'categoryName': category_names
        }
    return result

#'author', 'priceSales', 'description', 'cover', 'categoryId'
    # # 여기에 코드를 작성합니다.  
    # # categories_id = book['categories_id']
    # # categories_name = []
    # # for idname in categories :
    # #     if idname in categories_id : 
    # #         categories_name.append('id'['name'])

    # A = check_list['categoryId']
    # B = categories['id']
    # if A == B :
    #     print(categories['name'])

    # check_list = ['id', 'title', 'author', 'priceSales', 'description', 'cover', 'categoryId']
    # book_info = {}
    # for check in check_list :
    #     book_info[check] = book[check]
   

  

    
    # categories = ['id', 'name']
    # cate_info = {}
    # for cate in categories :
    #     cate_info[cate] = categories[cate]
    # return cate_info




 




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
