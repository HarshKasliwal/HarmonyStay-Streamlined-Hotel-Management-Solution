from tkinter import *
from PIL import Image,ImageTk
from customer import Cust_win
from room import Roombooking
from details import DetailsRoom

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #==================1st Image================
        img1=Image.open(r"D:\Harsh\SEM 4\PYTHON\Hotel Management\Hotel Management\images\hotel1.png")  #r is used to make backward slash as forward slash
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        #==================Logo====================
        img2 = Image.open( r"D:\Harsh\SEM 4\PYTHON\Hotel Management\Hotel Management\images\hotel2.png")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        #===============title=======================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=('Gabriola',40,'bold'),bg="black",fg="gold",relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #=================Main Frame================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #================Menu=======================
        lbl_menu = Label(main_frame, text="MENU", font=('Gabriola',20, 'bold'), bg="black",fg="gold", relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        #===============btn frame===================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=55,width=228,height=300)

        cust_btn=Button(btn_frame,text="Customer",width=24,command=self.cust_details,font=("Gabriola",14,'bold'),bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="Room",command=self.roombooking, width=24, font=("Gabriola", 14, 'bold'), bg="black", fg="gold",bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="Details", width=24,command=self.detailsroom, font=("Gabriola", 14, 'bold'), bg="black", fg="gold",bd=0, cursor="hand2")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="Thank You", width=24, font=("Gabriola", 14, 'bold'), bg="black", fg="gold",bd=0, cursor="hand2")
        report_btn.grid(row=4, column=0, pady=1)

        logout_btn = Button(btn_frame, text="Exit", width=24, command=self.logout,font=("Gabriola", 14, 'bold'), bg="black", fg="gold",bd=0, cursor="hand2")
        logout_btn.grid(row=3, column=0, pady=1)

        #================right side image=============
        img3 = Image.open(r"D:\Harsh\SEM 4\PYTHON\Hotel Management\Hotel Management\images\hotel3.jpg")  
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1300, height=600)

        #================down images==================
        img4 = Image.open(r"D:\Harsh\SEM 4\PYTHON\Hotel Management\Hotel Management\images\hotel4.png") 
        img4 = img4.resize((230, 250), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg2 = Label(self.root, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=550, width=230, height=250)

    def cust_details(self):
         self.new_Window=Toplevel(self.root)
         self.app=Cust_win(self.new_Window)

    def roombooking(self):
         self.new_Window=Toplevel(self.root)
         self.app=Roombooking(self.new_Window)

    def detailsroom(self):
        self.new_Window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_Window)

    def logout(self):
        self.root.destroy()


if __name__ == '__main__':
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()