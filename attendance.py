from tkinter import *
from tkinter import ttk #stylish GUI
from PIL import Image,ImageTk #for images
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2
import os
import csv
from tkinter import filedialog
mydata=[]
class attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1980x1080+0+0")
        self.root.title("Attendance")

        # +++++++++++++variables+++++++++++++++++
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dept=StringVar()
        self.var_attendance_stat=StringVar()
        self.var_date=StringVar()
        self.var_time=StringVar()


        ##BACKGROUND IMAGE
        bg_img=Image.open(r"C:\Users\Sushant\OneDrive\Desktop\major project\images\background.jpg")
        bg_img=bg_img.resize((1980,1080),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(bg_img)

        ##setting image in window
        bg_lbl=Label(self.root,image=self.bgimg)
        bg_lbl.place(x=0,y=0,width=1980,height=1080)

        ## main Title 
        title_lbl=Label(root,text="CONTACTLESS ATTENDANCE SYSTEM",font=("bigjohnpro", 35,"bold"),bg="#E8FFF5" ,fg="blue")
        title_lbl.place(x=0,y=0,width=1980,height=120)

        ##Sub title
        sub_title=Label(root,text="ATTENDANCE DETAILS",font=("bigjohnpro", 35,"bold"),bg="#E8FFF5" ,fg="blue")
        sub_title.place(x=0,y=150,width=1980,height=50)

        ##main frame
        main_frame=Frame(bg_lbl,bd=2,bg="#719770")
        main_frame.place(x=10,y=215,width=1890,height=780)

        # left label frame

        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Information",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        left_frame.place(x=15,y=10,width=930,height=760)

        
       ##student info

        #student roll entry 
        student_rno=Label(left_frame,text="Student Id:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        student_rno.grid(row=0,column=0,pady=20,sticky="W")

        stud_roll_ent_field=ttk.Entry(left_frame,textvariable=self.var_roll,width=25,font=("bigjohnpro", 15,"bold"))
        stud_roll_ent_field.grid(row=0,column=1,sticky="W")

         #student name
        student_name=Label(left_frame,text="Name:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        student_name.grid(row=1,column=0,pady=20,sticky="W")

        stud_name_field=ttk.Entry(left_frame,textvariable=self.var_name,width=25,font=("bigjohnpro", 15,"bold"))
        stud_name_field.grid(row=1,column=1,sticky="W")

        dep_label=Label(left_frame,text="Department:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        dep_label.grid(row=2,column=0,sticky="w")
        
        ##selection box
        dep_combo=ttk.Combobox(left_frame,textvariable=self.var_dept,font=("bigjohnpro", 15,"bold"),width=17,state="readonly")
        dep_combo["values"]=("select Dept","Mechanical","Aero","CSE","IT","EEE","ECE")
        dep_combo.current(0)
        dep_combo.grid(row=2,column=1,pady=20)


        #student hallticket
        student_ht=Label(left_frame,text="Hallticket:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        student_ht.grid(row=3,column=0,pady=20,sticky="W")

        stud_ht_field=ttk.Entry(left_frame,textvariable=self.var_roll,width=25,font=("bigjohnpro", 15,"bold"))
        stud_ht_field.grid(row=3,column=1,sticky="W")

        #student entry time
        student_ent_time=Label(left_frame,text="Time:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        student_ent_time.grid(row=4,column=0,pady=10,sticky="W")

        stud_ent_time_field=ttk.Entry(left_frame,textvariable=self.var_time,width=25,font=("bigjohnpro", 15,"bold"))
        stud_ent_time_field.grid(row=4,column=1,sticky=W)

        student_ent_date=Label(left_frame,text="Date:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        student_ent_date.grid(row=5,column=0,pady=10,sticky="W")

        stud_ent_date_field=ttk.Entry(left_frame,textvariable=self.var_date,width=25,font=("bigjohnpro", 15,"bold"))
        stud_ent_date_field.grid(row=5,column=1,sticky=W)


         #student attendance status
        student_attendance_stat=Label(left_frame,text="Attendance:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        student_attendance_stat.grid(row=6,column=0,pady=20,sticky="W")

        gen_combo=ttk.Combobox(left_frame,text="",font=("bigjohnpro", 15,"bold"),state="readonly")
        gen_combo["values"]=("Status","Present","Absent")
        gen_combo.current(0)
        gen_combo.grid(row=6,column=1,sticky="W")
         
        
        ##buttons
        bttn_frame=LabelFrame(left_frame,bd=0,relief=FLAT,text="",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        bttn_frame.place(x=15,y=590,width=880,height=60)

        import_btn=Button(bttn_frame,command=self.import_csv,text="Import CSV",font=("bigjohnpro", 15,"bold"),width=36)
        import_btn.grid(row=0,column=0,pady=10)

        export_btn=Button(bttn_frame,command=self.export_csv,text="Export CSV",font=("bigjohnpro", 15,"bold"),width=35)
        export_btn.grid(row=0,column=1)

        bttn_frame1=Frame(left_frame,bd=0,relief=FLAT,bg="#A3CE99")
        bttn_frame1.place(x=15,y=530,width=885,height=60)

        update_btn=Button(bttn_frame1,text="Update",font=("bigjohnpro", 15,"bold"),width=36)
        update_btn.grid(row=0,column=0,pady=15)

        reset_btn=Button(bttn_frame1,command=self.reset_data,text="Reset",font=("bigjohnpro", 15,"bold"),width=35)
        reset_btn.grid(row=0,column=1)

         # right label frame

        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Information",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        right_frame.place(x=945,y=10,width=925,height=760)

         # search results

        search_frame=LabelFrame(right_frame,bd=2,relief=RAISED,text="Search query",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        search_frame.place(x=10,y=10,width=900,height=70)
        #search bar
        search_bar=Label(search_frame,text="search by:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        search_bar.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        searchby_combo=ttk.Combobox(search_frame,font=("bigjohnpro", 15),state="readonly",width=15)
        searchby_combo["values"]=("Select","Name","Hall Ticket","Email","phone")
        searchby_combo.current(0)
        searchby_combo.grid(row=0,column=1,pady=10)

        search_query_field=ttk.Entry(search_frame,width=40,font=("bigjohnpro", 15,"bold"))
        search_query_field.grid(row=0,column=2,padx=7)

        
        search_btn=Button(search_frame,text="Search",font=("bigjohnpro", 10,"bold"))
        search_btn.grid(row=0,column=3)

        show_btn=Button(search_frame,text="Showall",font=("bigjohnpro", 10,"bold"))
        show_btn.grid(row=0,column=4)



        #display actual results
        table_frame=LabelFrame(right_frame,bd=2,relief=RAISED,text="Search Results",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        table_frame.place(x=10,y=85,width=900,height=625)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("roll","name","dept","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("roll",text="Student Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("dept",text="Department")
        self.student_table.heading("time",text="Time")
        self.student_table.heading("date",text="Date")
        self.student_table.heading("attendance",text="Attendance Status")
        
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("dept",width=100)
        self.student_table.column("time",width=100)
        self.student_table.column("date",width=100)
        self.student_table.column("attendance",width=100)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        # self.fetch_data()

        # ++++++++++++++fetch data from csv file++++++++++++++++++
    def fetch_data(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("",END,values=i)
    
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File",".*csv"),("ALL File","*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)
    

    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File",".*csv"),("ALL File","*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data has been exported to"+os.path.basename(fln)+"Successfully!!")
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 

    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        rows=content['values']
        self.var_roll.set(rows[0])
        self.var_name.set(rows[1])
        self.var_dept.set(rows[2])
        self.var_time.set(rows[3])
        self.var_date.set(rows[4])
        self.var_attendance_stat.set(rows[5])

    def reset_data(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dept.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance_stat.set("")

            

if __name__ =="__main__":
    root=Tk()
    obj=attendance(root)
    root.mainloop()