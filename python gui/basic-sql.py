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
        command = 'INSERT INTO expense  VALUES(?,?,?,?)'
        c.execute(command, (None, title, price, date))
    conn.commit()
    print('save')

# insert_expense('เติมน้ำมัน',300,'2023-02-24 20:30')

def view_all_expense():
    with conn:
        command = "SELECT * FROM expense"
        c.execute(command)
        result = c.fetchall()
        # print(result)
    return result
# view_all_expense()

def update_expense(ID, field,newvalue):
    with conn:
        command = 'UPDATE expense SET {} = (?) WHERE ID =(?)'.format(field)
        c.execute(command,([newvalue,ID]))
    conn.commit()
    print('update')

# update_expense(1,'title','ค่าน้ำมันวันก่อน')

def delete_expense(ID):
    with conn:
        command = 'DELETE FROM expense WHERE ID = (?)'
        c.execute(command,([ID]))
        conn.commit()
        print('deleted')


# insert_expense('เติมน้ำมัน',900,'2023-02-24 10:30')
# insert_expense('เติมน้ำมัน',700,'2023-02-24 10:40')
# insert_expense('เติมน้ำมัน',800,'2023-02-24 11:30')

# delete_expense(4)
# delete_expense(5)

# data = view_all_expense()
# print(data[0][1])