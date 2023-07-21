import json
from pprint import pprint



def book_info(book):
    pass
    # 여기에 코드를 작성합니다.  
    # check_list = ['id', 'title', 'author', 'priceSales', 'description', 'cover', 'categoryId']
    # book_info = {}
    # for check in check_list :
    #     book_info[check] = book[check]
    # return book_info
   
    
    ids = book
    

    result = {
     'id': book['id'],
        'title': book['title'],
        'author' : book['author'],
        'priceSales' : book['priceSales'],
        'description' : book['description'],
        'cover' : book['cover'],
        'categoryId' : book['categoryId']
    }
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)
    
    pprint(book_info(book))
