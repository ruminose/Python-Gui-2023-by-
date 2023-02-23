import sqlite3

conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS expense (
         ID INTEGER PRIMARY KEY AUTOINCREMENT,
         title TEXT,
         price REAL,
         date TEXT)""")


def insert_expense(title, price, date):
    with conn:
        command = 'INSERT INTO expense VALUES(?,?,?,?)'
        c.execute(command, (None, title, price, date))
    conn.commit()
    print('save')

    insert_expense('เติมน้ำมัน',300,'2023-02-20:30')
    insert_expense('เติมน้ำมัน',300,'2023-02-20:30')
    insert_expense('เติมน้ำมัน',300,'2023-02-20:30')

# def view_all_expense():
#     with conn:
#         command = "SELECT * FROM expense"
#         c.execute(command)
#         result = c.fetchall()
#         print(result)
#     return result
# view_all_expense()