from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root = root 
        self.root.geometry('1400x790+0+0')
        self.root.title('face Recognition System')


        # >>>>>>>>>>>>> variables >>>>>>>>>>>>>>
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()


        # image first
        img = Image.open(r"E:\python program\django project\face recognization\college_images\sample.jpg")
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
        img2 = Image.open(r"E:\python program\django project\face recognization\college_images\smart-attendance.jpg")
        img2 = img2.resize((500, 130),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)


        # bg image
        img3 = Image.open(r"E:\python program\django project\face recognization\college_images\wp2551980.jpg")
        img3 = img3.resize((1400, 610), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1400, height=710)

        title_lbl = Label(bg_img, text='STUDENT MAANAGEMENT SYSTEM', font=('times new roman',35,'bold'),bg='white',fg='darkgreen')
        title_lbl.place(x=-15,y=0,width=1400,height=45)

        main_frame = Frame(bg_img,bd=2,bg='white')
        main_frame.place(x=10,y=55,width=1345,height=600)

        # Left label frame
        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text='Student Details',font=('times new roman',12,'bold'),bg='white')
        Left_frame.place(x=0,y=0,width=650,height=580)

        # img_left = Image.open(r"E:\python program\django project\face recognization\college_images\AdobeStock_303989091.jpeg")
        # img_left = img_left.resize((630, 130),Image.Resampling.LANCZOS)
        # self.photoimg_left = ImageTk.PhotoImage(img_left)

        # f_lbl = Label(Left_frame, image=self.photoimg_left)
        # f_lbl.place(x=5, y=0, width=630, height=130)
        

        # Currunt course 
        currunt_course_frame = LabelFrame(Left_frame,bd=2,relief=RIDGE,text='Currunt Course Information',font=('times new roman',12,'bold'),bg='white')
        currunt_course_frame.place(x=5,y=0,width=615,height=120)


        # >>>>>>>>>>>>> DEPARTMENT >>>>>>>>>>>>>
        dep_label = Label(currunt_course_frame,text='Department',font=('times new roman',12,'bold'),bg='white')
        dep_label.grid(row=0,column=0,padx=10,)

        dep_combo = ttk.Combobox(currunt_course_frame,textvariable=self.var_dep,font=('times new roman',12,'bold'),width=17,state='readonly')
        dep_combo['values'] = ('Select Department','computer science','biotech','bio chemistery')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        # course 
        course_label = Label(currunt_course_frame,text='Course',font=('times new roman',12,'bold'),bg='white')
        course_label.grid(row=0,column=2,padx=10,)

        course_combo = ttk.Combobox(currunt_course_frame,textvariable=self.var_course,font=('times new roman',12,'bold'),width=17,state='readonly')
        course_combo['values'] = ('Select The Course','English','Hindi','Marathi','Spanish')
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        # Year 
        year_label = Label(currunt_course_frame,text='Year',font=('times new roman',12,'bold'),bg='white')
        year_label.grid(row=1,column=0,padx=10,)

        year_combo = ttk.Combobox(currunt_course_frame,textvariable=self.var_year,font=('times new roman',12,'bold'),width=17,state='readonly')
        year_combo['values'] = ('Select Year',2015,2016,2017,2018,2019,2020,2021,2022,2023)
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        # Semester
        sem_label = Label(currunt_course_frame,text='Semester',font=('times new roman',12,'bold'),bg='white')
        sem_label.grid(row=1,column=2,padx=10,)

        sem_combo = ttk.Combobox(currunt_course_frame,textvariable=self.var_semester,font=('times new roman',12,'bold'),width=17,state='readonly')
        sem_combo['values'] = ('Select Semester',1,2,3,4,5,6)
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        # Class Student information
        class_student_frame = LabelFrame(Left_frame,bd=2,relief=RIDGE,text='Class Student information',font=('times new roman',12,'bold'),bg='white')
        class_student_frame.place(x=5,y=120,width=615,height=400)


        # Student Id 
        studentId_label = Label(class_student_frame,text='Id',font=('times new roman',12,'bold'),bg='white')
        studentId_label.grid(row=0,column=0,padx=10,pady=4)

        studentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=('times new roman',13,'bold'))
        studentId_entry.grid(row=0,column=1,padx=10,pady=4,sticky=W)


        # Student Name 
        student_name_label = Label(class_student_frame,text='Name',font=('times new roman',12,'bold'),bg='white')
        student_name_label.grid(row=0,column=2,padx=10,pady=4)

        student_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name, width=20,font=('times new roman',13,'bold'))
        student_name_entry.grid(row=0,column=3,padx=10,pady=4,sticky=W)


        # Class Division
        class_division_label = Label(class_student_frame,text='Division',font=('times new roman',12,'bold'),bg='white')
        class_division_label.grid(row=1,column=0,padx=10,pady=4)

        # class_division_entry = ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=('times new roman',13,'bold'))
        # class_division_entry.grid(row=1,column=1,padx=10,pady=4,sticky=W)

        class_division_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font=('times new roman',12,'bold'),width=20,state='readonly')
        class_division_combo['values'] = ('Select Division','A','B','C')
        class_division_combo.current(0)
        class_division_combo.grid(row=1,column=1,padx=10,pady=4,sticky=W)

        


        # Roll No
        roll_no_label = Label(class_student_frame,text='Roll No',font=('times new roman',12,'bold'),bg='white')
        roll_no_label.grid(row=1,column=2,padx=10,pady=4)

        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=('times new roman',13,'bold'))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=4,sticky=W)


        # Gender 
        gender_label = Label(class_student_frame,text='Gender',font=('times new roman',12,'bold'),bg='white')
        gender_label.grid(row=2,column=0,padx=10,pady=4)

        # gender_entry = ttk.Entry(class_student_frame,width=20,font=('times new roman',13,'bold'))
        # gender_entry.grid(row=2,column=1,padx=10,pady=4,sticky=W)
        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=('times new roman',12,'bold'),width=20,state='readonly')
        gender_combo['values'] = ('Select Gender','Male','Female','Other')
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=4,sticky=W)


        # Dob
        dob_label = Label(class_student_frame,text='DOB',font=('times new roman',12,'bold'),bg='white')
        dob_label.grid(row=2,column=2,padx=10,pady=4)

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=('times new roman',13,'bold'))
        dob_entry.grid(row=2,column=3,padx=10,pady=4,sticky=W)


        # Email
        email_label = Label(class_student_frame,text='Email',font=('times new roman',12,'bold'),bg='white')
        email_label.grid(row=3,column=0,padx=10,pady=4)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=('times new roman',13,'bold'))
        email_entry.grid(row=3,column=1,padx=10,pady=4,sticky=W)


        # phone_no
        phone_no_label = Label(class_student_frame,text='Phone:',font=('times new roman',12,'bold'),bg='white')
        phone_no_label.grid(row=3,column=2,padx=10,pady=4)

        phone_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=('times new roman',13,'bold'))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=4,sticky=W)

        # address
        address_label = Label(class_student_frame,text='Address',font=('times new roman',12,'bold'),bg='white')
        address_label.grid(row=4,column=0,padx=10,pady=4)

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=('times new roman',13,'bold'))
        address_entry.grid(row=4,column=1,padx=10,pady=4,sticky=W)

        # Tehacher Name
        phone_no_label = Label(class_student_frame,text='Theacher',font=('times new roman',12,'bold'),bg='white')
        phone_no_label.grid(row=4,column=2,padx=10,pady=4)

        phone_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=('times new roman',13,'bold'))
        phone_no_entry.grid(row=4,column=3,padx=10,pady=4,sticky=W)



        # Radion Buttons >>>>
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text='Photo Sample',value='Yes')
        radiobtn1.grid(row=5,column=0)

        
        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text='No Sample',value='No')
        radiobtn2.grid(row=5,column=1)

        # Buttons frame
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=200,width=610,height=35)

        save_btn = Button(btn_frame,text='Save',command=self.add_dada,width=15,font=('times new roman',13,'bold'),bg='blue',fg='white')
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text='Update',command=self.update_data,width=15,font=('times new roman',13,'bold'),bg='yellow',fg='black')
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text='Delete',command=self.delete_data,width=15,font=('times new roman',13,'bold'),bg='red',fg='black')
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text='Reset',command=self.reset_data,width=15,font=('times new roman',13,'bold'),bg='green',fg='black')
        reset_btn.grid(row=0,column=3)


        btn1_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg='white')
        btn1_frame.place(x=0,y=235,width=610,height=35)

        take_photo_btn = Button(btn1_frame,command=self.generate_dataset, text='Take Photo Sample',width=29,font=('times new roman',13,'bold'),bg='blue',fg='white')
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn = Button(btn1_frame,text='Update Photo Sample',width=31,font=('times new roman',13,'bold'),bg='blue',fg='white')
        update_photo_btn.grid(row=0,column=1)










        # Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Student About',font=('times new roman',12,'bold'))
        Right_frame.place(x=660,y=0,width=675,height=580)

        # image 


        # image 


        # >>>>>>>>>> SEARCH SYSTEM >>>>>>>>>>>>

        search_frame = LabelFrame(Right_frame,bd=2,relief=RIDGE,text='Search System',font=('times new roman',12,'bold'),bg='white')
        search_frame.place(x=5,y=0,width=660,height=70)

        searcg_label = Label(search_frame,text='Seach By',font=('times new roman',15,'bold'),bg='red',fg='white')
        searcg_label.grid(row=0,column=0,padx=10,pady=4)

        search_combo = ttk.Combobox(search_frame,font=('times new roman',12,'bold'),width=14,state='readonly')
        search_combo['values'] = ('Select ','Roll_no','Phone_No')
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(search_frame,width=20,font=('times new roman',13,'bold'))
        search_entry.grid(row=0,column=2,padx=10,pady=4,sticky=W)




        search_btn = Button(search_frame,text='Search',width=9,font=('times new roman',10,'bold'),bg='red',fg='black')
        search_btn.grid(row=0,column=3,padx=4)

        searchAll_btn = Button(search_frame,text='Show All',width=9,font=('times new roman',10,'bold'),bg='green',fg='black')
        searchAll_btn.grid(row=0,column=4,padx=4)


        # >>>>>>>>>>> TABLE FRAME >>>>>>>>>>>>
        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=5,y=80,width=660,height=350)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,columns=('department','course','year','semester','id','name','div','roll','gender','dob','email','phone','address','teacher','photo'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM,fill= X)
        scroll_y.pack(side= RIGHT , fill = Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('department',text='Department')
        self.student_table.heading('course',text='Course')
        self.student_table.heading('year',text='Year')
        self.student_table.heading('semester',text='Semester')
        self.student_table.heading('id',text='StudentId')
        self.student_table.heading('name',text='Name')
        self.student_table.heading('div',text='Division')
        self.student_table.heading('roll',text='Roll No')
        self.student_table.heading('gender',text='Gender')
        self.student_table.heading('dob',text='DOB')
        self.student_table.heading('email',text='email')
        self.student_table.heading('phone',text='Phone')
        self.student_table.heading('address',text='Addresss')
        self.student_table.heading('teacher',text='Theacher')
        self.student_table.heading('photo',text='PhotosampleStatus')
        self.student_table['show'] = 'headings'

        self.student_table.column('department',width=150)
        self.student_table.column('course',width=150)
        self.student_table.column('year',width=100)
        self.student_table.column('semester',width=100)
        self.student_table.column('id',width=100)
        self.student_table.column('name',width=200)
        self.student_table.column('div',width=50)
        self.student_table.column('roll',width=100)
        self.student_table.column('gender',width=50)
        self.student_table.column('dob',width=100)
        self.student_table.column('email',width=200)
        self.student_table.column('phone',width=100)
        self.student_table.column('address',width=250)
        self.student_table.column('teacher',width=200)
        self.student_table.column('photo',width=150)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # >>>>>>>>>>>>>>>>>>>>>>>> function description >>>>>>>>>>>
    def add_dada(self):
        if self.var_dep.get() == 'Select Department' or self.var_std_name.get()=='' or self.var_std_id.get() == '':
            messagebox.showerror('Error','All Fields are required',parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='Pranav@123',database='face_recognizer')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Student details has been added successfully',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f" Due To :{str(es)}",parent=self.root)

        



    # >>>>>>>>>>>>>>>>> FETCH DATA >>>>>>>>>>>>>>>>>>
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='Pranav@123',database='face_recognizer')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from student')
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('',END,values=i)
            conn.commit()
        conn.close()



    # >>>>>>>>>>>>> get Cursor
    def get_cursor(self,event=''):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data  = content['values']

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])



    # update function
    def update_data(self):
        if self.var_dep.get() == 'Select Department' or self.var_std_name.get()=='' or self.var_std_id.get() == '':
            messagebox.showerror('Error','All Fields are required',parent=self.root)
        else:
            try:
                Update = messagebox.askyesno('Update','Do you want to update this student details',parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host='localhost',username='root',password='Pranav@123',database='face_recognizer')
                    my_cursor = conn.cursor()
                    my_cursor.execute('update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosamaple=%s where Student_id=%s',(
                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                self.var_std_id.get()
                                                                                                                                                                                                                ))
                else:
                    if not Update:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Student Details successfully Updated',parent=self.root)
                
            except Exception as es:
                messagebox.showerror('Error',f"{str(es)}",parent=self.root)


    def delete_data(self):
        if self.var_std_id.get()== '':
            messagebox.showerror('error','Student Id Must be requred ', parent=self.root)
        else:
            try:
                delete = messagebox.askyesno('Conformation','Do you want to delete',parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host='localhost',username='root',password='Pranav@123',database='face_recognizer')
                    my_cursor = conn.cursor()
                    sql = 'delete from student where Student_id =%s'
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Deleted',"Successfully Deleted ",parent=self.root)
            except Exception as es:
                messagebox.showerror('error',f"{str(es)}",parent=self.root)




    # reset
    def reset_data(self):
        self.var_dep.set('Select Department')
        self.var_course.set('Select The Course')
        self.var_year.set('Selsect Year')
        self.var_semester.set('Select Semsester')
        self.var_std_id.set('')
        self.var_std_name.set('')
        self.var_div.set('Select Division')
        self.var_roll.set('')
        self.var_gender.set('Select Gender')
        self.var_dob.set('')
        self.var_email.set('')
        self.var_phone.set('')
        self.var_address.set('')
        self.var_teacher.set('')
        self.var_radio1.set('')




    # >>>>>>>>>>>>>>>>>>>>>> GENERATE DATA SET OR TAKE PHOTO SAMPLE >>>>>>>>>>>>>>>>>
    def generate_dataset(self):
        if self.var_dep.get() == 'Select Department' or self.var_std_name.get()=='' or self.var_std_id.get() == '':
            messagebox.showerror('Error','All Fields are required',parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='Pranav@123',database='face_recognizer')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from student')
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute('update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosamaple=%s where Student_id=%s',(
                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                self.var_std_id.get()==id+1
                                                                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                # >>>>>>>>>>>>>>>> Load predifiend data on face frontals from opencv >>>>>
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # sacling factor = 1.3
                    # Minimum neighbor = 5 
                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = 'data/user.'+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('Result','Generating data sets complated successfully !')
            except Exception as es:
                messagebox.showerror('error',f"{str(es)}",parent=self.root)





        
if __name__ == '__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()