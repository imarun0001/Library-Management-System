from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import tkcalendar
from tkcalendar import DateEntry
import tkinter
import mysql.connector as mysql
conn=mysql.connect(host="localhost",user="root",password="Arun@2001",database="library")

def check():
    g_user=user1.get()
    g_pas=pas1.get()
    if g_user=='':
        message=tkinter.Message(root,text='Fill the empty field!!!                   ',fg="red",bg="white",width=200)
        message.place(x=250,y=237)
    else:
        store=[]
        sql=('select username from login')
        c=conn.cursor()
        c.execute(sql,)
        res=c.fetchall()
        for i in res:
            i[0]
            store.append(i[0])
        if(g_user in store):
            sql=('select password from login where username=%s')
            data=(g_user,)
            c=conn.cursor()
            c.execute(sql,data)
            k=c.fetchone()
            db_pas=k[0]
            if g_pas==db_pas:
                message=tkinter.Message(root,text="                                                   ",bg="white",width=500)
                message.place(x=250,y=237)
                show=messagebox.showinfo("LOGIN","Login Successful!!!")
                option()
            elif g_pas=='':
                message=tkinter.Message(root,text='Fill the empty field!!!                   ',fg="red",bg="white",width=200)
                message.place(x=250,y=237)
            else:
                message=tkinter.Message(root,text='Wrong Username/Password!!!   ',fg="red",bg="white",width=200)
                message.place(x=250,y=237)
        elif g_pas=='':
                message=tkinter.Message(root,text='Fill the empty field!!!                   ',fg="red",bg="white",width=200)
                message.place(x=250,y=237)
        else:
            message=tkinter.Message(root,text='Wrong Username/Password!!!   ',fg="red",bg="white",width=200)
            message.place(x=250,y=237)

def signup():
    global root1
    root1=tkinter.Toplevel()
    root1.title('SIGN UP')
    root1.geometry("678x452+310+150")
    bg=ImageTk.PhotoImage(file="photo3.jpeg")
    tkinter.Label(root1,image=bg).place(x=0,y=0)
    tkinter.Frame(root1,width=270,height=300,bg="white").place(x=200,y=50)
    tkinter.Label(root1,text='Sign Up',font=("Microsoft Yahei UI light",17,"bold"),width=10,bg="white",fg="medium blue").place(x=263,y=60)
    tkinter.Label(root1,text='Username',fg="black",bg="white",font=("Cambria",12)).place(x=250,y=118)
    tkinter.Label(root1,text='Password',fg="black",bg="white",font=("Cambria",12)).place(x=250,y=182)
    tkinter.Label(root1,text='Confirm Password',fg="black",bg="white",font=("Cambria",12)).place(x=250,y=247)
    tkinter.Frame(root1,width=175,height=2,bg="black").place(x=250,y=167)
    tkinter.Frame(root1,width=175,height=2,bg="black").place(x=250,y=231)
    tkinter.Frame(root1,width=175,height=2,bg="black").place(x=250,y=296)
    global user2
    global pas22
    global pas2
    user2=tkinter.StringVar()
    pas22=tkinter.StringVar()
    pas2=tkinter.StringVar()
    tkinter.Entry(root1,textvariable=user2,width=25,border=0,fg="black",bg="white",font=("Microsoft Yahei UI light",10,"bold")).place(x=250,y=146)
    tkinter.Entry(root1,textvariable=pas22,show='*',width=25,border=0,fg="black",bg="white",font=("Microsoft Yahei UI light",10,"bold")).place(x=250,y=210)
    tkinter.Entry(root1,textvariable=pas2,show='*',width=25,border=0,fg="black",bg="white",font=("Microsoft Yahei UI light",10,"bold")).place(x=250,y=274)
    confirm=tkinter.Button(root1,text='Register',bg="medium blue",fg="white",width=10,activebackground="green",font=("Microsoft Yahei UI light",11),command=confirm_s)
    confirm.place(x=200,y=374)
    confirm.config(fg="white")
    logout1=tkinter.Button(root1,text='Login Page',bg="medium blue",fg="white",width=10,font=("Microsoft Yahei UI light",11),command=root1.destroy)
    logout1.place(x=370,y=374)
    logout1.config(fg="white")
    root1.mainloop()

def confirm_s():
    s_user=user2.get()
    s_pas=pas2.get()
    s1_pas=pas22.get()
    if s_user=='' or s_pas=='' or s1_pas=='':
        message=tkinter.Message(root1,text='Fill the empty field!!!                   ',fg="red",bg="white",width=200)
        message.place(x=250,y=300)
    elif s_user=='' and s_pas=='' and s1_pas=='':
        message=tkinter.Message(root1,text='Fill the empty field!!!                   ',fg="red",bg="white",width=200)
        message.place(x=250,y=300)
    else:
        store1=[]
        sql=('select username from login')
        c=conn.cursor()
        c.execute(sql,)
        res=c.fetchall()
        for i in res:
            i[0]
            store1.append(i[0])
        if(s_user in store1):
            message=tkinter.Message(root1,text='Username Already Exist!!!                     ',fg="red",bg="white",width=200)
            message.place(x=250,y=300)
        elif(s_pas==s1_pas):
            b=conn.cursor()
            sq='insert into login values(%s,%s)'
            dat=(s_user,s_pas)
            b.execute(sq,dat)
            conn.commit()
            message=tkinter.Message(root1,text='Registered Successfully!!!                      ',fg="green",bg="white",font=("Cambria",10,"bold"),width=200)
            message.place(x=250,y=300)
        else:
            message=tkinter.Message(root1,text='Password Mismatch!!!                      ',fg="red",bg="white",font=("Cambria",10),width=200)
            message.place(x=250,y=300)

def forget():
    global root2
    root2=tkinter.Toplevel()
    root2.title('CHANGE PASSWORD')
    root2.geometry("678x452+310+150")
    bg=ImageTk.PhotoImage(file="photo3.jpeg")
    tkinter.Label(root2,image=bg).place(x=0,y=0)
    tkinter.Frame(root2,width=270,height=300,bg="white").place(x=200,y=50)
    tkinter.Label(root2,text='Set Password',font=("Microsoft Yahei UI light",17,"bold"),width=10,bg="white",fg="medium blue").place(x=263,y=60)
    tkinter.Label(root2,text='Old Username',fg="black",bg="white",font=("Cambria",12)).place(x=250,y=118)
    tkinter.Label(root2,text='New Password',fg="black",bg="white",font=("Cambria",12)).place(x=250,y=182)
    tkinter.Label(root2,text='Confirm Password',fg="black",bg="white",font=("Cambria",12)).place(x=250,y=247)
    tkinter.Frame(root2,width=175,height=2,bg="black").place(x=250,y=167)
    tkinter.Frame(root2,width=175,height=2,bg="black").place(x=250,y=231)
    tkinter.Frame(root2,width=175,height=2,bg="black").place(x=250,y=296)
    global user3
    global pas33
    global pas3
    user3=tkinter.StringVar()
    pas33=tkinter.StringVar()
    pas3=tkinter.StringVar()
    tkinter.Entry(root2,textvariable=user3,width=25,border=0,fg="black",bg="white",font=("Microsoft Yahei UI light",10,"bold")).place(x=250,y=146)
    tkinter.Entry(root2,textvariable=pas33,show='*',width=25,border=0,fg="black",bg="white",font=("Microsoft Yahei UI light",10,"bold")).place(x=250,y=210)
    tkinter.Entry(root2,textvariable=pas3,show='*',width=25,border=0,fg="black",bg="white",font=("Microsoft Yahei UI light",10,"bold")).place(x=250,y=274)
    confirm=tkinter.Button(root2,text='Submit',bg="medium blue",fg="white",width=10,activebackground="green",font=("Microsoft Yahei UI light",11),command=confirm_s1)
    confirm.place(x=200,y=374)
    confirm.config(fg="white")
    logout1=tkinter.Button(root2,text='Login Page',bg="medium blue",fg="white",width=10,font=("Microsoft Yahei UI light",11),command=root2.destroy)
    logout1.place(x=370,y=374)
    logout1.config(fg="white")
    root2.mainloop()

def confirm_s1():
    c_user=user3.get()
    c_pas=pas3.get()
    c1_pas=pas33.get()
    if c_user=='' or c_pas=='' or c1_pas=='':
        message=tkinter.Message(root2,text='Fill the empty field!!!                     ',fg="red",bg="white",width=200)
        message.place(x=250,y=300)
    elif c_user=='' and c_pas=='' and c1_pas=='':
        message=tkinter.Message(root2,text='Fill the empty field!!!                     ',fg="red",bg="white",width=200)
        message.place(x=250,y=300)
    else:
        store11=[]
        sql=('select username from login')
        c=conn.cursor()
        c.execute(sql,)
        res=c.fetchall()
        for i in res:
            i[0]
            store11.append(i[0])
        if(c_user not in store11):
            message=tkinter.Message(root2,text='Username Not Exist!!!                      ',fg="red",bg="white",width=200)
            message.place(x=250,y=300)
        elif(c_pas==c1_pas):
            b=conn.cursor()
            sq='update login set password=%s where username=%s'
            dat=(c_pas,c_user)
            b.execute(sq,dat)
            conn.commit()
            message=tkinter.Message(root2,text='Password Changed Successfully!!!                      ',fg="green",bg="white",font=("Cambria",9,"bold"),width=200)
            message.place(x=242,y=300)
        else:
            message=tkinter.Message(root2,text='Password Mismatch!!!                      ',fg="red",bg="white",font=("Cambria",10),width=200)
            message.place(x=250,y=300)

def view():
    w1.config(state=NORMAL)
    w2.config(state=NORMAL)
    w3.config(state=DISABLED)
    w4.config(state=NORMAL)
    w5.config(state=NORMAL)
    w6.config(state=NORMAL)
    w7.config(state=NORMAL)
    w8.config(state=NORMAL)
    w9.config(state=NORMAL)
    submit_s.config(state=DISABLED)
    cust_id.set('-----------------------------')
    b_name.set('-----------------------------')
    i_date.set('-----------------------------')
    b_add.set('-----------------------------')
    b_code.set('-----------------------------')
    a_name.set('-----------------------------')
    arn_book.set('-----------------------------')
    e1.config(state='disabled')
    e2.config(state='disabled')
    e3.config(state='disabled')
    e4.config(state='disabled')
    e5.config(state='disabled')
    e6.config(state='disabled')
    e7.config(state='disabled')
    tkinter.Message(r,text="                                                                            ",font=("Courier New",10),width=400,bg="white",fg="green").place(x=682,y=315)
    for item in tree1.get_children():
        tree1.delete(item)
    for itemm in tree.get_children():
        tree.delete(itemm)
    a=('select * from books')
    c=conn.cursor()
    c.execute(a)
    disp=c.fetchall()
    for i in disp:
        bcode=i[0]
        bname=i[1]
        avbook=i[2]
        auth=i[3]
        tree.insert('','end',text="1",values=(bcode,bname,avbook,auth))
        
def issued():
    w1.config(state=NORMAL)
    w2.config(state=NORMAL)
    w3.config(state=NORMAL)
    w4.config(state=DISABLED)
    w5.config(state=NORMAL)
    w6.config(state=NORMAL)
    w7.config(state=NORMAL)
    w8.config(state=NORMAL)
    w9.config(state=NORMAL)
    submit_s.config(state=DISABLED)
    cust_id.set('-----------------------------')
    b_name.set('-----------------------------')
    i_date.set('-----------------------------')
    b_add.set('-----------------------------')
    b_code.set('-----------------------------')
    a_name.set('-----------------------------')
    arn_book.set('-----------------------------')
    e1.config(state='disabled')
    e2.config(state='disabled')
    e3.config(state='disabled')
    e4.config(state='disabled')
    e5.config(state='disabled')
    e6.config(state='disabled')
    e7.config(state='disabled')
    tkinter.Message(r,text="                                                                        ",font=("Courier New",10),width=400,bg="white",fg="green").place(x=682,y=315)
    for item in tree.get_children():
        tree.delete(item)
    for itemm in tree1.get_children():
        tree1.delete(itemm)
    a=('select * from issue')
    c=conn.cursor()
    c.execute(a)
    disp=c.fetchall()
    for i in disp:
        cust_idd=i[0]
        bcode=i[1]
        issue_date=i[2]
        tree1.insert('','end',text="1",values=(cust_idd,bcode,issue_date))

store2=[]

def issue():
    num=1
    w1.config(state=DISABLED)
    w2.config(state=NORMAL)
    w3.config(state=NORMAL)
    w4.config(state=NORMAL)
    w5.config(state=NORMAL)
    w6.config(state=NORMAL)
    w7.config(state=NORMAL)
    w8.config(state=NORMAL)
    w9.config(state=NORMAL)
    submit_s.config(state=NORMAL)
    cust_id.set('')
    b_name.set('-----------------------------')
    i_date.set('')
    b_add.set('-----------------------------')
    b_code.set('')
    a_name.set('-----------------------------')
    arn_book.set('-----------------------------')
    e1.config(state='normal')
    e2.config(state='disabled')
    e3.config(state='normal')
    e4.config(state='disabled')
    e5.config(state='normal')
    e6.config(state='disabled')
    e7.config(state='disabled')
    tkinter.Message(r,text="                                                                         ",font=("Courier New",10),width=400,bg="white",fg="green").place(x=682,y=315)
    for item in tree1.get_children():
        tree1.delete(item)
    for itemm in tree.get_children():
        tree.delete(itemm)
    store2.clear()
    store2.append(num)
def add():
    num=2
    w1.config(state=NORMAL)
    w2.config(state=DISABLED)
    w3.config(state=NORMAL)
    w4.config(state=NORMAL)
    w5.config(state=NORMAL)
    w6.config(state=NORMAL)
    w7.config(state=NORMAL)
    w8.config(state=NORMAL)
    w9.config(state=NORMAL)
    submit_s.config(state=NORMAL)
    cust_id.set('-----------------------------')
    b_name.set('')
    i_date.set('-----------------------------')
    b_add.set('')
    b_code.set('')
    a_name.set('')
    arn_book.set('-----------------------------')
    e1.config(state='disabled')
    e2.config(state='normal')
    e3.config(state='disabled')
    e4.config(state='normal')
    e5.config(state='normal')
    e6.config(state='normal')
    e7.config(state='disabled')
    tkinter.Message(r,text="                                                                          ",font=("Courier New",10),width=400,bg="white",fg="green").place(x=682,y=315)
    for item in tree1.get_children():
        tree1.delete(item)
    for itemm in tree.get_children():
        tree.delete(itemm)
    store2.clear()
    store2.append(num)
def ret():
    num=3
    w1.config(state=NORMAL)
    w2.config(state=NORMAL)
    w3.config(state=NORMAL)
    w4.config(state=NORMAL)
    w5.config(state=DISABLED)
    w6.config(state=NORMAL)
    w7.config(state=NORMAL)
    w8.config(state=NORMAL)
    w9.config(state=NORMAL)
    submit_s.config(state=NORMAL)
    cust_id.set('')
    b_name.set('-----------------------------')
    i_date.set('-----------------------------')
    b_add.set('-----------------------------')
    b_code.set('')
    a_name.set('-----------------------------')
    arn_book.set('-----------------------------')
    e1.config(state='normal')
    e2.config(state='disabled')
    e3.config(state='disabled')
    e4.config(state='disabled')
    e5.config(state='normal')
    e6.config(state='disabled')
    e7.config(state='disabled')
    tkinter.Message(r,text="                                                                           ",font=("Courier New",10),width=400,bg="white",fg="green").place(x=682,y=315)
    for item in tree1.get_children():
        tree1.delete(item)
    for itemm in tree.get_children():
        tree.delete(itemm)
    store2.clear()
    store2.append(num)
def search():
    num=4
    w1.config(state=NORMAL)
    w2.config(state=NORMAL)
    w3.config(state=NORMAL)
    w4.config(state=NORMAL)
    w5.config(state=NORMAL)
    w6.config(state=DISABLED)
    w7.config(state=NORMAL)
    w8.config(state=NORMAL)
    w9.config(state=NORMAL)
    submit_s.config(state=NORMAL)
    cust_id.set('-----------------------------')
    b_name.set('')
    i_date.set('-----------------------------')
    b_add.set('-----------------------------')
    b_code.set('')
    a_name.set('')
    arn_book.set('-----------------------------')
    e1.config(state='disabled')
    e2.config(state='normal')
    e3.config(state='disabled')
    e4.config(state='disabled')
    e5.config(state='normal')
    e6.config(state='normal')
    e7.config(state='disabled')
    tkinter.Message(r,text="                                                                            ",font=("Courier New",10),width=400,bg="white",fg="green").place(x=682,y=315)
    for item in tree1.get_children():
        tree1.delete(item)
    for itemm in tree.get_children():
        tree.delete(itemm)
    messagebox.showinfo("INFORMATION","INFORMATION: \n\n1. If you don't know all details,you can fill any one of them and search it.\n2. Suppose,If you search one book with it's book name and another one with it's author name simultaneously,then there will be 2 different results that will be display for each of them.",parent=r)
    store2.clear()
    store2.append(num)
def delete():
    num=5
    w1.config(state=NORMAL)
    w2.config(state=NORMAL)
    w3.config(state=NORMAL)
    w4.config(state=NORMAL)
    w5.config(state=NORMAL)
    w6.config(state=NORMAL)
    w7.config(state=DISABLED)
    w8.config(state=NORMAL)
    w9.config(state=NORMAL)
    submit_s.config(state=NORMAL)
    cust_id.set('-----------------------------')
    b_name.set('-----------------------------')
    i_date.set('-----------------------------')
    b_add.set('-----------------------------')
    b_code.set('')
    a_name.set('-----------------------------')
    arn_book.set('-----------------------------')
    e1.config(state='disabled')
    e2.config(state='disabled')
    e3.config(state='disabled')
    e4.config(state='disabled')
    e5.config(state='normal')
    e6.config(state='disabled')
    e7.config(state='disabled')
    tkinter.Message(r,text="                                                                               ",font=("Courier New",10),width=400,bg="white",fg="green").place(x=682,y=315)
    for item in tree1.get_children():
        tree1.delete(item)
    for itemm in tree.get_children():
        tree.delete(itemm)
    store2.clear()
    store2.append(num)
def update():
    num=6
    w1.config(state=NORMAL)
    w2.config(state=NORMAL)
    w3.config(state=NORMAL)
    w4.config(state=NORMAL)
    w5.config(state=NORMAL)
    w6.config(state=NORMAL)
    w7.config(state=NORMAL)
    w8.config(state=DISABLED)
    w9.config(state=NORMAL)
    submit_s.config(state=NORMAL)
    cust_id.set('-----------------------------')
    b_name.set('')
    i_date.set('-----------------------------')
    b_add.set('-----------------------------')
    b_code.set('')
    a_name.set('')
    arn_book.set('')
    e1.config(state='disabled')
    e2.config(state='normal')
    e3.config(state='disabled')
    e4.config(state='disabled')
    e5.config(state='normal')
    e6.config(state='normal')
    e7.config(state='normal')
    tkinter.Message(r,text="                                                                             ",font=("Courier New",10),width=400,bg="white",fg="green").place(x=682,y=315)
    for item in tree1.get_children():
        tree1.delete(item)
    for itemm in tree.get_children():
        tree.delete(itemm)
    messagebox.showinfo("RULES","RULES:\n\n1. Rewrite ALL Existing Details if there is no need of any changes.\n2. In ADD BOOKS/REMOVE BOOKS/NO CHANGE field,Enter (+n) for Adding Books or (-n) for Reducing Books or ( 0 ) for No Change,where n=Number of Books.",parent=r)
    store2.clear()
    store2.append(num)

def help_s():
    w1.config(state=NORMAL)
    w2.config(state=NORMAL)
    w3.config(state=NORMAL)
    w4.config(state=NORMAL)
    w5.config(state=NORMAL)
    w6.config(state=NORMAL)
    w7.config(state=NORMAL)
    w8.config(state=NORMAL)
    w9.config(state=DISABLED)
    submit_s.config(state=DISABLED)
    cust_id.set('-----------------------------')
    b_name.set('-----------------------------')
    i_date.set('-----------------------------')
    b_add.set('-----------------------------')
    b_code.set('-----------------------------')
    a_name.set('-----------------------------')
    arn_book.set('-----------------------------')
    e1.config(state='disabled')
    e2.config(state='disabled')
    e3.config(state='disabled')
    e4.config(state='disabled')
    e5.config(state='disabled')
    e6.config(state='disabled')
    e7.config(state='disabled')
    tkinter.Message(r,text="                                                                              ",font=("Courier New",10),width=400,bg="white",fg="green").place(x=682,y=315)
    for item in tree1.get_children():
        tree1.delete(item)
    for itemm in tree.get_children():
        tree.delete(itemm)
    messagebox.showinfo("Help & Support","For any Help/Queries,mail us on support.group07@gmail.com",parent=r)

def clear_text():
    user1.set('')
    pas1.set('')

def logout():
    r.destroy()
    clear_text()

def count(BCODE,u):
    a=('select Total from books where Bcode=%s')
    data=(BCODE,)
    c=conn.cursor()
    c.execute(a,data)
    res=c.fetchone()
    t=res[0] + u
    sql='update books set Total=%s where Bcode=%s'
    d=(t,BCODE)
    c.execute(sql,d)
    conn.commit()

def submit_b():
    if(1 in store2):
        ID1=cust_id.get()
        ID=ID1.upper()
        ISSUE_DATE=i_date.get()
        BCODE1=b_code.get()
        BCODE=BCODE1.upper()
        QUANTITY=1
        tkinter.Message(r,text="                                                                              ",font=("Courier New",10),width=400,bg="white",fg="green").place(x=682,y=315)
        try:
            if(ID=='' or ISSUE_DATE=='' or BCODE==''):
                tkinter.Message(r,text="FILL THE EMPTY FIELDS!!!",font=("Courier New",10),width=300,bg="white",fg="red").place(x=682,y=315)
            else:
                store7=[]
                sql=('select Bcode from books')
                c=conn.cursor()
                c.execute(sql,)
                res=c.fetchall()
                for i in res:
                    i[0]
                    store7.append(i[0])
                if(BCODE not in store7):
                    tkinter.Message(r,text="ENTER THE CORRECT BOOK CODE!!!",font=("Courier New",10),width=300,bg="white",fg="red").place(x=682,y=315)
                else:
                    a=('select Total from books where Bcode=%s')
                    d=(BCODE,)
                    c=conn.cursor()
                    c.execute(a,d)
                    res=c.fetchone()
                    k=res[0]
                    if k>=QUANTITY:
                        x=('select count(*) from issue where Customer_id=%s and Bcode=%s')
                        y=(ID,BCODE)
                        c=conn.cursor()
                        c.execute(x,y)
                        z=c.fetchone()
                        u=z[0]
                        if u>=1:
                            tkinter.Message(r,text="SORRY...,BOOK IS ALREADY ISSUED BY THE CUSTOMER!!!",font=("Courier New",9),width=450,bg="white",fg="red").place(x=682,y=315)
                        else:
                            data=(ID,BCODE,ISSUE_DATE,QUANTITY)
                            sql='insert into issue values(%s,%s,%s,%s)'
                            c=conn.cursor()
                            c.execute(sql,data)
                            conn.commit()
                            count(BCODE,-1)
                            tkinter.Message(r,text="BOOK ISSUED SUCESSFULLY!!!",font=("Courier New",10),width=500,bg="white",fg="green").place(x=682,y=315)
                    else:
                        tkinter.Message(r,text="SORRY...,BOOK IS NOT AVAILABLE IN SUFFICIENT QUANTITY!!!",font=("Courier New",9),width=400,bg="white",fg="red").place(x=682,y=315)
        except mysql.DataError:
            tkinter.Message(r,text="DATE FORMAT INCORRECT!!!",font=("Courier New",10),width=300,bg="white",fg="red").place(x=682,y=315)
             

    elif(2 in store2):
        BCODE1=b_code.get()
        BCODE=BCODE1.upper()
        BNAME1=b_name.get()
        BNAME=BNAME1.upper()
        T1=b_add.get()
        AUTHOR1=a_name.get()
        AUTHOR=AUTHOR1.upper()
        tkinter.Message(r,text="                                                                              ",font=("Courier New",10),width=400,bg="white",fg="green").place(x=682,y=315)
        try:
            if(BCODE=='' or BNAME=='' or AUTHOR==''):
                tkinter.Message(r,text="FILL THE EMPTY FIELDS!!!",font=("Courier New",10),width=300,bg="white",fg="red").place(x=682,y=315)
            else:
                T=int(b_add.get())
                store3=[]
                sql=('select Bcode from books')
                c=conn.cursor()
                c.execute(sql,)
                res=c.fetchall()
                for i in res:
                    i[0]
                    store3.append(i[0])
                if(BCODE in store3):
                    tkinter.Message(r,text="ENTER UNIQUE BOOK CODE!!!",font=("Courier New",10),width=300,bg="white",fg="red").place(x=682,y=315)
                else:
                    if T<0:
                        tkinter.Message(r,text="SORRY...,BOOKS CANN'T BE LESS THAN ZERO!!!",font=("Courier New",9),width=400,bg="white",fg="red").place(x=682,y=315)
                    else:
                        data=(BCODE,BNAME,T,AUTHOR)
                        a='insert into books values(%s,%s,%s,%s)'
                        c=conn.cursor()
                        c.execute(a,data)
                        conn.commit()
                        tkinter.Message(r,text="BOOK DETAIL ADDED SUCESSFULLY!!!",font=("Courier New",10),width=300,bg="white",fg="green").place(x=682,y=315)
        except ValueError:
            tkinter.Message(r,text="ENTER INTEGER TYPE FOR NUMBER OF BOOKS!!!",font=("Courier New",9),width=400,bg="white",fg="red").place(x=682,y=315)

    elif(3 in store2):
        ID1=cust_id.get()
        ID=ID1.upper()
        BCODE1=b_code.get()
        BCODE=BCODE1.upper()
        tkinter.Message(r,text="                                                                              ",font=("Courier New",10),width=400,bg="white",fg="green").place(x=682,y=315)
        if(BCODE=='' or ID==''):
            tkinter.Message(r,text="FILL THE EMPTY FIELDS!!!",font=("Courier New",10),width=300,bg="white",fg="red").place(x=682,y=315)
        else:
            store5=[]
            sql=('select Bcode from issue')
            c=conn.cursor()
            c.execute(sql,)
            res=c.fetchall()
            for i in res:
                i[0]
                store5.append(i[0])
            store6=[]
            sql=('select Customer_id from issue')
            c=conn.cursor()
            c.execute(sql,)
            res=c.fetchall()
            for i in res:
                i[0]
                store6.append(i[0])
            if((BCODE not in store5) or (ID not in store6)):
                tkinter.Message(r,text="ENTER CORRECT DETAILS!!!",font=("Courier New",10),width=300,bg="white",fg="red").place(x=682,y=315)
            else:
                store9=[]
                sql=('select Bcode from issue')
                c=conn.cursor()
                c.execute(sql,)
                res=c.fetchall()
                for i in res:
                    i[0]
                    store9.append(i[0])
                store10=[]
                sql=('select Customer_id from issue')
                c=conn.cursor()
                c.execute(sql,)
                res=c.fetchall()
                for i in res:
                    i[0]
                    store10.append(i[0])
                pair1=list(zip(store9,store10))
                if((BCODE,ID) not in pair1):
                    tkinter.Message(r,text="ENTER CORRECT DETAILS!!!",font=("Courier New",10),width=300,bg="white",fg="red").place(x=682,y=315)
                else:
                    data=(BCODE,ID)
                    sql='delete from issue where Bcode=%s and Customer_id=%s'
                    c=conn.cursor()
                    c.execute(sql,data)
                    conn.commit()
                    count(BCODE,1)
                    tkinter.Message(r,text="BOOK RETURNED SUCESSFULLY!!!",font=("Courier New",10),width=300,bg="white",fg="green").place(x=682,y=315)

    elif(4 in store2):
        BCODE1=b_code.get()
        BCODE=BCODE1.upper()
        BNAME1=b_name.get()
        BNAME=BNAME1.upper()
        AUTHOR1=a_name.get()
        AUTHOR=AUTHOR1.upper()
        tkinter.Message(r,text="                                                                              ",font=("Courier New",10),width=400,bg="white",fg="green").place(x=682,y=315)
        for itemm in tree.get_children():
            tree.delete(itemm)
        if(BCODE=='' and BNAME=='' and AUTHOR==''):
            tkinter.Message(r,text="FILL THE EMPTY FIELDS!!!",font=("Courier New",10),width=300,bg="white",fg="red").place(x=682,y=315)
        else:
            a=('select * from books where Bcode=%s or Book=%s or Author=%s')
            data=(BCODE,BNAME,AUTHOR)
            c=conn.cursor()
            c.execute(a,data)
            res=c.fetchall()
            for i in res:
                bcode=i[0]
                bname=i[1]
                avbook=i[2]
                auth=i[3]
                tree.insert('','end',text="1",values=(bcode,bname,avbook,auth))
            no_of_row=len(tree.get_children())
            if(no_of_row>=1):
                tkinter.Message(r,text="RESULT FOUND!!!",font=("Courier New",10),width=400,bg="white",fg="green").place(x=682,y=315)
            else:
                tkinter.Message(r,text="NO RESULT FOUND!!!",font=("Courier New",10),width=300,bg="white",fg="red").place(x=682,y=315)

    elif(5 in store2):
        BCODE1=b_code.get()
        BCODE=BCODE1.upper()
        tkinter.Message(r,text="                                                                              ",font=("Courier New",10),width=400,bg="white",fg="green").place(x=682,y=315)
        if(BCODE==''):
            tkinter.Message(r,text="FILL THE EMPTY FIELD!!!",font=("Courier New",10),width=300,bg="white",fg="red").place(x=682,y=315)
        else:
            store4=[]
            sql=('select Bcode from books')
            c=conn.cursor()
            c.execute(sql,)
            res=c.fetchall()
            for i in res:
                i[0]
                store4.append(i[0])
            if(BCODE not in store4):
                tkinter.Message(r,text="ENTER THE CORRECT BOOK CODE!!!",font=("Courier New",10),width=300,bg="white",fg="red").place(x=682,y=315)
            else:
                a='delete from books where Bcode=%s'
                data=(BCODE,)
                c=conn.cursor()
                c.execute(a,data)
                conn.commit()
                b='delete from issue where bcode=%s'
                dat=(BCODE,)
                c1=conn.cursor()
                c1.execute(b,dat)
                conn.commit()
                tkinter.Message(r,text="BOOK DETAIL DELETED SUCESSFULLY!!!",font=("Courier New",10),width=300,bg="white",fg="green").place(x=682,y=315)
        
    elif(6 in store2):
            BCODE1=b_code.get()
            BCODE=BCODE1.upper()
            BNAME1=b_name.get()
            BNAME=BNAME1.upper()
            T21=arn_book.get()
            AUTHOR1=a_name.get()
            AUTHOR=AUTHOR1.upper()
            tkinter.Message(r,text="                                                                              ",font=("Courier New",10),width=400,bg="white",fg="green").place(x=682,y=315)
            try:
                if(BCODE=='' or BNAME=='' or T21=='' or AUTHOR==''):
                    tkinter.Message(r,text="FILL THE EMPTY FIELDS!!!",font=("Courier New",10),width=300,bg="white",fg="red").place(x=682,y=315)
                else:
                    T1=int(arn_book.get())
                    store8=[]
                    sql=('select Bcode from books')
                    c=conn.cursor()
                    c.execute(sql,)
                    res=c.fetchall()
                    for i in res:
                        i[0]
                        store8.append(i[0])
                    if(BCODE not in store8):
                        tkinter.Message(r,text="ENTER THE CORRECT BOOK CODE!!!",font=("Courier New",10),width=300,bg="white",fg="red").place(x=682,y=315)
                    else:
                        a1=('select Total from books where Bcode=%s')
                        data1=(BCODE,)
                        c1=conn.cursor()
                        c1.execute(a1,data1)
                        res1=c1.fetchone()
                        to1=res1[0] + T1
                        if to1<0:
                            tkinter.Message(r,text="SORRY..,BOOK IS NOT AVAILABLE IN SUFFICIENT QUANTITY!!!",font=("Courier New",9),width=400,bg="white",fg="red").place(x=682,y=315)
                        else:
                            a='update books set Book=%s,Author=%s where Bcode=%s'
                            data=(BNAME,AUTHOR,BCODE)
                            c=conn.cursor()
                            c.execute(a,data)
                            conn.commit()
                            count(BCODE,T1)
                            tkinter.Message(r,text="BOOK DETAIL UPDATED SUCESSFULLY!!!",font=("Courier New",10),width=300,bg="white",fg="green").place(x=682,y=315)

            except ValueError:                
                 tkinter.Message(r,text="ENTER INTEGER TYPE FOR NUMBER OF BOOKS!!!",font=("Courier New",9),width=400,bg="white",fg="red").place(x=682,y=315)

    else:
        tkinter.Message(r,text="FIRST,... SELECT ANY OPTION!!!",font=("Courier New",10),width=300,bg="white",fg="red").place(x=682,y=315)
                             

def option():
    global r
    r=tkinter.Toplevel(root)
    r.title('LIBRARY MANAGEMENT SYSTEM')
    r.geometry("1200x650+40+20")
    head=tkinter.Label(r,text='WELCOME TO CENTRAL LIBRARY',font=("Boldman Old Style",27,"bold"),width=56,height=3,fg="floral white",bg="navy")
    head.place(x=0,y=16)
    tkinter.Label(r,bg="lavender",width=190,height=40).place(x=0,y=150)
    global w1,w2,w3,w4,w5,w6,w7,w8,w9,submit_s
    w1=tkinter.Button(r,text='ISSUE BOOK',width=18,height=2,relief=RIDGE,font=("Cambria",10,"bold"),bg="silver",command=issue)
    w1.place(x=10,y=162)
    w1.config(fg="navy blue")
    w2=tkinter.Button(r,text='ADD BOOKS',width=18,height=2,relief=RIDGE,font=("Cambria",10,"bold"),bg="silver",command=add)
    w2.place(x=10,y=207)
    w2.config(fg="navy blue")
    w3=tkinter.Button(r,text='VIEW BOOKS',width=18,height=2,relief=RIDGE,font=("Cambria",10,"bold"),bg="silver",command=view)
    w3.place(x=10,y=252)
    w3.config(fg="navy blue")
    w4=tkinter.Button(r,text='VIEW ISSUED BOOKS',width=18,height=2,relief=RIDGE,font=("Cambria",10,"bold"),bg="silver",command=issued)
    w4.place(x=10,y=297)
    w4.config(fg="navy blue")
    w5=tkinter.Button(r,text='RETURN BOOK',width=18,height=2,relief=RIDGE,font=("Cambria",10,"bold"),bg="silver",command=ret)
    w5.place(x=10,y=342)
    w5.config(fg="navy blue")
    w6=tkinter.Button(r,text='SEARCH BOOK',width=18,height=2,relief=RIDGE,font=("Cambria",10,"bold"),bg="silver",command=search)
    w6.place(x=10,y=387)
    w6.config(fg="navy blue")
    w7=tkinter.Button(r,text='DELETE BOOKS',width=18,height=2,relief=RIDGE,font=("Cambria",10,"bold"),bg="silver",command=delete)
    w7.place(x=10,y=432)
    w7.config(fg="navy blue")
    w8=tkinter.Button(r,text='UPDATE BOOKS',width=18,height=2,relief=RIDGE,font=("Cambria",10,"bold"),bg="silver",command=update)
    w8.place(x=10,y=477)
    w8.config(fg="navy blue")
    w9=tkinter.Button(r,text='HELP',width=18,height=2,relief=RIDGE,font=("Cambria",10,"bold"),bg="silver",command=help_s)
    w9.place(x=10,y=522)
    w9.config(fg="navy blue")
    w10=tkinter.Button(r,text='LOGOUT',width=18,height=2,relief=RIDGE,font=("Cambria",10,"bold"),bg="silver",command=logout)
    w10.place(x=10,y=567)
    w10.config(fg="navy blue")

    tkinter.Label(r,text='CUSTOMER ID:',fg="black",bg="lavender",font=("Cambria",10)).place(x=200,y=165)
    tkinter.Label(r,text='BOOK NAME:',fg="black",bg="lavender",font=("Cambria",10)).place(x=200,y=245)
    tkinter.Label(r,text='ISSUE DATE[YYYY-MM-DD]:',fg="black",bg="lavender",font=("Cambria",10)).place(x=670,y=205)
    tkinter.Label(r,text='NUMBER OF BOOKS ADDING:',fg="black",bg="lavender",font=("Cambria",10)).place(x=670,y=165)
    tkinter.Label(r,text='BOOK CODE:',fg="black",bg="lavender",font=("Cambria",10)).place(x=200,y=205)
    tkinter.Label(r,text='AUTHOR NAME:',fg="black",bg="lavender",font=("Cambria",10)).place(x=200,y=285)
    tkinter.Label(r,text='ADD BOOKS/REMOVE BOOKS/NO CHANGE:',fg="black",bg="lavender",font=("Cambria",10)).place(x=670,y=245)
    tkinter.Label(r,text='BOOK LIST:',fg="black",bg="lavender",font=("Cambria",10)).place(x=200,y=381)
    tkinter.Label(r,text='CUSTOMER RECORD:',fg="black",bg="lavender",font=("Cambria",10)).place(x=673,y=381)
    global cust_id
    global b_name
    global i_date
    global b_add
    global b_code
    global a_name
    global arn_book
    cust_id=tkinter.StringVar()
    b_name=tkinter.StringVar()
    i_date=tkinter.StringVar()
    b_add=tkinter.StringVar()
    b_code=tkinter.StringVar()
    a_name=tkinter.StringVar()
    arn_book=tkinter.StringVar()
    global e1,e2,e3,e4,e5,e6,e7
    e1=tkinter.Entry(r,textvariable=cust_id,width=25,fg="black",bg="white",font=("Microsoft Yahei UI light",10))
    e1.place(x=300,y=165)
    e2=tkinter.Entry(r,textvariable=b_name,width=25,fg="black",bg="white",font=("Microsoft Yahei UI light",10))
    e2.place(x=295,y=245)
    e3=DateEntry(r,textvariable=i_date,width=25,fg="black",bg="white",date_pattern='yyyy-mm-dd',state='disabled',font=("Microsoft Yahei UI light",10))
    e3.place(x=840,y=205)
    e4=tkinter.Entry(r,textvariable=b_add,width=25,fg="black",bg="white",font=("Microsoft Yahei UI light",10))
    e4.place(x=855,y=165)
    e5=tkinter.Entry(r,textvariable=b_code,width=25,fg="black",bg="white",font=("Microsoft Yahei UI light",10))
    e5.place(x=295,y=205)
    e6=tkinter.Entry(r,textvariable=a_name,width=25,fg="black",bg="white",font=("Microsoft Yahei UI light",10))
    e6.place(x=310,y=285)
    e7=tkinter.Entry(r,textvariable=arn_book,width=25,fg="black",bg="white",font=("Microsoft Yahei UI light",10))
    e7.place(x=935,y=245)
    submit_s=tkinter.Button(r,text='SUBMIT',relief=RIDGE,font=("Cambria",10,"bold"),fg="navy blue",bg="silver",activebackground="lavender",width=18,height=2,command=submit_b)
    submit_s.place(x=320,y=325)
    tkinter.Frame(r,width=440,height=74,bg="white").place(x=676,y=294)
    notify=tkinter.Message(r,text="MESSAGE:",font=("Cambria",10),width=60,bg="white").place(x=682,y=294)

    s=ttk.Style()
    s.theme_use("clam")
    tkinter.Frame(r,width=450,height=200,bd=8,bg="white",relief=RIDGE).place(x=200,y=400)
    global tree
    tree=ttk.Treeview(r,column=("BOOK CODE","BOOK NAME","QUANTITY","AUTHOR"),show='headings',height=7)
    xscrolll=ttk.Scrollbar(r,orient=HORIZONTAL,command=tree.xview)
    yscrolll=ttk.Scrollbar(r,orient=VERTICAL,command=tree.yview)
    xscrolll.place(x=212,y=577,width=407)
    yscrolll.place(x=623,y=410,height=168)
    tree.configure(xscrollcommand=xscrolll.set)
    tree.configure(yscrollcommand=yscrolll.set)
    tree.column("#1",width=100,anchor=CENTER)
    tree.heading("#1",text="BOOK CODE")
    tree.column("#2",width=120,anchor=CENTER)
    tree.heading("#2",text="BOOK NAME")
    tree.column("#3",width=80,anchor=CENTER)
    tree.heading("#3",text="QUANTITY")
    tree.column("#4",width=105,anchor=CENTER)
    tree.heading("#4",text="AUTHOR")
    tree.place(x=212,y=409)

    tkinter.Frame(r,width=450,height=200,bd=8,bg="white",relief=RIDGE).place(x=673,y=400)
    global tree1
    tree1=ttk.Treeview(r,column=("CUSTOMER ID","BOOK CODE","ISSUE DATE"),show='headings',height=7)
    xscrollll=ttk.Scrollbar(r,orient=HORIZONTAL,command=tree1.xview)
    yscrollll=ttk.Scrollbar(r,orient=VERTICAL,command=tree1.yview)
    xscrollll.place(x=687,y=577,width=404)
    yscrollll.place(x=1095,y=410,height=168)
    tree1.configure(xscrollcommand=xscrollll.set)
    tree1.config(yscrollcommand=yscrollll.set)
    tree1.column("#1",width=150,anchor=CENTER)
    tree1.heading("#1",text="CUSTOMER ID")
    tree1.column("#2",width=100,anchor=CENTER)
    tree1.heading("#2",text="BOOK CODE")
    tree1.column("#3",width=150,anchor=CENTER)
    tree1.heading("#3",text="ISSUE DATE")
    tree1.place(x=687,y=409)
    r.mainloop()
    
def login():        
    global root
    root=tkinter.Tk()
    root.title('LOGIN')
    root.geometry("678x452+310+150")
    bg=ImageTk.PhotoImage(file="photo3.jpeg")
    tkinter.Label(root,image=bg).place(x=0,y=0)
    tkinter.Frame(root,width=270,height=245,bg="white").place(x=200,y=50)
    tkinter.Label(root,text='Login',font=("Microsoft Yahei UI light",17,"bold"),width=10,bg="white",fg="medium blue").place(x=263,y=60)
    tkinter.Label(root,text='Username',fg="black",bg="white",font=("Cambria",12)).place(x=250,y=118)
    tkinter.Label(root,text='Password',fg="black",bg="white",font=("Cambria",12)).place(x=250,y=182)
    linkk=tkinter.Label(root,text='Forget Password?',width=15,height=1,font=("Microsoft Yahei UI light",9,"underline"),bg="white",fg="medium blue")
    linkk.place(x=320,y=259)
    linkk.bind("<Button-1>",lambda e: forget())
    tkinter.Frame(root,width=175,height=2,bg="black").place(x=250,y=167)
    tkinter.Frame(root,width=175,height=2,bg="black").place(x=250,y=231)
    global user1
    global pas1
    user1=tkinter.StringVar()
    pas1=tkinter.StringVar()
    tkinter.Entry(root,textvariable=user1,width=25,border=0,fg="black",bg="white",font=("Microsoft Yahei UI light",10,"bold")).place(x=250,y=146)
    tkinter.Entry(root,textvariable=pas1,show='*',width=25,border=0,fg="black",bg="white",font=("Microsoft Yahei UI light",10,"bold")).place(x=250,y=210)
    submit=tkinter.Button(root,text='Submit',bg="medium blue",fg="white",width=9,activebackground="green",font=("Microsoft Yahei UI light",12),command=check)
    submit.place(x=200,y=310)
    submit.config(fg="white")
    logout=tkinter.Button(root,text='Exit',bg="medium blue",fg="white",width=9,font=("Microsoft Yahei UI light",12),command=root.destroy)
    logout.place(x=377,y=310)
    logout.config(fg="white")
    register=tkinter.Button(root,text='Create New Account',bg="medium blue",fg="white",activeforeground="green",width=19,font=("Microsoft Yahei UI light",11,"underline"),command=signup)
    register.place(x=246,y=355)
    root.mainloop()
login()




