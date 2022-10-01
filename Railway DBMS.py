import csv
import random
from tabulate import tabulate

def Login():
    F1=open("UI","r",newline="")
    w=csv.reader(F1)
    
    global x
    
    x=input("Username:")
    y=input("Password:")
    p=0
    
    for i in w:
        a=i[0]
        b=i[1]

        if x == a and y == b:
            p=0
            print("Login Successfull")
            print("\n")
            break
        else:
            p=1
            continue
        
    if p == 1:
        print("Invalid Username or Password.")
        Login()
    
    F1.close()

    
def Create():
   F=open("UI","a",newline="")
   
   a=input("Enter New User-Name:")
   b=input("Enter New Password:")

   L=[a,b]

   w=csv.writer(F)
   w.writerow(L)

   print("User Created!!")
   print("\n")

   F.close()
   MAIN1()


def MAIN1():
    print("[1]Login-")
    print("Username")
    print("Password")
    print("[2]Create a new account")
    print("\n")

    ch=int(input("Enter your option:"))

    if ch == 1:
        Login()
    else:
        Create()

MAIN1()


def PNR():
    p="123456789"
    global z
    z=""
    
    for i in range(0,4):
        q=random.choice(p)
        z+=q


def Booking():
    PNR()
    
    L=[ ["City","Fare"],
        ["[1]Chennai","270"],
        ["[2]Mumbai","300"],
        ["[3]Delhi","700"],
        ["[4]Kolkata","670"],
        ["[5]Hydrebad","300"],
        ["         ","  "],
        ["[6]Mysore","170"],
        ["[7]Tumkur","210"],
        ["[8]Coorg","100"] ]
    print(tabulate(L,headers="firstrow",tablefmt="fancy_grid")) 

    ch=int(input("Enter your choice:"))

    import mysql.connector as X
    con1=X.connect(host="localhost",user="root",password="System123",database="GUI")
    c1=con1.cursor()
    
    if ch == 1:
        c1.execute("insert into USERS values ('{}','Chennai',270,{})".format(x,z))
        con1.commit()
    elif ch == 2:
        c1.execute("insert into USERS values ('{}','Mumbai',300,{})".format(x,z))
        con1.commit()
    elif ch == 3:       
        c1.execute("insert into USERS values ('{}','Delhi',700,{})".format(x,z))
        con1.commit()
    elif ch == 4:
        c1.execute("insert into USERS values ('{}','Kolkata',670,{})".format(x,z))
        con1.commit()
    elif ch == 5:
        c1.execute("insert into USERS values ('{}','Hydrebad',300,{})".format(x,z))
        con1.commit()
    elif ch == 6:
        c1.execute("insert into USERS values ('{}','Mysore',170,{})".format(x,z))
        con1.commit()
    elif ch == 7:
        c1.execute("insert into USERS values ('{}','Tumkur',210,{})".format(x,z))
        con1.commit()
    elif ch == 8:        
        c1.execute("insert into USERS values ('{}','Coorg',100,{})".format(x,z))
        con1.commit()

    print("Your payment has been successful.")
    
    while True:
        ch1=input("Go back to menu Y/N?")

        if ch1 == "N":
            break
        else:
            MAIN2()


def VIEW():
    import mysql.connector as X
    con1=X.connect(host="localhost",user="root",password="System123",database="GUI")

    c1=con1.cursor()
    c1.execute("select * from USERS where Name = '{}' ".format(x))

    r=c1.fetchall()
    q=len(r)
    print(x,"'s Bookings-")

    for i in range(0,q):
        L=[ ["City","Fare","PNR Number"],
        [r[i][1],r[i][2],r[i][3] ] ]
        print(tabulate(L,headers="firstrow",tablefmt="fancy_grid"))
    
    while True:
        ch1=input("Go back to menu Y/N?")

        if ch1 == "N":
            break
        else:
            MAIN2()


def CANCEL():
    import mysql.connector as X
    con1=X.connect(host="localhost",user="root",password="System123",database="GUI")
    c1=con1.cursor()

    ans=input("Enter name of city you want to cancel:")

    c1.execute("delete from USERS where name = '{}' and City = '{}' ".format(x,ans))
    con1.commit()


def MAIN2():
    print("Welcome",x,"!!")
    print("[1]View Account")
    print("[2]Make a Booking")
    print("[3]Cancel a Booking")
    print("[4]Quit")

    ch=int(input("Enter your choice:"))

    if ch == 1:
        VIEW()
    elif ch == 2:
        Booking()
    elif ch == 3:
        CANCEL()
    else:
        pass

MAIN2()

#Explanation-
'''
Login():
    Username and password is inputed by the user
    the variable x is global'ed so as to make it usable in other udf's for
    fetching data,cancelling,etc of that particular user
    if and else conditions are used to verify if user is in the csv file or not.

Create():
    new user name and passwd is created
    and gets added to the main csv file

MAIN1():
    option 1:
        for login
        udf Login() get's called
    option 2:
        for creating a new user
        udf Create get's called

PNR():
    PNR number is generated in this udf
    and stored in variable z
    z is global'ed so as to use it in adding it in the user's data

Booking():
    The List L is printed to show the user various options[1,2,3,.....]

    in sql- table "USERS" is created
    as USERS("User Name","City Name","Fare","PNR Number")

    the particular details/values of the journey is inserted into that particular user

VIEW():
    r is the list of Bookings made by that particular user
    For Eg:-
    in my sql 
    (say for)User (ABC)
    r=[ journey 1--("USER-ABC","City","Fare","PNR no"), journey 2--("USER-ABC","City","Fare","PNR no")]

    since there exists only one table USERS
    the order of users is mixed up
    
    mysql> select * from USERS;
    +--------+----------+------+------+
    | Name   | City     | Fare | PNR  |
    +--------+----------+------+------+
    | PQR    | Chennai  |  270 | 7222 |
    | Apurva | Hydrebad |  300 | 4763 |
    | Apurva | Mumbai   |  300 | 1853 |
    | PQR    | Tumkur   |  210 | 7155 |
    +--------+----------+------+------+
    4 rows in set (0.00 sec)

    for loop is used from 0 to len(of list r)

    r[i][1]---->City
    r[i][2]---->Fare
    r[i][3]---->PNR Number

CANCEL():
    can be understood

MAIN2():
    option's 1,2,..,4
    are for viewing,booking and canelling
    the respective udf's are called

                                                                '''
