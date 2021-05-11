from tkinter import *
from tkinter import ttk #stylish GUI
from PIL import Image,ImageTk #for images
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2
import os
from tqdm.auto import tqdm
import numpy as np

class train_data:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1980x1080+0+0")
        self.root.title("Train data")

        bg_img=Image.open(r"C:\Users\Sushant\OneDrive\Desktop\major project\images\background.jpg")
        bg_img=bg_img.resize((1980,1080),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(bg_img)

        ##setting image in window
        bg_lbl=Label(self.root,image=self.bgimg)
        bg_lbl.place(x=0,y=0,width=1980,height=1080)

        ##Title 
        title_lbl=Label(root,text="CONTACTLESS ATTENDANCE SYSTEM",font=("bigjohnpro", 35,"bold"),bg="#E8FFF5" ,fg="blue")
        title_lbl.place(x=0,y=0,width=1980,height=120)

        sub_title=Label(root,text="Data Training",font=("bigjohnpro", 35,"bold"),bg="#E8FFF5" ,fg="blue")
        sub_title.place(x=0,y=150,width=1980,height=50)

        train_btn_img=Image.open(r"images\dat_train.jpg")
        train_btn_img=train_btn_img.resize((400,400),Image.ANTIALIAS)
        self.tbi=ImageTk.PhotoImage(train_btn_img)

        train_lbl=Label(bg_lbl,image=self.tbi)
        train_lbl.place(x=350,y=225,width=400,height=400)

        train_btn_img1=Image.open(r"images\dat_train1.jpg")
        train_btn_img1=train_btn_img1.resize((400,400),Image.ANTIALIAS)
        self.tbi1=ImageTk.PhotoImage(train_btn_img1)

        train_lbl1=Label(bg_lbl,image=self.tbi1)
        train_lbl1.place(x=750,y=225,width=400,height=400)

        train_btn_img2=Image.open(r"images\dat_train2.jpg")
        train_btn_img2=train_btn_img2.resize((400,400),Image.ANTIALIAS)
        self.tbi2=ImageTk.PhotoImage(train_btn_img2)

        train_lbl2=Label(bg_lbl,image=self.tbi2)
        train_lbl2.place(x=1150,y=225,width=400,height=400)

        train_btn=Button(bg_lbl,text="Train Data",command=self.train_classifier,cursor="hand2",fg="#008E80",font=("bigjohnpro",15),bg="#E8FFF5")
        train_btn.place(x=800,y=750,width=300,height=40)

        load_lbl=Label(bg_lbl,text="Training...",fg="#008E80",font=("bigjohnpro",15),bg="#E8FFF5")
        load_lbl.place(x=800,y=650,width=100,height=30)

        # load_anim=for i in tqdm(range(100001)):
        #                 print(" ",end ='\r')
        # anim_lbl=Label(bg_lbl,text="Training...",fg="#008E80",font=("bigjohnpro",15),bg="#E8FFF5")
        # anim_lbl.place(x=800,y=700,width=100,height=30)
    def train_classifier(self):
        data_dir=("stud_imgs")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')  #Grayscale image
            image_np=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training",image_np)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        
        # +++++++++++++++++Train the classifier++++++++++++
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")



                


                        












if __name__ =="__main__":
    root=Tk()
    obj=train_data(root)
    root.mainloop()