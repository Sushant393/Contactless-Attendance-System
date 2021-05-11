from tkinter import *
from tkinter import ttk #stylish GUI
from PIL import Image,ImageTk #for images
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2
import os
class add_students:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1980x1080+0+0")
        self.root.title("Add Student details")

        #+++++++++++++++++++variables+++++++++++++++
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_roll=StringVar()
        self.var_ht=StringVar()
        self.var_div=StringVar()
        self.var_gen=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_addr=StringVar()
        self.var_pcon=StringVar()
        self.var_pname=StringVar()
        self.var_dob=StringVar()
        self.var_name=StringVar()


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
        sub_title=Label(root,text="ADD STUDENT DETAILS",font=("bigjohnpro", 35,"bold"),bg="#E8FFF5" ,fg="blue")
        sub_title.place(x=0,y=150,width=1980,height=50)

        ##main frame
        main_frame=Frame(bg_lbl,bd=2,bg="#719770")
        main_frame.place(x=10,y=215,width=1890,height=780)

        # left label frame

        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Add Student Details",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        left_frame.place(x=15,y=10,width=930,height=760)

        
        # current course 

        cur_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Course Details",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        cur_course_frame.place(x=10,y=10,width=910,height=150)

        #adding department lables
        dep_label=Label(cur_course_frame,text="Department:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        dep_label.grid(row=0,column=0)
        
        ##selection box
        dep_combo=ttk.Combobox(cur_course_frame,textvariable=self.var_dept,font=("bigjohnpro", 15,"bold"),width=17,state="readonly")
        dep_combo["values"]=("select Dept","Mechanical","Aero","CSE","IT","EEE","ECE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,pady=10)

        ##course
        course_lbl=Label(cur_course_frame,text="Select Course:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        course_lbl.grid(row=0,column=4,padx=10,pady=10)

        course_combo=ttk.Combobox(cur_course_frame,textvariable=self.var_course,font=("bigjohnpro", 15,"bold"),state="readonly")
        course_combo["values"]=("Select course","B.Tech","M.Teach")
        course_combo.current(0)
        course_combo.grid(row=0,column=5,padx=10,pady=10)

         ##year
        year_lbl=Label(cur_course_frame,text="Select Year:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        year_lbl.grid(row=1,column=0)

        year_combo=ttk.Combobox(cur_course_frame,textvariable=self.var_year,font=("bigjohnpro", 15,"bold"),state="readonly")
        year_combo["values"]=("Select year","First","Second","Third","fourth")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,pady=10)

        ##semester
        sem_lbl=Label(cur_course_frame,text="Select semester:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        sem_lbl.grid(row=1,column=4,padx=10,pady=10)

        sem_combo=ttk.Combobox(cur_course_frame,textvariable=self.var_sem,font=("bigjohnpro", 15,"bold"),state="readonly")
        sem_combo["values"]=("Select sem","I","II")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=5,padx=10,pady=10)

        ##student info
        stud_info_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Student Details",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        stud_info_frame.place(x=10,y=165,width=910,height=550)

        #student roll entry 
        student_rno=Label(stud_info_frame,text="Student Id:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        student_rno.grid(row=0,column=0,padx=10,pady=10,sticky="W")

        stud_roll_ent_field=ttk.Entry(stud_info_frame,textvariable=self.var_roll,width=25,font=("bigjohnpro", 15,"bold"))
        stud_roll_ent_field.grid(row=0,column=1,sticky="W")

         #student name
        student_name=Label(stud_info_frame,text="Name:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        student_name.grid(row=0,column=2,padx=10,sticky="W")

        stud_name_field=ttk.Entry(stud_info_frame,textvariable=self.var_name,width=25,font=("bigjohnpro", 15,"bold"))
        stud_name_field.grid(row=0,column=3,sticky="W")

        #student div
        student_div=Label(stud_info_frame,text="Division:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        student_div.grid(row=1,column=0,padx=10,sticky="W")

        stud_div_combo=ttk.Combobox(stud_info_frame,textvariable=self.var_div,font=("bigjohnpro", 15,"bold"),state="readonly")
        stud_div_combo["values"]=("A","B","C","D")
        stud_div_combo.current(0)
        stud_div_combo.grid(row=1,column=1,sticky="W")

        #student hallticket
        student_ht=Label(stud_info_frame,text="Hallticket:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        student_ht.grid(row=1,column=2,padx=10,sticky="W")

        stud_ht_field=ttk.Entry(stud_info_frame,textvariable=self.var_ht,width=25,font=("bigjohnpro", 15,"bold"))
        stud_ht_field.grid(row=1,column=3,sticky="W")

        #student gender
        student_gen=Label(stud_info_frame,text="Gender:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        student_gen.grid(row=2,column=0,padx=10,pady=10,sticky="W")

        gen_combo=ttk.Combobox(stud_info_frame,textvariable=self.var_gen,font=("bigjohnpro", 15,"bold"),state="readonly")
        gen_combo["values"]=("Select gender","Male","Female","other")
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,sticky="W")

        #student phone
        student_phone=Label(stud_info_frame,text="Mobile no:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        student_phone.grid(row=2,column=2,padx=10,sticky="W")

        stud_phone_field=ttk.Entry(stud_info_frame,textvariable=self.var_phone,width=25,font=("bigjohnpro", 15,"bold"))
        stud_phone_field.grid(row=2,column=3,sticky=W)
         
         #student gmail
        student_email=Label(stud_info_frame,text="Email:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        student_email.grid(row=3,column=0,padx=10,sticky=W)

        stud_email_field=ttk.Entry(stud_info_frame,textvariable=self.var_email,width=25,font=("bigjohnpro", 15,"bold"))
        stud_email_field.grid(row=3,column=1,sticky=W)

         #student address
        student_add=Label(stud_info_frame,text="Address:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        student_add.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        stud_add_field=ttk.Entry(stud_info_frame,textvariable=self.var_addr,width=25,font=("bigjohnpro", 15,"bold"))
        stud_add_field.grid(row=4,column=1,sticky=W)

        ##Student DOB
        stud_dob=Label(stud_info_frame,text="DOB:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        stud_dob.grid(row=4,column=2,padx=10,pady=10,sticky=W)

        stud_dob_field=ttk.Entry(stud_info_frame,textvariable=self.var_dob,width=25,font=("bigjohnpro", 15,"bold"))
        stud_dob_field.grid(row=4,column=3,sticky=W)

         #parents name
        par_name=Label(stud_info_frame,text="Parent name:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        par_name.grid(row=5,column=0,padx=10,pady=10,sticky=W)

        par_name_field=ttk.Entry(stud_info_frame,textvariable=self.var_pname,width=25,font=("bigjohnpro", 15,"bold"))
        par_name_field.grid(row=5,column=1,sticky=W)

        #parents contact
        par_contact=Label(stud_info_frame,text="Parent contact:",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        par_contact.grid(row=5,column=2,padx=10,sticky=W)

        par_contact_field=ttk.Entry(stud_info_frame,textvariable=self.var_pcon,width=25,font=("bigjohnpro", 15,"bold"))
        par_contact_field.grid(row=5,column=3,sticky=W)

        ##radio buttons
        sam_photo=Label(stud_info_frame,text="Sample photo:",font=("bigjohnpro", 12,"bold"),bg="#A3CE99")
        sam_photo.grid(row=6,column=0,padx=10,pady=10)
        self.var_rd1=StringVar()
        rd1=ttk.Radiobutton(stud_info_frame,variable=self.var_rd1,text="Take sample photo",value="Yes")
        rd1.grid(row=7,column=1,pady=10)

        rd2=ttk.Radiobutton(stud_info_frame,variable=self.var_rd1,text="No sample photo",value="No")
        rd2.grid(row=7,column=2,pady=10)

        ##buttons
        bttn_frame=LabelFrame(left_frame,bd=0,relief=FLAT,text="",font=("bigjohnpro", 15,"bold"),bg="#A3CE99")
        bttn_frame.place(x=15,y=590,width=880,height=60)

        save_btn=Button(bttn_frame,command=self.add_record,text="Save",font=("bigjohnpro", 15,"bold"),width=18)
        save_btn.grid(row=0,column=0,pady=10)

        update_btn=Button(bttn_frame,command=self.update_data,text="Update",font=("bigjohnpro", 15,"bold"),width=18)
        update_btn.grid(row=0,column=1)

        del_btn=Button(bttn_frame,command=self.del_data,text="Delete",font=("bigjohnpro", 15,"bold"),width=17)
        del_btn.grid(row=0,column=2)

        res_btn=Button(bttn_frame,command=self.reset_data,text="Reset",font=("bigjohnpro", 15,"bold"),width=17)
        res_btn.grid(row=0,column=3)

        bttn_frame1=Frame(left_frame,bd=0,relief=FLAT,bg="#A3CE99")
        bttn_frame1.place(x=15,y=530,width=885,height=60)

        capt_btn=Button(bttn_frame1,command=self.gen_dataset,text="Capture Image",font=("bigjohnpro", 15,"bold"),width=36)
        capt_btn.grid(row=0,column=0,pady=15)

        upload_btn=Button(bttn_frame1,text="Upload Image",font=("bigjohnpro", 15,"bold"),width=36)
        upload_btn.grid(row=0,column=1)

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

        self.student_table=ttk.Treeview(table_frame,column=("roll","name","dept","course","year","sem","sec","contact","email","dob","gen","pcon","pname","addr","ht","samp_img_stat"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("roll",text="Student Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("dept",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("sec",text="section")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("gen",text="Gender")
        self.student_table.heading("pcon",text="Parent contact")
        self.student_table.heading("pname",text="Parent Name")
        self.student_table.heading("addr",text="Address")
        self.student_table.heading("ht",text="Hall Ticket")
        self.student_table.heading("samp_img_stat",text="sample image status")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    #++++++++++++++FUNCTION DECLERATION+++++++++++++++++++++

    def add_record(self):
        if self.var_dept.get()=="select Department" or self.var_div.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_gen.get()=="" or self.var_addr.get()=="" or self.var_course.get()=="Select course" or self.var_name.get()=="" or self.var_roll.get()=="" or self.var_year.get()=="Select year" or self.var_sem.get()=="Select semester" or self.var_ht.get()=="" or self.var_phone.get()=="" or self.var_pname.get()=="" or self.var_pcon.get()=="" or self.var_rd1.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="root",database="cas_db")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_dept.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_div.get(),
                        self.var_phone.get(),
                        self.var_email.get(),
                        self.var_dob.get(),
                        self.var_gen.get(),
                        self.var_pcon.get(),
                        self.var_pname.get(),
                        self.var_addr.get(),
                        self.var_rd1.get(),
                        self.var_ht.get()     
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Students added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    # +++++++++++++++Fetch and preview data on right side++++++++++++++++++++
    def fetch_data(self):
        conn=mysql.connector.connect(host="127.0.0.1",username="root",password="root",database="cas_db")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    # +++++++++++++++++++++++++++update++++++++++++++
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_roll.set(data[0]),
        self.var_name.set(data[1]),
        self.var_dept.set(data[2]),
        self.var_course.set(data[3]),
        self.var_year.set(data[4]),
        self.var_sem.set(data[5]),
        self.var_div.set(data[6]),
        self.var_phone.set(data[7]),
        self.var_email.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_gen.set(data[10]),
        self.var_pcon.set(data[11]),
        self.var_pname.set(data[12]),
        self.var_addr.set(data[13]),
        self.var_rd1.set(data[14]),
        self.var_ht.set(data[15])  
    
    # +++++++++++++++++update function+++++++++++++++++++++++++
    def update_data(self):
        if self.var_dept.get()=="select Department" or self.var_div.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_gen.get()=="" or self.var_addr.get()=="" or self.var_course.get()=="Select course" or self.var_name.get()=="" or self.var_roll.get()=="" or self.var_year.get()=="Select year" or self.var_sem.get()=="Select semester" or self.var_ht.get()=="" or self.var_phone.get()=="" or self.var_pname.get()=="" or self.var_pcon.get()=="" or self.var_rd1.get()=="":
           messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                modify=messagebox.askyesno("modify","Do you want to modify student details",parent=self.root)
                if modify>0:
                    conn=mysql.connector.connect(host="127.0.0.1",username="root",password="root",database="cas_db")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set rollno=%s,name=%s,dept=%s,course=%s,year=%s,sem=%s,sec=%s,contact=%s,email=%s,dob=%s,gen=%s,pcon=%s,pname=%s,addr=%s,ht=%s,samp_img_stat=%s where rollno=%s",(
                            self.var_roll.get(),
                            self.var_name.get(),
                            self.var_dept.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_div.get(),
                            self.var_phone.get(),
                            self.var_email.get(),
                            self.var_dob.get(),
                            self.var_gen.get(),
                            self.var_pcon.get(),
                            self.var_pname.get(),
                            self.var_addr.get(),
                            self.var_rd1.get(),
                            self.var_ht.get(),
                            self.var_roll.get()    
                    ))
                      
                else:
                    if not modify:
                        return
                # conn.autocommit(True)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Succcess","Details modified successfully",parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    
    # ++++++++++++++++delete++++++++++++
    def del_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Roll number is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Delete record?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="127.0.0.1",username="root",password="root",database="cas_db")
                    my_cursor=conn.cursor()
                    sql="delete from student where rollno=%s"
                    val=(self.var_roll.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Record deleted successfully",parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    # ++++++++++++++++++Reset++++++++++++++++++++++++
    def reset_data(self):
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_dept.set("select Department"),
        self.var_course.set("Select course"),
        self.var_year.set("Select year"),
        self.var_sem.set("Select sem"),
        self.var_div.set("A"),
        self.var_phone.set(""),
        self.var_email.set(""),
        self.var_dob.set(""),
        self.var_gen.set("Select gender"),
        self.var_pcon.set(""),
        self.var_pname.set(""),
        self.var_addr.set(""),
        self.var_rd1.set(""),
        self.var_ht.set("")


    # ++++++++++++++++++++++++Generate dataset and take photo sample++++++++++++++++++++++++
    def gen_dataset(self):
        if self.var_dept.get()=="select Department" or self.var_div.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_gen.get()=="" or self.var_addr.get()=="" or self.var_course.get()=="Select course" or self.var_name.get()=="" or self.var_roll.get()=="" or self.var_year.get()=="Select year" or self.var_sem.get()=="Select semester" or self.var_ht.get()=="" or self.var_phone.get()=="" or self.var_pname.get()=="" or self.var_pcon.get()=="" or self.var_rd1.get()=="":
           messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="root",database="cas_db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set rollno=%s,name=%s,dept=%s,course=%s,year=%s,sem=%s,sec=%s,contact=%s,email=%s,dob=%s,gen=%s,pcon=%s,pname=%s,addr=%s,ht=%s,samp_img_stat=%s where rollno=%s",(
                            self.var_roll.get(),
                            self.var_name.get(),
                            self.var_dept.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_div.get(),
                            self.var_phone.get(),
                            self.var_email.get(),
                            self.var_dob.get(),
                            self.var_gen.get(),
                            self.var_pcon.get(),
                            self.var_pname.get(),
                            self.var_addr.get(),
                            self.var_rd1.get(),
                            self.var_ht.get(),
                            self.var_roll.get()    
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                # +++++++++++++Load predefined data on frontal face from open cv+++++++++++++
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbor=5
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="stud_imgs/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed",parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)





                    
if __name__ =="__main__":
    root=Tk()
    obj=add_students(root)
    root.mainloop()