from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_recognition



class Face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1400x790+0+0')
        self.root.title('face Recognition System')
        # image first
        img = Image.open(r"E:\python program\django project\face recognization\college_images\Stanford.jpg")
        img = img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second image
        img1 = Image.open(r"E:\python program\django project\face recognization\college_images\facialrecognition.png")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # third image
        img2 = Image.open(r"E:\python program\django project\face recognization\college_images\u.jpg")
        img2 = img2.resize((500, 130),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)


        # bg image
        img3 = Image.open(r"E:\python program\django project\face recognization\college_images\wp2551980.jpg")
        img3 = img3.resize((1400, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1400, height=710)

        title_lbl = Label(bg_img, text='FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE', font=('times new roman',35,'bold'),bg='white',fg='red')
        title_lbl.place(x=-15,y=0,width=1400,height=45)


        # student button
        img4 = Image.open(r"E:\python program\django project\face recognization\college_images\gettyimages-1022573162.jpg")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1 = Button(bg_img,image=self.photoimg4,command=self.student_details,cursor='hand2')
        b1.place(x=100,y=50,width=220,height=220)

        b1_1 = Button(bg_img,text='Student Details',command=self.student_details,cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=100,y=250,width=220,height=40)

        # detect face button
        img5 = Image.open(r"E:\python program\django project\face recognization\college_images\face_detector1.jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor='hand2',command=self.face_data)
        b1.place(x=400, y=50, width=220, height=220)

        b1_1 = Button(bg_img, text='Face Detector', cursor='hand2',command=self.face_data, font=('times new roman', 15, 'bold'),bg='darkblue', fg='white')
        b1_1.place(x=400, y=250, width=220, height=40)


        # Attendance Face Button
        img6 = Image.open(r"E:\python program\django project\face recognization\college_images\report.jpg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor='hand2')
        b1.place(x=700, y=50, width=220, height=220)

        b1_1 = Button(bg_img, text='Attendance', cursor='hand2', font=('times new roman', 15, 'bold'),bg='darkblue', fg='white')
        b1_1.place(x=700, y=250, width=220, height=40)



         # Help
        img7 = Image.open(r"E:\python program\django project\face recognization\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor='hand2')
        b1.place(x=1000, y=50, width=220, height=220)

        b1_1 = Button(bg_img, text='Help Desk', cursor='hand2', font=('times new roman', 15, 'bold'),bg='darkblue', fg='white')
        b1_1.place(x=1000, y=250, width=220, height=40)



         # Train 
        img8 = Image.open(r"E:\python program\django project\face recognization\college_images\Train.jpg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor='hand2',command=self.train_data)
        b1.place(x=100, y=310, width=220, height=220)

        b1_1 = Button(bg_img, text='Train Data', cursor='hand2',command=self.train_data, font=('times new roman', 15, 'bold'),bg='darkblue', fg='white')
        b1_1.place(x=100, y=510, width=220, height=40)


        # photos 
        img9 = Image.open(r"E:\python program\django project\face recognization\college_images\opencv_face_reco_more_data.jpg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor='hand2',command=self.open_img)
        b1.place(x=400, y=310, width=220, height=220)

        b1_1 = Button(bg_img, text='Photos', cursor='hand2',command=self.open_img, font=('times new roman', 15, 'bold'),bg='darkblue', fg='white')
        b1_1.place(x=400, y=510, width=220, height=40)



        # Developers 
        img10 = Image.open(r"E:\python program\django project\face recognization\college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor='hand2')
        b1.place(x=700, y=310, width=220, height=220)

        b1_1 = Button(bg_img, text='Developer', cursor='hand2', font=('times new roman', 15, 'bold'),bg='darkblue', fg='white')
        b1_1.place(x=700, y=510, width=220, height=40)



        # Exit
        img11 = Image.open(r"E:\python program\django project\face recognization\college_images\exit.jpg")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor='hand2')
        b1.place(x=1000, y=310, width=220, height=220)

        b1_1 = Button(bg_img, text='Exit', cursor='hand2', font=('times new roman', 15, 'bold'),bg='darkblue', fg='white')
        b1_1.place(x=1000, y=510, width=220, height=40)


    def open_img(self):
        os.startfile('data')



        # >>>>>>>>>>>>>>>>> FUNCTION BUTTON >>>>>>>>>>>>>>>
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


    
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)


    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)







if __name__ =='__main__':
    root = Tk()
    obj = Face_recognition_system(root)
    root.mainloop()
