
def main():
    """ Создание БД средствами Python """

    import sqlite3

    conn = sqlite3.connect('NikitaP.sqlite')
    cursor = conn.cursor()

    return conn, cursor


def create_table(cursor):
    cursor.execute("""CREATE TABLE book (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'title' TEXT,
    'author' TEXT,
    'year_of_pub' INTEGER) """)
    # Выяснить нужно ли выполнять commit при создании таблицы
    # Не обязательно, таблица будет создана и без commita


def insert_data(conn, cursor):
    cursor.execute("""INSERT INTO book VALUES
    (NULL, 'Фудзи', 'В. Пелевин', '2018')""")
    conn.commit()

    # what is the difference between method above and below
    # which is better and why?
    # cursor.executemany()
    # Метод executemany() использует список в качестве вводных данных, подставляя вместо "?" значения из списка


def close_db():
    global conn
    global cursor

    cursor = None

    conn.close()

def clear_table(conn, cursor, id:int=None, title:str=None):
    """
    Очистка таблицы
    """
    if id:
        cursor.execute(f'DELETE FROM Book WHERE ID={id};')
        print(f'Элемент с id = {id} удален')
    elif title:
        cursor.execute(f'DELETE FROM Book WHERE title=\'{title}\';')
        print(f'Книга с названием {title} удалена из таблицы')
    else:
        cursor.execute('DELETE FROM Book;')
        print('Все данные удалены из таблицы')
    conn.commit()

def delete_table(cursor):
    cursor.execute('DROP TABLE Book')
    print('Таблица удалена')

def print_table(cursor):
    cursor.execute('SELECT * FROM Book')
    print(cursor.fetchall())

def change_element(conn, cursor, id, title='', author='', year_of_pub=''):
    set = []
    if title:
        set.append(f'title = \'{title}\'')
    if author:
        set.append(f'author = \'{author}\'')
    if year_of_pub:
        set.append(f'year_of_pub = {year_of_pub}')
    set = ', '.join(set)
    cursor.execute(f'UPDATE Book SET {set} WHERE id = {id};')
    print(f'Данные книги с id = {id} изменены: ', title, author, year_of_pub)
    conn.commit()

conn, cursor = main()
change_element(conn, cursor, 0, 'Игра Престолов', 'Миссандея У.', 2019)
print_table(cursor)
close_db()
