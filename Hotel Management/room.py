from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
#import random
from time import strftime
from datetime import datetime
from tkinter import messagebox
import mysql.connector

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title="Hotel Management System"
        self.root.geometry("1300x500+230+230")

        #================Variables=================
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        # ===============title=======================
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=('Gabriola', 18, 'bold'), bg="black",fg="gold", relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1300, height=50)

        img2 = Image.open(
            r"D:\Harsh\SEM 4\PYTHON\Hotel Management\Hotel Management\images\hotel2.png")  # r is used to make backward slash as forward slash
        img2 = img2.resize((100, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=2, y=0, width=100, height=50)

        # =================Labelframe====================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, padx=2, text="Room Booking",font=('Gabriola', 12, 'bold'))
        labelframeleft.place(x=5, y=50, width=425, height=445)

        # ================labels and entry ==============
        # cust contact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact", font=('Arial', 10, 'bold'), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0,sticky=W)

        entry_contact = ttk.Entry(labelframeleft, width=20, textvariable=self.var_contact ,font=('Arial', 12, 'bold'))
        entry_contact.grid(row=0, column=1,sticky=W)

        # ================Fetch Data Button=====================
        btnFetchdata = Button(labelframeleft, command=self.Fetch_contact,text="Fetch Data", font=('Arial', 10, 'bold'), bg='black', fg='gold',width=8)
        btnFetchdata.place(x=312,y=2)

        # checkin date
        lbl_cust_checkin = Label(labelframeleft, text="Check_in Date:", font=('Arial', 10, 'bold'), padx=2, pady=6)
        lbl_cust_checkin.grid(row=1, column=0,sticky=W)

        text_checkin = ttk.Entry(labelframeleft, width=29, textvariable=self.var_checkin , font=('Arial', 12, 'bold'))
        text_checkin.grid(row=1, column=1)

        # checkout date
        lbl_cust_checkout = Label(labelframeleft, text="Check_out Date:", font=('Arial', 10, 'bold'), padx=2, pady=6)
        lbl_cust_checkout.grid(row=2, column=0,sticky=W)

        text_checkout = ttk.Entry(labelframeleft, width=29, textvariable=self.var_checkout ,font=('Arial', 12, 'bold'))
        text_checkout.grid(row=2, column=1)

        # Room Type
        lbl_RoomType = Label(labelframeleft, text=" Room Type:", font=('Arial', 10, 'bold'), padx=2, pady=6)
        lbl_RoomType.grid(row=3, column=0,sticky=W)

        conn = mysql.connector.connect(host="localhost", user="root", password="password", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        type = my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype ,font=('Arial', 10, 'bold'), width=35,state="readonly")
        combo_RoomType["value"] = type
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Available Room
        lbl_RoomAvailable = Label(labelframeleft, text="Available Room:", font=('Arial', 10, 'bold'), padx=2, pady=6)
        lbl_RoomAvailable.grid(row=4, column=0,sticky=W)

        #text_RoomAvailable = ttk.Entry(labelframeleft, textvariable=self.var_roomavailable ,width=29, font=('Arial', 12, 'bold'))
        #text_RoomAvailable.grid(row=4, column=1)

        conn = mysql.connector.connect(host="localhost", user="root", password="password", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, font=('Arial', 10, 'bold'),
                                      width=35, state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

        # Meal
        lbl_Meal = Label(labelframeleft, text=" Meal:", font=('Arial', 10, 'bold'), padx=2, pady=6)
        lbl_Meal.grid(row=5, column=0,sticky=W)

        text_Meal = ttk.Entry(labelframeleft, width=29,textvariable=self.var_meal , font=('Arial', 12, 'bold'))
        text_Meal.grid(row=5, column=1)

        # No.of Days
        lbl_NoOfDays = Label(labelframeleft, text="No.of Days:", font=('Arial', 10, 'bold'), padx=2, pady=6)
        lbl_NoOfDays.grid(row=6, column=0,sticky=W)

        text_NoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_noofdays ,width=29, font=('Arial', 12, 'bold'))
        text_NoOfDays.grid(row=6, column=1)

        # Paid Tax
        lbl_paidTax = Label(labelframeleft, text="Paid Tax:", font=('Arial', 10, 'bold'), padx=2, pady=6)
        lbl_paidTax.grid(row=7, column=0,sticky=W)

        text_paidTax = ttk.Entry(labelframeleft, textvariable=self.var_paidtax,width=29, font=('Arial', 12, 'bold'))
        text_paidTax.grid(row=7, column=1)

        # sub Total
        lbl_subTotal = Label(labelframeleft, text="Sub Total:", font=('Arial', 10, 'bold'), padx=2, pady=6)
        lbl_subTotal.grid(row=8, column=0,sticky=W)

        text_subTotal = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal ,width=29, font=('Arial', 12, 'bold'))
        text_subTotal.grid(row=8, column=1)

        #Total Cost
        lbl_totalCost = Label(labelframeleft, text="Total Cost:", font=('Arial', 10, 'bold'), padx=2, pady=6)
        lbl_totalCost.grid(row=9, column=0,sticky=W)

        text_totalCost = ttk.Entry(labelframeleft, textvariable=self.var_total ,width=29, font=('Arial', 12, 'bold'))
        text_totalCost.grid(row=9, column=1)

        #=======Bill Button=========
        btnBill = Button(labelframeleft, text="Bill", command=self.total ,font=('Arial', 12, 'bold'), bg='black', fg='gold',width=9)
        btnBill.grid(row=10, column=0, padx=1,sticky=W)

        # =================Buttons=====================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=370, width=312, height=40)

        btnAdd = Button(btn_frame, text="Add",command=self.add_data, font=('Arial', 12, 'bold'), bg='black', fg='gold',width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btndelete = Button(btn_frame, text="DELETE", command=self.delete ,font=('Arial', 12, 'bold'), bg='black',fg='gold', width=9)
        btndelete.grid(row=0, column=2, padx=1)

        btnreset = Button(btn_frame, text="RESET" ,command=self.reset ,font=('Arial', 12, 'bold'), bg='black',fg='gold', width=9)
        btnreset.grid(row=0, column=3, padx=1)

        #==================Right Side Image==========================
        img3 = Image.open(
            r"D:\Harsh\SEM 4\PYTHON\Hotel Management\Hotel Management\images\hotel4.png")  # r is used to make backward slash as forward slash
        img3 = img3.resize((499, 200), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=800, y=51, width=499, height=200)


        # =================table frame Search System==================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, padx=2, text="View Details",font=('Gabriola', 12, 'bold'))
        Table_Frame.place(x=435, y=250, width=862, height=245)

        #=============Show Table Data================
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=20, width=862, height=160)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table,column=("Contact", "CheckIn", "CheckOut", "RoomType", "RoomAvailable", "Meal","NoOfDays",),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Contact", text="Contact No.")
        self.room_table.heading("CheckIn", text="Check-in")
        self.room_table.heading("CheckOut", text="Check-out")
        self.room_table.heading("RoomType", text="Room Type")
        self.room_table.heading("RoomAvailable", text="Room No.")
        self.room_table.heading("Meal", text="Meal")
        self.room_table.heading("NoOfDays", text="No.of Days")


        self.room_table["show"] = "headings"

        self.room_table.column("Contact", width=100)
        self.room_table.column("CheckIn", width=100)
        self.room_table.column("CheckOut", width=100)
        self.room_table.column("RoomType", width=100)
        self.room_table.column("RoomAvailable", width=100)
        self.room_table.column("Meal", width=100)
        self.room_table.column("NoOfDays", width=100)
        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    #================Add Function=======================

    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Warning","Pleas enter all the details",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",passwd="password",database="hotel")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_contact.get(),
                                                                                    self.var_checkin.get(),
                                                                                    self.var_checkout.get(),
                                                                                    self.var_roomtype.get(),
                                                                                    self.var_roomavailable.get(),
                                                                                    self.var_meal.get(),
                                                                                    self.var_noofdays.get(),
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Room Booked!",parent=self.root)
            except Exception as es:
                messagebox.showerror("warning","something went wrong!:{str(es)}",parent=self.root)

    #===============Fetch FUnction=================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="password", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
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

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

    #============Update Function===================


    #===========Delete Function==============
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if delete>0:
            conn = mysql.connector.connect(host="localhost", user="root", password="password", database="hotel")
            my_cursor = conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #=============Reset Function============
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set("")


    #==================All Data Fetch===================
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", passwd="password", database="hotel")
            my_cursor = conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Oops!","Number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=330,height=190)

                lblName=Label(showDataframe,text="Name:",font=("Arial",12,"bold"))
                lblName.place\
                    (x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("Arial",12,"bold"))
                lbl.place(x=90, y=0)

                #========Gender=============
                conn = mysql.connector.connect(host="localhost", user="root", passwd="password", database="hotel")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblgender = Label(showDataframe, text="Gender:", font=("Arial", 12, "bold"))
                lblgender.place(x=0, y=30)

                lbl2 = Label(showDataframe, text=row, font=("Arial", 12, "bold"))
                lbl2.place(x=90, y=30)

                #===========Email=============
                conn = mysql.connector.connect(host="localhost", user="root", passwd="password", database="hotel")
                my_cursor = conn.cursor()
                query = ("select Email from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblemail = Label(showDataframe, text="Email:", font=("Arial", 12, "bold"))
                lblemail.place(x=0, y=60)

                lbl3 = Label(showDataframe, text=row, font=("Arial", 12, "bold"))
                lbl3.place(x=90, y=60)

                #==========Nationality==============
                conn = mysql.connector.connect(host="localhost", user="root", passwd="password", database="hotel")
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblnationality = Label(showDataframe, text="Nationality:", font=("Arial", 12, "bold"))
                lblnationality.place(x=0, y=90)

                lbl4 = Label(showDataframe, text=row, font=("Arial", 12, "bold"))
                lbl4.place(x=90, y=90)

                #============Address=============
                conn = mysql.connector.connect(host="localhost", user="root", passwd="password", database="hotel")
                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lbladdress = Label(showDataframe, text="Address:", font=("Arial", 12, "bold"))
                lbladdress.place(x=0, y=120)

                lbl4 = Label(showDataframe, text=row, font=("Arial", 12, "bold"))
                lbl4.place(x=90, y=120)

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(1500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.2))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*.2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "Super Delux"):
            q1 = float(300)
            q2 = float(1100)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.2))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * .2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "Delux"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.2))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * .2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Delux"):
            q1 = float(350)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.2))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * .2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Super Delux"):
            q1 = float(350)
            q2 = float(1100)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.2))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * .2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Luxury"):
            q1 = float(350)
            q2 = float(1500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.2))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * .2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Delux"):
            q1 = float(400)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.2))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * .2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Super Delux"):
            q1 = float(400)
            q2 = float(1100)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.2))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * .2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Luxury"):
            q1 = float(400)
            q2 = float(1500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.2))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * .2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()