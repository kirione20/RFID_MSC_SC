from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image

root=Tk()
 
       
class MainWindow:
    #para widget ng mainform
    def __init__(self,root,*args,**kwargs):
       
        self.root=root
        self.root.title("RFID SYSTEM")
        self.root.geometry("1200x700+200+70")
        self.root.configure(bg="#01a01b")
        self.root.resizable(False,False)

        #para sa background image
        #self.image=ImageTk.PhotoImage(file="images/background_win.jpg")
        #self.label=Label(self.root,image=self.image)
        #self.label.place(x=0,y=0)
       
       

        
        #Function for Main button. para mapunta sa front ung Frame

        ###Para sa Home Frame##### 
        def clicked_home():
            self.frame_home.lift()
            
            
        ###Para sa Employee Frame#####       
        def clicked_emp():
            self.frame_emp.lift()
             #Mga label sa pag insert ng Data
            self.head_label=Label(self.frame_emp,text="Register Employee Information",
            font=("Andalus",24,'bold'),fg="white",bg="#339900",borderwidth=10)
            self.head_label.place(x=0,y=20,width=880)
            
            self.name_label=Label(self.frame_emp,text="First Name",font=("Andalus",12,'bold'),fg="black",bg="white")
            self.name_label.place(x=20,y=100)
            
            self.mname_label=Label(self.frame_emp,text="Middle Name",font=("Andalus",12,'bold'),fg="black",bg="white")
            self.mname_label.place(x=20,y=185)
           
            self.lname_label=Label(self.frame_emp,text="Last Name",font=("Andalus",12,'bold'),fg="black",bg="white")     
            self.lname_label.place(x=20,y=270)

            self.gender_label=Label(self.frame_emp,text="Sex",font=("Andalus",12,'bold'),fg="black",bg="white")
            self.gender_label.place(x=20,y=350)

            self.bdate_label=Label(self.frame_emp,text="Birth Date",font=("Andalus",12,'bold'),fg="black",bg="white")     
            self.bdate_label.place(x=20,y=430)

            self.address_label=Label(self.frame_emp,text="Address",font=("Andalus",12,'bold'),fg="black",bg="white")     
            self.address_label.place(x=20,y=510)

            #label sa right side ng employee frame
            self.department_label=Label(self.frame_emp,text="Department",font=("Andalus",12,'bold'),fg="black",bg="white")     
            self.department_label.place(x=350,y=95)

            self.position_label=Label(self.frame_emp,text="Position",font=("Andalus",12,'bold'),fg="black",bg="white")
            self.position_label.place(x=350,y=181)

            self.Salary_label=Label(self.frame_emp,text="Salary Grade",font=("Andalus",12,'bold'),fg="black",bg="white")
            self.Salary_label.place(x=350,y=265)

            self.email_label=Label(self.frame_emp,text="Email Address",font=("Andalus",12,'bold'),fg="black",bg="white")
            self.email_label.place(x=350,y=350)

            self.contact_label=Label(self.frame_emp,text="Contact Details",font=("Andalus",12,'bold'),fg="black",bg="white")
            self.contact_label.place(x=350,y=435)

            self.rfid_label=Label(self.frame_emp,text="RFID Number",font=("Andalus",12,'bold'),fg="black",bg="white")
            self.rfid_label.place(x=350,y=510)
            
            ###Picture Box###
            self.picbox_label=Label(self.frame_emp,text="",bg="darkgreen")
            self.picbox_label.place(x=680,y=125, width=130,height=130)
           

             #Mga Entry box para sa pag insert
            self.name_entry=Entry(self.frame_emp,font=("calibri",14),borderwidth=5)
            self.name_entry.place(x=20,y=135,width=250)

            self.mname_entry=Entry(self.frame_emp,font=("calibri",14),borderwidth=5)
            self.mname_entry.place(x=20,y=220,width=250)

            self.lname_entry=Entry(self.frame_emp,font=("calibri",14),borderwidth=5)
            self.lname_entry.place(x=20,y=305,width=250)

            self.birthdate_entry=Entry(self.frame_emp,font=("calibri",14),borderwidth=5)
            self.birthdate_entry.place(x=20,y=465,width=250)

            self.address_entry=Entry(self.frame_emp,font=("calibri",14),borderwidth=5)
            self.address_entry.place(x=20,y=550,width=250)

            #entry box for employee registration right side
            self.email_entry=Entry(self.frame_emp,font=("calibri",14),borderwidth=5)
            self.email_entry.place(x=350,y=382,width=250)

            self.contact_entry=Entry(self.frame_emp,font=("calibri",14),borderwidth=5)
            self.contact_entry.place(x=350,y=463,width=250)

            self.rfid_entry=Entry(self.frame_emp,font=("calibri",14),borderwidth=5)
            self.rfid_entry.place(x=350,y=548,width=250)


            #combo box for department options
            options_dep = [
                "",
                "SICS",
                "SED",
                "SENG"
            ]
            self.dep_cbox= ttk.Combobox(self.frame_emp,value=options_dep)
            self.dep_cbox.current(0)
            self.dep_cbox.place(x=350,y=131,width=250,height=31)
            
            #combo box for positions options
            options_position = [
                "",
                "Support Staff",
                "College Lecturer",
                "Instructor I"
            ]
            self.position_cbox= ttk.Combobox(self.frame_emp,value=options_position)
            self.position_cbox.current(0)
            self.position_cbox.place(x=350,y=216,width=250,height=31)

             #combo box for salary Grade
            options_salaryg = [
                "","1","2","3","4","5","6","7","8","9",
                "10","11","12","13","14","15","16","17","18"
            ]
            self.salaryg_cbox= ttk.Combobox(self.frame_emp,value=options_salaryg)
            self.salaryg_cbox.current(0)
            self.salaryg_cbox.place(x=350,y=302,width=250,height=31)

            #combo box for department options
            options_gender = [
                "","MALE",
                "FEMALE"
            ]
            self.gender_cbox= ttk.Combobox(self.frame_emp,value=options_gender)
            self.gender_cbox.current(0)
            self.gender_cbox.place(x=20,y=385,width=250,height=31)

            
            
            

            #Register button for the employee registration
            self.btn_save = Button(self.frame_emp, text="Register",borderwidth=3,relief=GROOVE,activebackground="#0B0F08",
            activeforeground="white",fg="white",bg="green",font=("arial",15,'bold'))
            self.btn_save.place(x=45,y=610,width=200,height=50)

            #Update button for the employee registration
            self.btn_update = Button(self.frame_emp, text="Update",borderwidth=3,relief=GROOVE,activebackground="#0B0F08",
            activeforeground="white",fg="white",bg="green",font=("arial",15,'bold'))
            self.btn_update.place(x=380,y=610,width=200,height=50)

            #Update button for the employee registration
            self.btn_delete = Button(self.frame_emp, text="Delete",borderwidth=3,relief=GROOVE,activebackground="#0B0F08",
            activeforeground="white",fg="white",bg="red",font=("arial",15,'bold'))
            self.btn_delete.place(x=650,y=610,width=200,height=50)

            #picture box button for the employee registration
            self.btn_picture = Button(self.frame_emp, text="Upload",borderwidth=3,relief=GROOVE,activebackground="#0B0F08",
            activeforeground="white",fg="white",bg="green",font=("arial",12,'bold'))
            self.btn_picture.place(x=695,y=270,width=100,height=30)

        ###Para sa Department Frame##### 
        def clicked_dep():
            self.frame_dep.lift()
        
        ###Para sa Position Frame##### 
        def clicked_pos():
            self.frame_pos.lift()
        
        ###Para sa settings Frame##### 
        def clicked_setting():
            self.frame_setting.lift()

        ###Para sa settings Frame##### 
        def clicked_event():
            self.frame_event.lift()
        


   
        
        #Container for Main button example: Home,Employee etc.
        self.canvas = Canvas(self.root)
        self.canvas.place(x=10,y=10,width=300,height=680)
        #ito ung sa image na png
        
        self.image1=ImageTk.PhotoImage(file="images/msclogo1.png")
        self.label1=Label(self.canvas,image=self.image1,borderwidth=10)
        self.label1.place(x=75,y=5)

      

        #Home button
        self.Home = Button(self.canvas, text="HOME",borderwidth=5,relief=GROOVE, activebackground="#0B0F08",
        activeforeground="white",fg="white",bg="green",font=("arial",15,'bold'),command=clicked_home)
        self.Home.place(x=10,y=150,width=280,height=60)
        
    
       
        #employee button
        self.employee = Button(self.canvas, text="EMPLOYEE",borderwidth=5,relief=GROOVE,activebackground="#0B0F08",
         activeforeground="white",fg="white",bg="green",font=("arial",15,'bold'),command=clicked_emp)
        self.employee.place(x=10,y=210,width=280,height=60)
         

        #department button
        self.department = Button(self.canvas, text="DEPARTMENT",borderwidth=5,relief=GROOVE,
         activebackground="#0B0F08",activeforeground="white",fg="white",bg="green",font=("arial",15,'bold')
        ,command=clicked_dep)
        self.department.place(x=10,y=270,width=280,height=60)

        #position button
        self.post = Button(self.canvas, text="POSITION",borderwidth=5,relief=GROOVE, 
        activebackground="#0B0F08",activeforeground="white",fg="white",bg="green",font=("arial",15,'bold')
        ,command=clicked_pos)
        self.post.place(x=10,y=330,width=280,height=60)

          #setting button
        self.settings = Button(self.canvas, text="SETTINGS",borderwidth=5,relief=GROOVE,
         activebackground="#0B0F08",activeforeground="white",fg="white",bg="green",font=("arial",15,'bold'),command=clicked_setting)
        self.settings.place(x=10,y=390,width=280,height=60)

        #event button    
        self.event = Button(self.canvas, text="EVENT",borderwidth=5,relief=GROOVE,
         activebackground="#0B0F08",activeforeground="white",fg="white",bg="green",font=("arial",15,'bold'),command=clicked_event)
        self.event.place(x=10,y=450,width=280,height=60)


       
        #####Frame para sa Main Button#####
        #frame for event info
        self.frame_event = Frame(self.root)
        self.frame_event.place(x=320,y=10,width=870,height=680)
         ###Background image sa event frame###
        self.image_eventback=ImageTk.PhotoImage(file="images/backwin2.jpg")
        self.label_eventback=Label(self.frame_event,image=self.image_eventback)
        self.label_eventback.place(x=0,y=0,width=870,height=680)

        #frame for setting info
        self.frame_setting = Frame(self.root)
        self.frame_setting.place(x=320,y=10,width=870,height=680)
         ###Background image sa setting frame###
        self.image_settingback=ImageTk.PhotoImage(file="images/backwin2.jpg")
        self.label_settingback=Label(self.frame_setting,image=self.image_settingback)
        self.label_settingback.place(x=0,y=0,width=870,height=680)


        #frame for position info
        self.frame_pos = Frame(self.root)
        self.frame_pos.place(x=320,y=10,width=870,height=680)
         ###Background image sa position frame###
        self.image_posback=ImageTk.PhotoImage(file="images/backwin2.jpg")
        self.label_posback=Label(self.frame_pos,image=self.image_posback)
        self.label_posback.place(x=0,y=0,width=870,height=680)


        #frame for department info
        self.frame_dep = Frame(self.root)
        self.frame_dep.place(x=320,y=10,width=870,height=680)
        ###Background image sa department frame###
        self.image_depback=ImageTk.PhotoImage(file="images/backwin2.jpg")
        self.label_depback=Label(self.frame_dep,image=self.image_depback)
        self.label_depback.place(x=0,y=0,width=870,height=680)



        #frame for employee info
        self.frame_emp = Frame(self.root)
        self.frame_emp.place(x=320,y=10,width=870,height=680) 
        ###Background image sa employee frame###
        self.image_empback=ImageTk.PhotoImage(file="images/backwin2.jpg")
        self.label_empback=Label(self.frame_emp,image=self.image_empback)
        self.label_empback.place(x=0,y=0,width=870,height=680)

        

        #frame for home info
        self.frame_home = Frame(self.root)
        self.frame_home.place(x=320,y=10,width=870,height=680)
        #Background image sa home frame
        self.image_homeback=ImageTk.PhotoImage(file="images/backwin2.jpg")
        self.label_homeback=Label(self.frame_home,image=self.image_homeback)
        self.label_homeback.place(x=0,y=0,width=870,height=680)


 

       
        

       


main=MainWindow(root)
root.mainloop()
