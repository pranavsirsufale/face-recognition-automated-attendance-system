## Project GUI(Graphical User Interface):
1. Login Window:
The main window serves as the primary interface for users to interact with the attendance system. Consists with Title of project and there is few buttons like Login, Register, exit etc.
![image](https://github.com/user-attachments/assets/4dbb616d-f146-4f7c-b5c9-c8e51e4ac0a6)

 
3. Register window:
If the user does not registered there are button to register the user if user press register button it will be redirected the register window.
 ![image](https://github.com/user-attachments/assets/db434f68-b542-438b-a304-605420723887)
![image](https://github.com/user-attachments/assets/ef6e29e8-4064-43eb-bfde-ee48c20f032d)

 
2. Forgot password window:
If the user forgot password there are button to reset the password using some questions. Firstly user need to press button forgot password. If user put correct answer it will change password and show user password change succesfffully
 
 ![image](https://github.com/user-attachments/assets/92df9c93-522a-4f53-8308-98b7d4a8f525)
![image](https://github.com/user-attachments/assets/b047cf29-afa4-46aa-b1b0-f601c6bf9bed)
![image](https://github.com/user-attachments/assets/5bbaeaff-ce95-491c-bee8-3d794dc366a8)
![image](https://github.com/user-attachments/assets/857d6308-a2d0-410d-a59d-c82891513bc0)

 
User put right username and password user will redirect main window otherwise user will get error message, “password or username didn’t match”.
2. Menu Bar:
The menu bar contains student detail, take attendance, attendance report, train data images developer and help window.
 ![image](https://github.com/user-attachments/assets/dfc57436-c107-483c-b9fa-5db8c039c9fe)


3. Top Banner/Header:
This section include the system title, “Pranav’s face recognition automated attendance system”.

 ![image](https://github.com/user-attachments/assets/e3323385-7804-46c9-8c8d-766a0598907f)


4. Take Attendance:
The Take Attendance panel contains button, “Face Recognition” for capturing live images to mark attend the student:
 ![image](https://github.com/user-attachments/assets/72ae6d4b-9a47-4ed4-9a9c-ba569c98a24d)

Start/Stop Button: Initiates and stops the attendance capturing process.
Exit Button: Press Enter Button.
![image](https://github.com/user-attachments/assets/94b00b54-deea-4c93-aa89-522eb2e106b4)

 
![image](https://github.com/user-attachments/assets/d6539ab7-d5ff-4dcb-982e-50094236daff)




5. Camera Feed Display:
A portion of the GUI is dedicated to displaying the live camera feed for face detection and recognition once they look on camera the system will automatically find their details in database and mark attend the student and the student will get notification on display.
![image](https://github.com/user-attachments/assets/2268b42c-e65a-47ea-8eae-f1c930a278d2)


6. Attendance Report:
This section lists the individuals whose attendance has been recognized and marked.
It will display their Attendance Id, Roll  , Name , Department , Time , date, and status ("Present").
In the attendance report window if user want to see attendance user can go attendance report window and do following processes .
 
 ![image](https://github.com/user-attachments/assets/2306e42b-b49d-4cfb-ad1f-23fa4d74edad)
![image](https://github.com/user-attachments/assets/663fa172-936d-4a96-80f0-295eb8f3665d)


7. Live Timer:
Display System time in the hh:mm:ss format .
 
![image](https://github.com/user-attachments/assets/dc675764-7de6-4ad8-8731-f07cc8d5aa90)

8. Csv file Integration:
The GUI interacts with a backend attendance csv for storing and retrieving attendance records.
It includes functions for accessing and managing the records.
 ![image](https://github.com/user-attachments/assets/c47fd703-9848-4f45-82b9-553adf9b7ac0)

The captured attendance will store automatically in “Test.csv” in this , and open this file user should press the ,”Import csv” Button it will open folder where Test.csv file already should be available and once user open this file the data load , student attendance report window like this 
 ![image](https://github.com/user-attachments/assets/7688c094-ac06-41fb-bd9d-d8fa9f17a1af)

If the user click table data the student details will automatically fetch given form where user can easily analyze details 
 ![image](https://github.com/user-attachments/assets/6eaad274-e037-4f3e-8095-348db6f158cf)


9. Facial Recognition Module:
- The GUI interacts with the facial recognition module opencv’s ,”haarcascade_frontalface_default.xml’ classifier this is algorithm provided by python’s library called “opencv-contrib-python”, which handles face detection and recognition.
- It receives data from the camera feed, processes it, and communicates the results (recognized faces) back to the GUI for display.

10. User Interaction:
- Users can interact with the GUI through mouse clicks, button presses, and input fields.

11. Security:
- Implement security measures to protect sensitive data, especially in a system handling facial data and attendance records.

This architecture provides a high-level overview of how the graphical user interface for Pranav's Face Recognition Automated Attendance System using Tkinter should be structured. You can further refine and detail the architecture based on the specific requirements and functionalities of your project.
