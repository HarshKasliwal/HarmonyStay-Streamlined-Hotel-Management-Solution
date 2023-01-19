from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk              #pip install pillow
from tkinter import messagebox
import mysql.connector
class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"D:\Harsh\SEM 4\PYTHON\Hotel Management\Hotel Management\images\login2.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"D:\Harsh\SEM 4\PYTHON\Hotel Management\Hotel Management\images\login3.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=100)

        #===============Lables================
        username=lbl=Label(frame,text="Username",font=("times new roman",16,"bold"),fg="black",bg="white")
        username.place(x=60,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password = lbl = Label(frame, text="Password", font=("times new roman", 16, "bold"), fg="black", bg="white")
        password.place(x=60, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        #============Icon Images=================
        img2 = Image.open(r"D:\Harsh\SEM 4\PYTHON\Hotel Management\Hotel Management\images\login3.jpg")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="white", borderwidth=0)
        lblimg2.place(x=650, y=325, width=25, height=25)

        img3 = Image.open(r"D:\Harsh\SEM 4\PYTHON\Hotel Management\Hotel Management\images\login5.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="white", borderwidth=0)
        lblimg3.place(x=650, y=395, width=25, height=25)

        #===============Login btn================
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman", 16, "bold"),bd=3,relief=RIDGE,fg="Black",bg="Red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #===============Register btn==============
        regstrbtn = Button(frame, text="New User Register", font=("times new roman", 10, "bold"), borderwidth=0, relief=RIDGE, fg="Black",
                          bg="white", activeforeground="white", activebackground="white")
        regstrbtn.place(x=20, y=350, width=160)

        #==========Forget Password===============
        forgetbtn = Button(frame, text="Forget Password", font=("times new roman", 10, "bold"), borderwidth=0, relief=RIDGE, fg="Black",
                          bg="white"
                             "", activeforeground="white", activebackground="white")
        forgetbtn.place(x=15, y=370, width=160)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fieds are required!")
        elif self.txtuser.get()=="Harsh" and self.txtpass.get()=="1234":
            messagebox.showinfo("Success","Welcome here...")
        else:
            messagebox.showerror("Error","Invalid Username and password")


if __name__== "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()