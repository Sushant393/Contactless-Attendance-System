from tkinter import *
from tkinter import ttk #stylish GUI
from PIL import Image,ImageTk #for images
from student import add_students
import os
from train import train_data
from face_recognizer import face_recognizer
from attendance import attendance
import tkinter

class contactless_Attendance_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1980x1080+0+0")
        self.root.title("Contactless Attendance System")

        ##BACKGROUND IMAGE
        bg_img=Image.open(r"C:\Users\Sushant\OneDrive\Desktop\major project\images\background.jpg")
        bg_img=bg_img.resize((1980,1080),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(bg_img)

        ##setting image in window
        bg_lbl=Label(self.root,image=self.bgimg)
        bg_lbl.place(x=0,y=0,width=1980,height=1080)

        ##Title 
        title_lbl=Label(root,text="CONTACTLESS ATTENDANCE SYSTEM",font=("bigjohnpro", 35,"bold"),bg="#E8FFF5" ,fg="blue")
        title_lbl.place(x=0,y=0,width=1980,height=150)

        ##buttons
        #student details button
        stud_btn_img=Image.open(r"C:\Users\Sushant\OneDrive\Desktop\major project\images\stud_img.png")
        stud_btn_img=stud_btn_img.resize((200,200),Image.ANTIALIAS)
        self.sbi=ImageTk.PhotoImage(stud_btn_img)

        sbtn_img_lbl=Label(bg_lbl,image=self.sbi)
        sbtn_img_lbl.place(x=100,y=225,width=200,height=200)

        b1=Button(bg_lbl,text="Student Details",command=self.add_record,cursor="hand2",fg="#008E80",font=("bigjohnpro",15),bg="#E8FFF5")
        b1.place(x=100,y=400,width=200,height=40)

        #Detect face button
        detface_btn_img=Image.open(r"C:\Users\Sushant\OneDrive\Desktop\major project\images\det_face.jpg")
        detface_btn_img=detface_btn_img.resize((200,200),Image.ANTIALIAS)
        self.detface=ImageTk.PhotoImage(detface_btn_img)

        detface_img_lbl=Label(bg_lbl,image=self.detface)
        detface_img_lbl.place(x=350,y=225,width=200,height=200)

        b2=Button(bg_lbl,text="Detect Face",command=self.recognizer,cursor="hand2",fg="#008E80",font=("bigjohnpro",15),bg="#E8FFF5")
        b2.place(x=350 ,y=400,width=200,height=40)

        #attendance button
        att_btn_img=Image.open(r"C:\Users\Sushant\OneDrive\Desktop\major project\images\att.png")
        att_btn_img=att_btn_img.resize((200,200),Image.ANTIALIAS)
        self.att_bi=ImageTk.PhotoImage(att_btn_img)

        abtn_img_lbl=Label(bg_lbl,image=self.att_bi)
        abtn_img_lbl.place(x=600,y=225,width=200,height=200)

        b3=Button(bg_lbl,command=self.attendance_btn,text="Attendance",cursor="hand2",fg="#008E80",font=("bigjohnpro",15),bg="#E8FFF5")
        b3.place(x=600,y=400,width=200,height=40)

        #Train data button
        train_btn_img=Image.open(r"images\train_data.jpg")
        train_btn_img=train_btn_img.resize((200,200),Image.ANTIALIAS)
        self.tbi=ImageTk.PhotoImage(train_btn_img)

        tbtn_img_lbl=Label(bg_lbl,image=self.tbi)
        tbtn_img_lbl.place(x=100,y=550,width=200,height=200)

        b4=Button(bg_lbl,text="Train Data",command=self.train,cursor="hand2",fg="#008E80",font=("bigjohnpro",15),bg="#E8FFF5")
        b4.place(x=100,y=750,width=200,height=40)

        #photos button
        stud_pics_btn_img=Image.open(r"images\gallery.png")
        stud_pics_btn_img=stud_pics_btn_img.resize((200,200),Image.ANTIALIAS)
        self.spbi=ImageTk.PhotoImage(stud_pics_btn_img)

        spbtn_img_lbl=Label(bg_lbl,image=self.spbi)
        spbtn_img_lbl.place(x=350,y=550,width=200,height=200)

        b5=Button(bg_lbl,command=self.open_img,text="Photos",cursor="hand2",fg="#008E80",font=("bigjohnpro",15),bg="#E8FFF5")
        b5.place(x=350,y=750,width=200,height=40)

        #Exit button
        exit_btn_img=Image.open(r"images\exit.png")
        exit_btn_img=exit_btn_img.resize((200,200),Image.ANTIALIAS)
        self.ebi=ImageTk.PhotoImage(exit_btn_img)

        exit_img_lbl=Label(bg_lbl,image=self.ebi)
        exit_img_lbl.place(x=600,y=550,width=200,height=200)

        b6=Button(bg_lbl,command=self.exit_prog,text="Exit",cursor="hand2",fg="#008E80",font=("bigjohnpro",15),bg="#E8FFF5")
        b6.place(x=600,y=750,width=200,height=40)

        # right_accent_img=Image.open(r"C:\Users\Sushant\OneDrive\Desktop\major project\images\face_recog.jpg")
        # right_accent_img=right_accent_img.resize((1024,819),Image.ANTIALIAS)
        # self.rai=ImageTk.PhotoImage(right_accent_img)

        # acnt_img_lbl=Label(bg_lbl,image=self.rai)
        # acnt_img_lbl.place(x=900,y=225,width=900,height=750)



     # ++++++++++FUNCTION BUTTONS+++++++++++++++

    def add_record(self):
        self.new_window=Toplevel(self.root)
        self.app=add_students(self.new_window)
    

    def open_img(self):
        os.startfile("stud_imgs")

    def train(self):
        self.new_window=Toplevel(self.root)
        self.app=train_data(self.new_window)

    def recognizer(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognizer(self.new_window)    


    def attendance_btn(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)    

    def exit_prog(self):
        self.exit_prog=tkinter.messagebox.askyesno("Exit","Are you Sure?",parent=self.root)
        if self.exit_prog>0:
            self.root.destroy()
        else:
            return

    



    



if __name__=="__main__":
    root=Tk()
    obj=contactless_Attendance_System(root)
    root.mainloop()