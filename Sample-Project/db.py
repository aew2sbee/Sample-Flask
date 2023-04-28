import sqlite3

DATABASE = 'database.db'

def create_books_table():
    con = sqlite3.connect(DATABASE)
    CREATE_SQL = "CREATE TABLE IF NOT EXISTS books (title, price, arrival_day)"
    print('CREATE_SQL')
    con.execute(CREATE_SQL)
    con.close()
