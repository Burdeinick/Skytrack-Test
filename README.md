# Skytrack-Test
API, отображающее мою способность(или неспособность) писать элементарный "Back-End код".

## Что такое Skytrack-Test?
Это API имитирующее некоторую функциональную часть онлайн магазинов по заказам книг.
***
## Как начать:

Если необходимо, изменить значения host, port, сделать это можно в конфигурационном файле `'Application/config.json'`.
По умолчанию данные параметры выставлены в `"host": "127.0.0.1"`, a `"port": "5000"`.

1. Установите зависимости: `$ pip3 install -r requirements.txt`.
2. Запустите команды в bash: 

   2.1. Накат тестовой БД: `$ make build`.

   2.2. Запуск сервера: `$ make run`.
***
## Пример взаимодействия с API:
Здесь будут приведены примеры запросов со стороны клиента к данному API. Данные запросы можно найти в `'Application/scripts/client/client.py'`.

Таблицы БД по умолчанию заполнены некоторыми данными для возможности протестировать API.

Таблица User:
```
(id_user, name, surname, fathers_name, email)
(1, 'Bob', 'Smith', 'Viktorovich', 'bo@ya.ru'),
(2, 'Kop', 'Johnson', 'Alexandrovich', 'ko@ya.ru'),
(3, 'Rob', 'Miller', 'Yurievich', 'ro@ya.ru')
```
Таблица Book:
```
(id_book, name, author, isbn)
(1, 'Fahrenheit 451', 'Ray Bradbury', '700-5-699-12014-7'),
(2, 'The Sea Wolf', 'Jack London', '800-5-699-12014-7'),
(3, 'Essays', 'Ralph Waldo Emerson', '900-5-699-12014-7')
```
Таблица Shop:
```
(id_shop, name, address, post_code)
('Beru', 'California Springs, CA 92926 USA', '140130'),
('Ozon', 'Residence of the Russian Ambassador to the U.S. 6', '150120'),
('AliExpress', 'University of Cambridge 12', '130110')
```
Таблица Assortiment:

Данная таблица была созданна для возможности обображать ассортимент конкретного магазина.
```
(id_assortiment, id_book, id_shop)
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 2, 2),
(5, 2, 3),
(6, 3, 1)
```
Таблица OrderAll:
```
(id_order_all, reg_data, id_user)
(1, CURRENT_TIMESTAMP, 2),
(1, CURRENT_TIMESTAMP, 2),
(1, CURRENT_TIMESTAMP, 3)
```
Таблица OrderItem:
```
(id_OrderItem, book_quantity, id_order_all, id_book, id_shop)
(1, 1, 2, 3, 3),
(2, 2, 3, 1, 1),
(3, 3, 1, 1, 1)
```

Получение данных пользователя:
```
def get_user():
    """For testing geting user on id"""
    url = r'http://127.0.0.1:5000/get_user'
    data = {"id_user": "2"}
    a = requests.post(url, data=data)
    print(a.content)
```

Просмотр истории заказов пользователя:
```
def get_order_user():
    """For testing geting order 
    of user on id_user.
    
    """
    url = r'http://127.0.0.1:5000/get_order_user'
    data = {"id_user": "1"}
    a = requests.post(url, data=data)
    print(a.content)
```

Добавление нового заказа:
```
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
```

Просмотр ассортимента определенного магазина:
```
def get_shop():
    """For testing geting assortiment 
    shop on id_shop.
    
    """
    url = r'http://127.0.0.1:5000/get_shop'
    data = {"id_shop": "1"}
    a = requests.post(url, data=data)
    print(a.content)
```
