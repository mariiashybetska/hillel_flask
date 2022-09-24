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
    connection.commit()
    return result

def unwrapper(records: List) -> None:
    '''
    Функция для вывода результата выполнения запроса
    :param records: список ответа БД
    '''
    return '\n'.join(map(str, records))





def get_filtered_customers(city, state) -> List:
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
    return unwrapper(execute_query(query_sql))



def get_unique_customers_by_sql(name) -> List:
    query_sql = f'''
        SELECT FirstName, COUNT(*) FROM customers WHERE FirstName = '{name}' GROUP BY FirstName;
    '''
    return unwrapper(execute_query(query_sql))

def get_sum_of_invoice_items() -> List:
    query_sql = '''
        SELECT SUM(UnitPrice * Quantity) as sum FROM invoice_items;
    '''
    return unwrapper(execute_query(query_sql))

