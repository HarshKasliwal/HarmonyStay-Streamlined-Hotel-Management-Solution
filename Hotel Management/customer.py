from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector

class Cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title="Hotel Management System"
        self.root.geometry("1300x500+230+230")

        #====================Variables===============
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()

        # ===============title=======================
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=('Gabriola', 18, 'bold'), bg="black",
                          fg="gold", relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1300, height=50)

        # ==================Logo====================
        img2 = Image.open(
            r"D:\Harsh\SEM 4\PYTHON\Hotel Management\Hotel Management\images\hotel2.png")  # r is used to make backward slash as forward slash
        img2 = img2.resize((100, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=2, y=0, width=100, height=50)

        #=================Labelframe====================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,padx=2,text="Customer Details",font=('Gabriola', 12, 'bold'))
        labelframeleft.place(x=5,y=50,width=425,height=445)

        #================labels and entry ==============
        #cust ref
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=('Arial', 10, 'bold'),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=('Arial', 12, 'bold'),state='readonly')
        entry_ref.grid(row=0,column=1)

        # cust name
        c_name = Label(labelframeleft, text="Customer Name", font=('Arial', 10, 'bold'), padx=2, pady=6)
        c_name.grid(row=1, column=0,sticky=W)

        entry_cname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name,font=('Arial', 12, 'bold'),width=29)
        entry_cname.grid(row=1, column=1)

        # mother name
        m_name = Label(labelframeleft, text="Mother Name", font=('Arial', 10, 'bold'), padx=2, pady=6)
        m_name.grid(row=2, column=0,sticky=W)

        entry_mname = ttk.Entry(labelframeleft,textvariable=self.var_mother,font=('Arial', 12, 'bold'),width=29)
        entry_mname.grid(row=2, column=1)

        # gender combobox
        gender_box = Label(labelframeleft, text="Gender:", font=('Arial', 10, 'bold'), padx=2, pady=6)
        gender_box.grid(row=3, column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=('Arial', 10, 'bold'),width=35,state="readonly")
        combo_gender["value"]=("Male","Female","other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #post code
        post_code = Label(labelframeleft, text="Post Code", font=('Arial', 10, 'bold'), padx=2, pady=6)
        post_code.grid(row=4, column=0, sticky=W)

        entry_pcode = ttk.Entry(labelframeleft,textvariable=self.var_post ,font=('Arial', 12, 'bold'), width=29)
        entry_pcode.grid(row=4, column=1)

        #mobile number
        mobile_no = Label(labelframeleft, text="Mobile Number", font=('Arial', 10, 'bold'), padx=2, pady=6)
        mobile_no.grid(row=5, column=0, sticky=W)

        entry_mno = ttk.Entry(labelframeleft, textvariable=self.var_mobile,font=('Arial', 12, 'bold'), width=29)
        entry_mno.grid(row=5, column=1)

        #email
        email = Label(labelframeleft, text="Email", font=('Arial', 10, 'bold'), padx=2, pady=6)
        email.grid(row=6, column=0, sticky=W)

        entry_email = ttk.Entry(labelframeleft, textvariable=self.var_email,font=('Arial', 12, 'bold'), width=29)
        entry_email.grid(row=6, column=1)

        # nationality
        nationality = Label(labelframeleft, text="Nationality:", font=('Arial', 10, 'bold'), padx=2, pady=6)
        nationality.grid(row=7, column=0, sticky=W)

        combo_nation = ttk.Combobox(labelframeleft,textvariable=self.var_nationality, font=('Arial', 10, 'bold'), width=35,state="readpnly")
        combo_nation["value"] = ("Indian", "America","British","Turkey")
        combo_nation.current(0)
        combo_nation.grid(row=7, column=1)

        #idproof type combobox
        id_proof = Label(labelframeleft, text="Id Proof type:", font=('Arial', 10, 'bold'), padx=2, pady=6)
        id_proof.grid(row=8, column=0, sticky=W)

        id_proof = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof,font=('Arial', 10, 'bold'), width=35,state="readonly")
        id_proof["value"] = ("AadharCard", "pancard", "Passport")
        id_proof.current(0)
        id_proof.grid(row=8, column=1)

        #id number
        id_no = Label(labelframeleft, text="Id Number", font=('Arial', 10, 'bold'), padx=2, pady=6)
        id_no.grid(row=9, column=0, sticky=W)

        entry_id = ttk.Entry(labelframeleft,textvariable=self.var_id_number, font=('Arial', 12, 'bold'), width=29)
        entry_id.grid(row=9, column=1)

        #address
        address = Label(labelframeleft, text="Address", font=('Arial', 10, 'bold'), padx=2, pady=6)
        address.grid(row=10, column=0, sticky=W)

        entry_add = ttk.Entry(labelframeleft, textvariable=self.var_address,font=('Arial', 12, 'bold'), width=29)
        entry_add.grid(row=10, column=1)

        #=================Buttons=====================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=370,width=312,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=('Arial', 12, 'bold'),bg='black',fg='gold',width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btndelete = Button(btn_frame, text="DELETE",command=self.delete, font=('Arial', 12, 'bold'), bg='black', fg='gold', width=9)
        btndelete.grid(row=0, column=2, padx=1)

        btnreset = Button(btn_frame, text="RESET", command=self.reset,font=('Arial', 12, 'bold'), bg='black', fg='gold', width=9)
        btnreset.grid(row=0, column=3, padx=1)

        #=================table frame==================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, padx=2, text="View Details",font=('Gabriola', 12, 'bold'))
        Table_Frame.place(x=435, y=50, width=862, height=345)
        #===================Show data Table===================

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=862,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile",
                                             "email","nationality","idproof","idnumber","address"),
                                             xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_details_Table.xview)
        scroll_y.config(command=self.Cust_details_Table.yview)

        self.Cust_details_Table.heading("ref",text="Refer No")
        self.Cust_details_Table.heading("name", text="Name")
        self.Cust_details_Table.heading("mother", text="Mother Name")
        self.Cust_details_Table.heading("gender", text="Gender")
        self.Cust_details_Table.heading("post", text="PostCode")
        self.Cust_details_Table.heading("mobile", text="Mobile No")
        self.Cust_details_Table.heading("email", text="Email")
        self.Cust_details_Table.heading("nationality", text="Nationality")
        self.Cust_details_Table.heading("idproof", text="Id Proof")
        self.Cust_details_Table.heading("idnumber", text="Id Number")
        self.Cust_details_Table.heading("address", text="Address")

        self.Cust_details_Table["show"]="headings"

        self.Cust_details_Table.column("ref", width=100)
        self.Cust_details_Table.column("name", width=100)
        self.Cust_details_Table.column("mother", width=100)
        self.Cust_details_Table.column("gender", width=100)
        self.Cust_details_Table.column("post", width=100)
        self.Cust_details_Table.column("mobile", width=100)
        self.Cust_details_Table.column("email", width=100)
        self.Cust_details_Table.column("nationality", width=100)
        self.Cust_details_Table.column("idproof", width=100)
        self.Cust_details_Table.column("idnumber", width=100)
        self.Cust_details_Table.column("address", width=100)

        self.Cust_details_Table.pack(fill=BOTH, expand=1)
        self.Cust_details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Warning","Pleas enter all the details",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",passwd="password",database="hotel")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_ref.get(),
                                                                                    self.var_cust_name.get(),
                                                                                    self.var_mother.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_post.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_nationality.get(),
                                                                                    self.var_id_proof.get(),
                                                                                    self.var_id_number.get(),
                                                                                    self.var_address.get()
                                                                                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("warning","something went wrong!:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="password", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_details_Table.delete(*self.Cust_details_Table.get_children())
            for i in rows:
                self.Cust_details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Cust_details_Table.focus()
        content=self.Cust_details_Table.item(cursor_row)
        row=content["values"]

        #self.var_ref.set(row[0]),
        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if delete>0:
            conn = mysql.connector.connect(host="localhost", user="root", password="password", database="hotel")
            my_cursor = conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

if __name__=="__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()