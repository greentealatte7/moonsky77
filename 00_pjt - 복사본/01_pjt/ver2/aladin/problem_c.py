import json
from pprint import pprint


def books_info(books, categories):
    # 여기에 코드를 작성합니다.  
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



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))