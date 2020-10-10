import requests


def get_user():
    """For testing geting user on id"""
    url = r'http://127.0.0.1:5000/get_user'
    data = {"id_user": "2"}
    a = requests.post(url, data=data)
    print(a.content)


def get_order_user():
    """For testing geting order 
    of user on id_user.
    
    """
    url = r'http://127.0.0.1:5000/get_order_user'
    data = {"id_user": "1"}
    a = requests.post(url, data=data)
    print(a.content)


def get_shop():
    """For testing geting assortiment 
    shop on id_shop.
    
    """
    url = r'http://127.0.0.1:5000/get_shop'
    data = {"id_shop": "1"}
    a = requests.post(url, data=data)
    print(a.content)


def add_new_order():
    """For testing adding 
    new order.
    
    """
    url = r'http://127.0.0.1:5000/add_new_order'
    data = {"id_shop": "2",
            "id_user": "1",
            "id_book": "2",
            "book_quantity": "2"}


    a = requests.put(url, data=data)
    print(a.content)


def main():
    get_user()
    get_order_user()
    get_shop()
    add_new_order()


if __name__ == "__main__":
    main()
