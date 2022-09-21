import sqlite3
import os

from typing import List


def execute_query(query_sql: str) -> List:
    '''
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    '''
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql).fetchall()
    connection.close()
    return result


def unwrapper(records: List) -> None:
    '''
    Функция для вывода результата выполнения запроса
    :param records: список ответа БД
    '''
    for record in records:
        print(*record)


def get_employees() -> List:
    '''
    Получение всех записей из таблицы employees
    :return: список записей
    '''
    query_sql = '''
        SELECT *
          FROM employees;
    '''
    return execute_query(query_sql)


# unwrapper(get_employees())


def get_filtered_customers(city=None,
                           state=None) -> List:
    '''
    Возвращает клиентов, отфильтрованных по городу и штату
    :param city: город проживания, строка
    :param state: штат проживания, строка
    :return: список клиентов
    '''
    query_sql = '''
        SELECT *
          FROM customers
    '''
    if city and state:
        query_sql += f" WHERE City = '{city}' AND State = '{state}';"
    elif city:
        query_sql += f" WHERE City = '{city}';"
    elif state:
        query_sql += f" WHERE State = '{state}';"
    return execute_query(query_sql)


# unwrapper(get_filtered_customers(state='SP', city='São Paulo'))


def get_unique_customers_by_sql() -> List:
    query_sql = '''
        SELECT distinct FirstName
          FROM customers;
    '''
    return execute_query(query_sql)


# unwrapper(get_unique_customers_by_sql())


def get_unique_customers_by_python() -> List:
    query_sql = '''
            SELECT distinct FirstName
              FROM customers;
    '''
    records = execute_query(query_sql)
    unique_names = set()
    for record in records:
        unique_names.add(record[0])
    return list(unique_names)


# unwrapper(get_unique_customers_by_python())
