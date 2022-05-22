import pymysql
import json


with open('config/mysql.json', 'r') as f:
    mysql_config = json.load(f)


def get_connection(old):
    def new_function(*args, **kwargs):
        conn = pymysql.connect(host=mysql_config['host'],
                               port=mysql_config['port'],
                               user=mysql_config['user'],
                               passwd=mysql_config['password'],
                               db=mysql_config['db'])
        cur = conn.cursor()
        try:
            res = old(cur, *args, **kwargs)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()
            conn.close()
        return res
    return new_function


def list2tuple_str(the_list):
    tuple_str = ''
    for i in the_list:
        tuple_str += (i + ', ')
    return '({})'.format(tuple_str[:-2])


@get_connection
def insert_records(cur, table_name, columns: list, data: list, ignore=False):
    """
    插入多行数据，适用于插入大量数据
    :param cur: param form @get_connection
    :param table_name: the table name in database
    :param columns: a list of the columns names, should be correspond to param 'data'
    :param data: a list of lists, each list contains a line of data
    :param ignore: whether ignore mysql warning
    :return:
    """
    query = 'insert into {} {} values {}'.format(
        'ignore' if ignore else '',
        table_name,
        list2tuple_str(columns),
        list2tuple_str(['%s' for _ in range(len(columns))])
    )
    try:
        row_count = cur.executemany(query, data)
    except Exception as e:
        print(query, data)
        raise e
    return row_count


@get_connection
def insert_record(cur, table_name, data: dict, ignore=False):
    """
    插入单行数据，适用于插入少量数据
    :param cur:
    :param table_name:
    :param data:
    :param ignore:
    :return:
    """
    query = 'insert {} into {} {} values {}'.format(
        'ignore' if ignore else '',
        table_name,
        list2tuple_str(list(data.keys())),
        list2tuple_str(['%s' for _ in range(len(data.keys()))])
    )
    try:
        row_count = cur.execute(query, tuple(data.values()))
    except Exception as e:
        print(query, data)
        raise e
    return row_count


@get_connection
def execute_query(cur, query, *args):
    try:
        row_count = cur.execute(query, tuple(args))
    except Exception as e:
        print(query, *args)
        raise e
    return row_count


delete = execute_query
update = execute_query


@get_connection
def select(cur, query, *args):
    try:
        res = None
        if cur.execute(query, tuple(args)):
            res = cur.fetchall()
    except Exception as e:
        print(query, *args)
        raise e
    return res
