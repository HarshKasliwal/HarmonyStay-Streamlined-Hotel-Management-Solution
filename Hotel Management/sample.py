
        #lbl_searchBy = Label(Table_Frame, font=('Gabriola', 12, 'bold'), text="Search By:", bg='black', fg='white')
        #lbl_searchBy.grid(row=0, column=0, sticky=W, padx=2)

        #self.search_var = StringVar()
        #combo_search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=('Arial', 10, 'bold'), width=24,state="readonly")
        #combo_search["value"] = ("Contact", "Room")
        #combo_search.current(0)
        #combo_search.grid(row=0, column=1, padx=2)

        #self.text_search = StringVar()
        #txtSearch = ttk.Entry(Table_Frame, textvariable=self.text_search, font=('Arial', 12, 'bold'), width=22)
        #txtSearch.grid(row=0, column=2, padx=2)

        #btnSearch = Button(Table_Frame, text="Search", command=self.search ,font=('Arial', 12, 'bold'), bg='black',fg='gold', width=9)
        #btnSearch.grid(row=0, column=3, padx=1)

        #btnShowAll = Button(Table_Frame, text="Show All",command=self.fetch_data , font=('Arial', 12, 'bold'),bg='black', fg='gold', width=9)
        #btnShowAll.grid(row=0, column=4, padx=1)

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile no.",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="password", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
                                                                                self.var_contact.get(),
                                                                                self.var_checkin.get(),
                                                                                self.var_checkout.get(),
                                                                                self.var_roomtype.get(),
                                                                                self.var_roomavailable.get(),
                                                                                self.var_meal.get(),
                                                                                self.var_noofdays.get(),
                                                                                #self.var_contact.get()
                                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)