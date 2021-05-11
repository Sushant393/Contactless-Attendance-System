from tkinter import *
from tkinter import ttk #stylish GUI
from PIL import Image,ImageTk #for images
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2
import os
from time import strftime
from datetime import datetime
from tqdm.auto import tqdm
import numpy as np
# coord=[]

class face_recognizer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1980x1080+0+0")
        self.root.title("Face recognition System")
        bg_img=Image.open(r"C:\Users\Sushant\OneDrive\Desktop\major project\images\background.jpg")
        bg_img=bg_img.resize((1980,1080),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(bg_img)

        ##setting image in window
        bg_lbl=Label(self.root,image=self.bgimg)
        bg_lbl.place(x=0,y=0,width=1980,height=1080)

        ##Title 
        title_lbl=Label(root,text="CONTACTLESS ATTENDANCE SYSTEM",font=("bigjohnpro", 35,"bold"),bg="#E8FFF5" ,fg="blue")
        title_lbl.place(x=0,y=0,width=1980,height=120)

        sub_title=Label(root,text="Face Recognition",font=("bigjohnpro", 35,"bold"),bg="#E8FFF5" ,fg="blue")
        sub_title.place(x=0,y=150,width=1980,height=50)

        recog_btn_img=Image.open(r"images\face_recog.jpg")
        recog_btn_img=recog_btn_img.resize((400,400),Image.ANTIALIAS)
        self.rbi=ImageTk.PhotoImage(recog_btn_img)

        recog_lbl=Label(bg_lbl,image=self.rbi)
        recog_lbl.place(x=350,y=225,width=400,height=400)

        recog_btn_img1=Image.open(r"images\face_recog1.jpg")
        recog_btn_img1=recog_btn_img1.resize((400,400),Image.ANTIALIAS)
        self.rbi1=ImageTk.PhotoImage(recog_btn_img1)

        recog_lbl1=Label(bg_lbl,image=self.rbi1)
        recog_lbl1.place(x=750,y=225,width=400,height=400)

        recog_btn_img2=Image.open(r"images\face_recog2.jpg")
        recog_btn_img2=recog_btn_img2.resize((400,400),Image.ANTIALIAS)
        self.rbi2=ImageTk.PhotoImage(recog_btn_img2)

        recog_lbl2=Label(bg_lbl,image=self.rbi2)
        recog_lbl2.place(x=1150,y=225,width=400,height=400)

        recog_btn=Button(bg_lbl,command=self.face_recog,text="Start Recognizor",cursor="hand2",fg="#008E80",font=("bigjohnpro",15),bg="#E8FFF5")
        recog_btn.place(x=800,y=750,width=300,height=40)

        # recog_lbl=Label(bg_lbl,text="Training...",fg="#008E80",font=("bigjohnpro",15),bg="#E8FFF5")
        # recog_lbl.place(x=800,y=650,width=100,height=30)

    # +++++++++++++++++++++attendance+++++++++++++++
    def mark_attendance(self,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            mydata=f.readlines()
            name_list=[]
            for line in mydata:
                entry=line.split((","))
                name_list.append((entry[0]))
            if((r not in name_list) and (n not in name_list) and (d not in name_list)) :
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{r},{n},{d},{dtString},{d1},Present")




    # +++++++++++++++++++++face recognition++++++++++++++++
    def face_recog(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="root",database="cas_db")
                my_cursor=conn.cursor()
                my_cursor.execute("select name from student where rollno="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select rollno from student where rollno="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select dept from student where rollno="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)


                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
                    cv2.putText(img,f"dept:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
                    self.mark_attendance(r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(img,"Unknown face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
                coord=[x,y,w,y]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundry(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
        
        while True:
            ret,img=cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognizer",img)
            if cv2.waitKey(1)==13:
                break
        cap.release()
        cv2.destroyAllWindows()



if __name__ =="__main__":
    root=Tk()
    obj=face_recognizer(root)
    root.mainloop()