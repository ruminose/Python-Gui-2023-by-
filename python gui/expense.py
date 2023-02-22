from tkinter import *
from tkinter import ttk
from datetime import datetime

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
def SaveData(even = None):
    expense = v_expense.get()
    amout   = float(v_amount.get())
    timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    data = [expense,amout,timestamp]
    writecsv(data)
    v_expense.set('')
    v_amount.set('')
    E1.focus()

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

header = ['ลำดับ','รายการ','ค่าใช้จ่าย','วัน-เวลา']
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

data = read_csv(file_path)

for i,d in enumerate(data):
    table.insert('','end',values=[i,d[0],d[1],d[2]])


GUI.mainloop()