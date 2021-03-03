from classes.Connection import Connection
import time
######### 
def choose_window():
    windows = (1,2,3)
    print("\t############### \n\t1. EMPLOYEES\t\n2. DEPARTMENT\n\t3. POSITION\n\t###############\n")

    ###### PILI NG ANONG WINDOW AEDIT #############

    ###### Create variable to handle the window #######

    window = 0
    while window not in windows:
        try:
            window = int(input("Choose window: "))    
           
        except:
            print("Wrong value")
    return window
    
######### EMPLOYEE CLASS ########
class Employee:
    def __init__(self):
        print("Employee Called")

######### DEPARTMENT CLASS #######
class Department:
    def __init__(self):
         print("Department Called")

######### POSITION CLASS ########
class Position:
    def __init__(self):
         print("Position Called")

########## FUNCTION FOR CHOOSED WINDOW ############
def switch_to_other_window(choosed_window):
    if choosed_window == 1:
        employee = Employee()

    elif choosed_window == 2:
        department = Department()


    else:
        position = Position()


choosed_window = choose_window()

switch_to_other_window(choosed_window)


###TESTING####
connectDB = Connection()

time.sleep(2)
print(connectDB.connect())
