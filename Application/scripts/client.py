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
    data = {"id_user": "3"}
    a = requests.post(url, data=data)
    print(a.content)



def main():
    get_user()


if __name__ == "__main__":
    main()
