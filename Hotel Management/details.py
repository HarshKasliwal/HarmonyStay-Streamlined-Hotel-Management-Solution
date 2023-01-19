from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox
import mysql.connector

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title="Hotel Management System"
        self.root.geometry("1300x500+230+230")

        # ===============title=======================
        lbl_title = Label(self.root, text="ROOM ADDING DEPARTMENT", font=('Gabriola', 18, 'bold'), bg="black", fg="gold",
                          relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1300, height=50)

        img2 = Image.open(
            r"D:\Harsh\SEM 4\PYTHON\Hotel Management\Hotel Management\images\hotel2.png")  # r is used to make backward slash as forward slash
        img2 = img2.resize((100, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=2, y=0, width=100, height=50)

        # =================Labelframe====================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, padx=2, text="New Room Add",
                                    font=('Gabriola', 12, 'bold'))
        labelframeleft.place(x=5, y=50, width=460, height=350)

        # ==========Floor=================
        lbl_floor = Label(labelframeleft, text="Floor", font=('Arial', 10, 'bold'), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)

        self.var_floor=StringVar()
        entry_floor = ttk.Entry(labelframeleft,textvariable=self.var_floor, width=20, font=('Arial', 12, 'bold'))
        entry_floor.grid(row=0, column=1, sticky=W)

        # ==========Room No.===============
        lbl_roomno = Label(labelframeleft, text="Room No.", font=('Arial', 10, 'bold'), padx=2, pady=6)
        lbl_roomno.grid(row=1, column=0, sticky=W)

        self.var_roomno=StringVar()
        entry_roomno = ttk.Entry(labelframeleft, textvariable=self.var_roomno,width=20, font=('Arial', 12, 'bold'))
        entry_roomno.grid(row=1, column=1, sticky=W)

        #================Room Type====================
        # cust contact
        lbl_roomtype = Label(labelframeleft, text="Room Type", font=('Arial', 10, 'bold'), padx=2, pady=6)
        lbl_roomtype.grid(row=2, column=0, sticky=W)

        self.var_roomtype=StringVar()
        entry_roomtype = ttk.Entry(labelframeleft, textvariable=self.var_roomtype ,width=20, font=('Arial', 12, 'bold'))
        entry_roomtype.grid(row=2, column=1, sticky=W)

        #=============Buttons=================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=312, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=('Arial', 12, 'bold'), bg='black', fg='gold',
                        width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btndelete = Button(btn_frame, text="DELETE", command=self.delete ,font=('Arial', 12, 'bold'), bg='black',
                           fg='gold', width=9)
        btndelete.grid(row=0, column=2, padx=1)

        btnreset = Button(btn_frame, text="RESET", command=self.reset,font=('Arial', 12, 'bold'), bg='black',
                          fg='gold', width=9)
        btnreset.grid(row=0, column=3, padx=1)

        # =================Labelframe Right====================
        labelframeright = LabelFrame(self.root, bd=2, relief=RIDGE, padx=2, text="Show Room Details",
                                    font=('Gabriola', 12, 'bold'))
        labelframeright.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(labelframeright, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(labelframeright, orient=VERTICAL)

        self.room_table = ttk.Treeview(labelframeright,
                                       column=("Floor", "RoomNo", "RoomType"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Floor", text="Floor")
        self.room_table.heading("RoomNo", text="Room No.")
        self.room_table.heading("RoomType", text="Room Type")


        self.room_table["show"] = "headings"

        self.room_table.column("Floor", width=100)
        self.room_table.column("RoomNo", width=100)
        self.room_table.column("RoomType", width=100)
        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    #=============Add Functio===================
    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
            messagebox.showerror("Warning","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",passwd="password",database="hotel")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                    self.var_floor.get(),
                                                                                    self.var_roomno.get(),
                                                                                    self.var_roomtype.get()

                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","New Room Added!",parent=self.root)
            except Exception as es:
                messagebox.showerror("warning","something went wrong!:{str(es)}",parent=self.root)
    #===========Fetch Data=====================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="password", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #=============Get Cursor Function=============
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2])
        

    #=================Delete Function==================
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete this Room Details",parent=self.root)
        if delete>0:
            conn = mysql.connector.connect(host="localhost", user="root", password="passworrd", database="hotel")
            my_cursor = conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #================Reset Function===============
    def reset(self):
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_roomtype.set("")



if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()