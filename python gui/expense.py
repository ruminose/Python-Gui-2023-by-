from tkinter import *
from tkinter import ttk
import csv
from datetime import datetime
###############################################################################
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

###############################################################################
GUI = Tk()
GUI.geometry('700x600')
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย')

#Image icons
icon = 'C:\\python gui\\Cat and dog-pana.png'
FONT1 = ('Angsana New',25)
########################################Config TAB 1########################################
Tab = ttk.Notebook(GUI)
Tab.pack(fil=BOTH,expand=1)

T1 = Frame(Tab)
T2 = Frame(Tab)

icon_tab1 = PhotoImage(file='tab1.png')
icon_tab2 = PhotoImage(file='tab2.png')

Tab.add(T1,text='บันทึกค่าใช้จ่าย',image=icon_tab1,compound='top')
Tab.add(T2,text='ประวิติค่าใช้จ่าย',image=icon_tab2,compound='top')



########################################TAB 1########################################
iconimage = PhotoImage(file=icon)
L = Label(T1,image=iconimage)
L.pack()

#ช่องรายการค่าใช้จ่าย

L = Label(T1,text='รายการค่าใช้จ่าย',font = (None,30))
L.pack(pady=5)

v_expense = StringVar()
E1 = ttk.Entry(T1,textvariable = v_expense, font = FONT1)
E1.pack(pady=5)

#ช่องกรอกจำนวนเงินค้าใช้จ่าย

L = Label(T1,text='กรอกจำนวนเงิน(บาท)',font = (None,30))
L.pack(pady=5)

v_amount = StringVar()
E2 = ttk.Entry(T1,textvariable = v_amount, font = FONT1)
E2.pack(pady=5)


#บันทึกข้อมูล

def update_table():
    table.delete(*table.get_children())
    data = view_all_expense()
    for d in data:
        table.insert('','end',values=[d[0],d[1],d[2],d[3]])


def SaveData(even = None):
    expense = v_expense.get()
    amout   = float(v_amount.get())
    timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    data = [expense,amout,timestamp]
    # writecsv(data)
    insert_expense(expense, amout,timestamp)
    v_expense.set('')
    v_amount.set('')
    E1.focus()
    update_table()

E2.bind('<Return>',SaveData)#even = None
E1.bind('<Return>',lambda x: E2.focus()) ## bind โดยไม่ต้องสร้างฟังชั่น

# def Fav1(event=None):
#     v_expense.set('Gunjupro')
#     v_amount.set('230')

#     GUI.bind('<1>',Fav1)

B1 = ttk.Button(T1,text='บันทึก',command=SaveData)
B1.pack(ipady=10,ipadx=20,pady=10)


#FUNCTION#
import csv
def writecsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
       fw = csv.writer(file)
       fw.writerow(data) 

import csv

def read_csv(file_path):
    data = []
    with open(file_path, 'r',encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

# Call the function to read the CSV file
file_path = 'data.csv'
data = read_csv(file_path)

# Print the data
for row in data:
    # print(row)

    read_csv(file_path)       
########################################TAB 2########################################
########################################TAB 2########################################

header = ['ID','รายการ','ค่าใช้จ่าย','วัน-เวลา']
hwidth = [70,300,150,120]

table  = ttk.Treeview(T2,columns=header,show='headings',height=20)
table.pack()

##resize table
style = ttk.Style()
style.configure('TreeView.Heading',font=(None,15))
style.configure('TreeView',font=(None,13),rowheight=30)


# table.column('ลำดับ',width=50)
# table.heading('ลำดับ',text='No.')

for h,w in zip(header,hwidth):
    table.column(h,width=w)
    table.heading(h,text=h)

    # table.insert('','end',values=['A','B','C','D'])

# data = read_csv(file_path)
data = view_all_expense()

for i,d in enumerate(data,start =1):
    table.insert('','end',values=[d[0],d[1],d[2],d[3]])


##Delete data
def delete_data(event):
    select = table.selection()
    print(select)
    select_data = table.item(select)
    print(select_data['values'][0])
    ID = select_data['values'][0]
    delete_expense(ID)
    update_table()

def update_data(event):
    select = table.selection()
    select_data = table.item(select)
    ID = select_data['values'][0]
    title = select_data['values'][1]
    price = select_data['values'][2]
    
    GUI2 =Toplevel()
    GUI2.geometry('500x500')
    GUI2.title('แก้ไขรายการ')

    L = Label(GUI2,text='รายการค่าใช้จ่าย',font = (None,30))
    L.pack(pady=5)

    v_expense2 = StringVar()
    v_expense2.set(title)
    E1 = ttk.Entry(GUI2,textvariable = v_expense2, font = FONT1)
    E1.pack(pady=5)

    #ช่องกรอกจำนวนเงินค้าใช้จ่าย

    L = Label(GUI2,text='กรอกจำนวนเงิน(บาท)',font = (None,30))
    L.pack(pady=5)

    v_amount2 = StringVar()
    v_amount2.set(price)
    E2 = ttk.Entry(GUI2,textvariable = v_amount2, font = FONT1)
    E2.pack(pady=5)
    
    def UpdateData():
        update_expense(ID,'title',v_expense2.get())
        update_expense(ID,'price',float(v_amount2.get()))
        update_table()
        GUI2.destroy() ## Auto close GUI2 if it done

    B1 = ttk.Button(GUI2,text='บันทึก',command=UpdateData)
    B1.pack(ipady=10,ipadx=20,pady=10)


    GUI2.mainloop()

table.bind('<Double-1>',update_data)


table.bind('<Delete>',delete_data) # dont forget 'event' in fucntion



GUI.mainloop()