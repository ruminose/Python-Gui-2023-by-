from tkinter import *
from tkinter import ttk #

GUI = Tk()
GUI.geometry('500x500')
GUI.title('โปรแกรมหาร')

L = Label(GUI,text='โปรแกรมหาร',font=('Angsana NEw',30))
L.pack(pady=20)

#################################################################
L = Label(GUI,text='ราคาทั้งหมด(บาท)',font=('Angsana NEw',20))
L.pack(pady=5)

v_total = StringVar()

E1 = ttk.Entry(GUI,textvariable=v_total,font=('Angsana NEw',20))
E1.pack(pady=10)


##################################################################
L = Label(GUI,text='มากันกี่คน',font=('Angsana New',20))
L.pack(pady=5)

v_person = StringVar()

E2 = ttk.Entry(GUI,textvariable=v_person,font=('Angsana New',20))
E2.pack(pady=10)



#################################################################
def Calculate():
    total = float(v_total.get())
    persons = int(v_person.get())
    calc = total / persons

    print('Split (bath/person): ',calc)
    text = 'รวมทั้งหมด {:,.2f} บาท จำนวน {} คน ({:.2f} บาทต่อคน)'.format(total,persons,calc)
    v_result.set(text)

B1 = ttk.Button(GUI,text='Calculate',command=Calculate)
B1.pack(pady=10,ipadx=20,ipady=10)

##################################################################
v_result = StringVar()
result = ttk.Label(GUI,textvariable=v_result,font=('Angsana New',20),foreground='green')
result.pack(pady=20)



GUI.mainloop()