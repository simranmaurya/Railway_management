import psycopg2 as pg
import random
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import ImageTk as itk , Image



#connection is established
con = pg.connect(host='localhost',
                 database='Railway',
                 user='postgres',
                 password='776779',
                 port=5432)

#curser is created
cur = con.cursor()


def payment_gateway(PNR):
    ViewRecords = tk.Toplevel(window)
    ViewRecords.title("New Reservation")
    ViewRecords.configure(background='light blue')
    ViewRecords.geometry('400x400')
    style = Style(ViewRecords)

    passLabel1 = Label(ViewRecords,text = "Enter Payment Method")
    passLabel1.pack(padx=50,pady=2)
    passtxt1 = Entry(ViewRecords,width = 10)
    passtxt1.pack(padx=50,pady=2)

    def passclick():
        PayMethod = passtxt1.get()
        ViewRecords2 = tk.Toplevel(ViewRecords)
        ViewRecords2.title("New Reservation")
        ViewRecords2.configure(background='light blue')
        ViewRecords2.geometry('400x400')
        style = Style(ViewRecords2)
        amount = random.choice(['1020', '2011', '1560', '1542'])    
        captcha_text = (random.choice(['127413', 'ABTYSA', '7861AB', 'yuja67']))

        passLabel3 = Label(ViewRecords2,text = "Amount to be paid is")
        passLabel3.pack(padx=50,pady=2)
        passLabel4 = Label(ViewRecords2,text = amount)
        passLabel4.pack(padx=50,pady=2)

        passLabel3 = Label(ViewRecords2,text = "Enter the captcha below")
        passLabel3.pack(padx=50,pady=2)
        passLabel2 = Label(ViewRecords2,text = captcha_text)
        passLabel2.pack(padx=50,pady=2)
        passtxt2 = Entry(ViewRecords2,width = 10)
        passtxt2.pack(padx=50,pady=2)

        def passclick2():
            Captcha = passtxt2.get()
            if(Captcha == captcha_text):
                txn_id = str(round(random.random()*1000000))
                query = "insert into payment_gateway values("+txn_id + \
                ","+"'"+PayMethod+"'"+","+amount+","+PNR+")"
                cur.execute(query)
                con.commit()
                messagebox.showinfo("Pnr", PNR)
                ViewRecords.destroy()
                ViewRecords2.destroy()
            else:
                messagebox.showerror("Quit", "Payment Failed")
                ViewRecords.destroy()
                ViewRecords2.destroy()
      
        bt4 = tk.Button(ViewRecords2,text = 'Enter', fg = 'white', bg = 'black',command = passclick2)
        bt4.pack(padx=50,pady=2)
    bt3 = tk.Button(ViewRecords,text = 'Enter', fg = 'white', bg = 'black',command = passclick)
    bt3.pack(padx=50,pady=2)




def user():
    UserWindow = tk.Toplevel(window)
    UserWindow.title("UserWindow")
    UserWindow.configure(background='light blue')
    UserWindow.geometry('400x400')
    v = StringVar(UserWindow,"1")
    style = Style(UserWindow)
    style.configure("TRadiobutton", background = "light blue")

    def selectOption():
        option = var1.get()
        if(option == 1):
            PassDeet = tk.Toplevel(UserWindow)
            PassDeet.title("Related to Reservation")
            PassDeet.configure(background='light blue')
            PassDeet.geometry('400x400')
            v = StringVar(UserWindow)
            style = Style(UserWindow)
            style.configure("TRadiobutton", background = "light blue")
            
            def selectpassdeets():
                passoption = var2.get()
                if(passoption == 1):
                    ViewRecords = tk.Toplevel(PassDeet)
                    ViewRecords.title("View Reservation")
                    ViewRecords.configure(background='light blue')
                    ViewRecords.geometry('400x400')
                    style = Style(ViewRecords)
                    
                    passLabel1 = Label(ViewRecords,text = "Enter PNR")
                    passLabel1.pack(padx=50,pady=2)
                    passtxt1 = Entry(ViewRecords,width = 10)
                    passtxt1.pack(padx=50,pady=2)

                    def passclick():
                        ViewRecords2 = tk.Toplevel(ViewRecords)
                        ViewRecords2.title("View Reservation")
                        ViewRecords2.configure(background='light blue')
                        ViewRecords2.geometry('400x400')
                        style = Style(ViewRecords2)
                        Pnr = passtxt1.get()
                        query = "Select * from passengers where PNR = "+Pnr
                        cur.execute(query)
                        out = cur.fetchall()
                        passLabel100 = Label(ViewRecords2,text = "PNR  ")
                        passLabel100.grid(column =0,row =0)
                        passLabel101 = Label(ViewRecords2,text = "Passenger Name")
                        passLabel101.grid(column =1,row =0)
                        passLabel102 = Label(ViewRecords2,text = " DOJ ")
                        passLabel102.grid(column =2,row =0)
                        passLabel103 = Label(ViewRecords2,text = " Train Number")
                        passLabel103.grid(column =3,row =0)
                        passLabel104 = Label(ViewRecords2,text = " Reservation Status")
                        passLabel104.grid(column =4,row =0)
                        for index,x in enumerate(out): 
                            for index2,y in enumerate(x):
                                lookup = Label(ViewRecords2, text = y,background="light blue")
                                lookup.grid(row = index+1, column =index2)
                    
                    bt3 = tk.Button(ViewRecords,text = 'Enter', fg = 'white', bg = 'black',command = passclick)
                    bt3.pack(padx=50,pady=2)

                if(passoption == 2):
                    ViewRecords = tk.Toplevel(PassDeet)
                    ViewRecords.title("New Reservation")
                    ViewRecords.configure(background='light blue')
                    ViewRecords.geometry('400x400')
                    style = Style(ViewRecords)
                    

                    passLabel2 = Label(ViewRecords,text = "Enter Name")
                    passLabel2.pack(padx=50,pady=2)
                    passtxt2 = Entry(ViewRecords,width = 10)
                    passtxt2.pack(padx=50,pady=2)

                    passLabel3 = Label(ViewRecords,text = "Enter Train")
                    passLabel3.pack(padx=50,pady=2)
                    passtxt3 = Entry(ViewRecords,width = 10)
                    passtxt3.pack(padx=50,pady=2)

                    passLabel4 = Label(ViewRecords,text = "Enter DOJ (DD-MMM-YYYY)")
                    passLabel4.pack(padx=50,pady=2)
                    passtxt4 = Entry(ViewRecords,width = 10)
                    passtxt4.pack(padx=50,pady=2)

                    def passclick():
                        Train =passtxt3.get()
                        Name = passtxt2.get()
                        DOJ = passtxt4.get()
                        Pnr = str(round(random.random()*10000))
                        Status = random.choice(['Confirmed', 'RAC', 'Waiting'])

                        query = "insert into passengers values("+Pnr+','+"'"+Name + \
        "'"+','+"'"+DOJ+"'"+','+Train+','+"'"+Status+"'"+")"        
                        payment_gateway(Pnr)
                        cur.execute(query)
                        con.commit()
                        ViewRecords.destroy()

                    bt3 = tk.Button(ViewRecords,text = 'Enter', fg = 'white', bg = 'black',command = passclick)
                    bt3.pack(padx=50,pady=2)
              
                if(passoption == 3):
                    ViewRecords = tk.Toplevel(PassDeet)
                    ViewRecords.title("Cancel Reservation")
                    ViewRecords.configure(background='light blue')
                    ViewRecords.geometry('400x400')
                    style = Style(ViewRecords)
                    
                    passLabel1 = Label(ViewRecords,text = "Enter PNR")
                    passLabel1.pack(padx=50,pady=2)
                    passtxt1 = Entry(ViewRecords,width = 10)
                    passtxt1.pack(padx=50,pady=2)

                    def passclick():
                        Pnr = passtxt1.get()
                        query = "Update passengers set reservation_status = 'Cancelled' where PNR ="+Pnr
                        cur.execute(query)
                        con.commit()
                        messagebox.showerror("Cancel", "Reservation Cancelled")
                        ViewRecords.destroy()
                    
                    bt3 = tk.Button(ViewRecords,text = 'Enter', fg = 'white', bg = 'black',command = passclick)
                    bt3.pack(padx=50,pady=2)
                    
                            

            var2 = IntVar()
            Radiobutton(PassDeet, text="View Reservation", variable=var2, value=1, command=selectpassdeets).pack(padx=50,pady=2)
            Radiobutton(PassDeet, text="New Reservation", variable=var2, value=2, command=selectpassdeets).pack(padx=50,pady=2)
            Radiobutton(PassDeet, text="Cancel Reservation", variable=var2, value=3, command=selectpassdeets).pack(padx=50,pady=2)

        elif(option == 2):
            TrainDeet = tk.Toplevel(UserWindow)
            TrainDeet.title("Train Availability")
            TrainDeet.configure(background='light blue')
            TrainDeet.geometry('400x400')

            cur.execute("select * from train")
            out = cur.fetchall()
            passLabel100 = Label(TrainDeet,text = "Train Number")
            passLabel100.grid(column =0,row =0)
            passLabel101 = Label(TrainDeet,text = "Train Name")
            passLabel101.grid(column =1,row =0)
            passLabel102 = Label(TrainDeet,text = "Source")
            passLabel102.grid(column =2,row =0)
            passLabel103 = Label(TrainDeet,text = " Destination")
            passLabel103.grid(column =3,row =0)
            passLabel104 = Label(TrainDeet,text = " Seats")
            passLabel104.grid(column =4,row =0)
            for index,x in enumerate(out): 
                num = 0
                for y in x:
                    lookup = Label(TrainDeet, text = y,background="light blue")
                    lookup.grid(row = index+1, column =num)
                    num += 1
                
        elif(option == 3):
            messagebox.showinfo("Quit", "Thank You. Have a nice Day!!")
            UserWindow.destroy()

    var1 = IntVar()
    Radiobutton(UserWindow, text="Related to Reservation", variable=var1, value=1, command=selectOption).pack(padx=50,pady=2)
    Radiobutton(UserWindow, text="Train Availability", variable=var1, value=2, command=selectOption).pack(padx=50,pady=2)
    Radiobutton(UserWindow, text="EXIT", variable=var1, value=3, command=selectOption).pack(padx=50,pady=2)



def admin():
    AdminWindow = tk.Toplevel(window)
    AdminWindow.title("AdminWindow")
    AdminWindow.configure(background='light blue')
    AdminWindow.geometry('400x400')
    v = StringVar(AdminWindow,"1")
    style = Style(AdminWindow)
    style.configure("TRadiobutton", background = "light blue")
    
    def selectOption():
        option = var1.get()
        print("Value is ", option)
        if(option == 1):
            PassDeet = tk.Toplevel(AdminWindow)
            PassDeet.title("Passenger Details")
            PassDeet.configure(background='light blue')
            PassDeet.geometry('400x400')
            v = StringVar(AdminWindow)
            style = Style(AdminWindow)
            style.configure("TRadiobutton", background = "light blue")
            
            def selectpassdeets():
                passoption = var2.get()
                cur.execute("select * from passengers")
                out = cur.fetchall()
                if not out:
                    messagebox.showerror("Error", "NO RECORD FOUND")
                if(passoption == 1):
                    ViewRecords = tk.Toplevel(PassDeet)
                    ViewRecords.title("Passenger Details")
                    ViewRecords.configure(background='light blue')
                    ViewRecords.geometry('400x400')
                    style = Style(ViewRecords)
                    passLabel100 = Label(ViewRecords,text = "PNR  ")
                    passLabel100.grid(column =0,row =0)
                    passLabel101 = Label(ViewRecords,text = "Passenger Name")
                    passLabel101.grid(column =1,row =0)
                    passLabel102 = Label(ViewRecords,text = " DOJ ")
                    passLabel102.grid(column =2,row =0)
                    passLabel103 = Label(ViewRecords,text = " Train Number")
                    passLabel103.grid(column =3,row =0)
                    passLabel104 = Label(ViewRecords,text = " Reservation Status")
                    passLabel104.grid(column =4,row =0)
                    for index,x in enumerate(out): 
                        num = 0
                        for y in x:
                            lookup = Label(ViewRecords, text = y, background="light blue")
                            lookup.grid(row = index+1, column =num)
                            num += 1
                        
                if(passoption == 2):
                    ViewRecords = tk.Toplevel(PassDeet)
                    ViewRecords.title("Update Details")
                    ViewRecords.configure(background='light blue')
                    ViewRecords.geometry('400x400')
                    style = Style(ViewRecords)
                    passLabel100 = Label(ViewRecords,text = "PNR  ")
                    passLabel100.grid(column =0,row =0)
                    passLabel101 = Label(ViewRecords,text = "Passenger Name")
                    passLabel101.grid(column =1,row =0)
                    passLabel102 = Label(ViewRecords,text = " DOJ ")
                    passLabel102.grid(column =2,row =0)
                    passLabel103 = Label(ViewRecords,text = " Train Number")
                    passLabel103.grid(column =3,row =0)
                    passLabel104 = Label(ViewRecords,text = " Reservation Status")
                    passLabel104.grid(column =4,row =0)
                    for index,x in enumerate(out): 
                        num = 0
                        for y in x:
                            lookup = Label(ViewRecords, text = y,background="light blue")
                            lookup.grid(row = index+1, column =num)
                            num += 1 

                    passLabel1 = Label(ViewRecords,text = "Enter PNR")
                    passLabel1.grid(column =0,row =20)
                    passtxt1 = Entry(ViewRecords,width = 10)
                    passtxt1.grid(column =1, row =20)
                        
                    passLabel2 = Label(ViewRecords,text = "Enter Name")
                    passLabel2.grid(column =0,row =21)
                    passtxt2 = Entry(ViewRecords,width = 10)
                    passtxt2.grid(column =1, row =21)

                    passLabel3 = Label(ViewRecords,text = "Enter Train")
                    passLabel3.grid(column =0,row =22)
                    passtxt3 = Entry(ViewRecords,width = 10)
                    passtxt3.grid(column =1, row =22)

                    passLabel4 = Label(ViewRecords,text = "Enter DOJ (DD-MMM-YYYY)")
                    passLabel4.grid(column =0,row =23)
                    passtxt4 = Entry(ViewRecords,width = 10)
                    passtxt4.grid(column =1, row =23)

                    def passclick():
                        Pnr = passtxt1.get()
                        Name = passtxt2.get()
                        Train = passtxt3.get()
                        DOJ = passtxt4.get()
                        Status = random.choice(['Confirmed', 'RAC', 'Waiting'])
                        query = "update passengers set P_name="+"'"+Name+"'"+",DOJ="+"'"+DOJ+"'" + \
                    ",Train_number="+Train+",reservation_status="+"'"+Status+"'"+"where pnr="+Pnr
                        cur.execute(query)
                        con.commit()
                        messagebox.showinfo("Update", "Record Updated!!")
                        ViewRecords.destroy()


                    bt3 = tk.Button(ViewRecords,text = 'Enter', fg = 'white', bg = 'black',command = passclick)
                    bt3.grid(column =0, row =25)          
                            
                if(passoption == 3):
                    ViewRecords = tk.Toplevel(PassDeet)
                    ViewRecords.title("Delete Details")
                    ViewRecords.configure(background='light blue')
                    ViewRecords.geometry('400x400')
                    style = Style(ViewRecords)
                    passLabel100 = Label(ViewRecords,text = "PNR  ")
                    passLabel100.grid(column =0,row =0)
                    passLabel101 = Label(ViewRecords,text = "Passenger Name")
                    passLabel101.grid(column =1,row =0)
                    passLabel102 = Label(ViewRecords,text = " DOJ ")
                    passLabel102.grid(column =2,row =0)
                    passLabel103 = Label(ViewRecords,text = " Train Number")
                    passLabel103.grid(column =3,row =0)
                    passLabel104 = Label(ViewRecords,text = " Reservation Status")
                    passLabel104.grid(column =4,row =0)
                    for index,x in enumerate(out): 
                        num = 0
                        for y in x:
                            lookup = Label(ViewRecords, text = y,background="light blue")
                            lookup.grid(row = index+1, column =num)
                            num += 1      
                    
                    passLabel1 = Label(ViewRecords,text = "Enter PNR")
                    passLabel1.grid(column =0,row =20)
                    passtxt1 = Entry(ViewRecords,width = 10)
                    passtxt1.grid(column =1, row =20)   

                    def passclick():
                        Pnr = passtxt1.get()
                        query = "Delete from passengers where pnr="+Pnr
                        cur.execute(query)
                        con.commit()
                        messagebox.showerror("Delete", "Record Deleted!!")
                        ViewRecords.destroy()
                    
                    bt3 = tk.Button(ViewRecords,text = 'Enter', fg = 'white', bg = 'black',command = passclick)
                    bt3.grid(column =0, row =25)        

            var2 = IntVar()
            Radiobutton(PassDeet, text="View Details", variable=var2, value=1, command=selectpassdeets).pack(padx=50,pady=2)
            Radiobutton(PassDeet, text="Update Details", variable=var2, value=2, command=selectpassdeets).pack(padx=50,pady=2)
            Radiobutton(PassDeet, text="Delete Details", variable=var2, value=3, command=selectpassdeets).pack(padx=50,pady=2)

        elif(option == 2):
            TrainDeet = tk.Toplevel(AdminWindow)
            TrainDeet.title("Train Details")
            TrainDeet.configure(background='light blue')
            TrainDeet.geometry('400x400')

            cur.execute("select * from train")
            out = cur.fetchall()
            passLabel100 = Label(TrainDeet,text = "Train Number")
            passLabel100.grid(column =0,row =0)
            passLabel101 = Label(TrainDeet,text = "Train Name")
            passLabel101.grid(column =1,row =0)
            passLabel102 = Label(TrainDeet,text = "Source")
            passLabel102.grid(column =2,row =0)
            passLabel103 = Label(TrainDeet,text = " Destination")
            passLabel103.grid(column =3,row =0)
            passLabel104 = Label(TrainDeet,text = " Seats")
            passLabel104.grid(column =4,row =0)
            for index,x in enumerate(out): 
                num = 0
                for y in x:
                    lookup = Label(TrainDeet, text = y, background="light blue")
                    lookup.grid(row = index+1, column =num)
                    num += 1
                
        elif(option == 3):
            PayDeet = tk.Toplevel(AdminWindow)
            PayDeet.title("Payment Details")
            PayDeet.configure(background='light blue')
            PayDeet.geometry('400x400')

            cur.execute("select * from payment_gateway")
            out = cur.fetchall()
            passLabel100 = Label(PayDeet,text = "Transaction ID")
            passLabel100.grid(column =0,row =0)
            passLabel101 = Label(PayDeet,text = "Payment Mode ")
            passLabel101.grid(column =1,row =0)
            passLabel102 = Label(PayDeet,text = "Amount ")
            passLabel102.grid(column =2,row =0)
            passLabel103 = Label(PayDeet,text = " PNR")
            passLabel103.grid(column =3,row =0)
            for index,x in enumerate(out): 
                num = 0
                for y in x:
                    lookup = Label(PayDeet, text = y,background="light blue")
                    lookup.grid(row = index+1, column =num)
                    num += 1

        elif(option == 4):
            StationDeet = tk.Toplevel(AdminWindow)
            StationDeet.title("Station Details")
            StationDeet.configure(background='light blue')
            StationDeet.geometry('400x400')

            cur.execute("select * from stations")
            out = cur.fetchall()
            passLabel100 = Label(StationDeet,text = "Serial Number")
            passLabel100.grid(column =0,row =0)
            passLabel101 = Label(StationDeet,text = "Station Name")
            passLabel101.grid(column =1,row =0)
            for index,x in enumerate(out): 
                num = 0
                for y in x:
                    lookup = Label(StationDeet, text = y,background="light blue")
                    lookup.grid(row = index+1, column =num)
                    num += 1

        elif(option == 5):
            messagebox.showinfo("Quit", "Thank You. Have a nice Day!!")
            AdminWindow.destroy()

    var1 = IntVar()
    Radiobutton(AdminWindow, text="Passenger Details", variable=var1, value=1, command=selectOption).pack(padx=50,pady=2)
    Radiobutton(AdminWindow, text="Train Details", variable=var1, value=2, command=selectOption).pack(padx=50,pady=2)
    Radiobutton(AdminWindow, text="Payment History", variable=var1, value=3, command=selectOption).pack(padx=50,pady=2)
    Radiobutton(AdminWindow, text="Station Details", variable=var1, value=4, command=selectOption).pack(padx=50,pady=2)
    Radiobutton(AdminWindow, text="Exit", variable=var1, value=5, command=selectOption).pack(padx=50,pady=0)



window = tk.Tk()
window.title("RAILWAY MANAGEMENT")
window.configure(bg='light blue')
window.geometry('400x400')

path = "C:/Users/Simran/Desktop/Raj_Rail/Railways-DBMS-project-master/download"
path1= 'Railways-DBMS-project-master\download(1).jpg'

'''
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image = img, background="light blue")
panel.pack(side = "bottom", fill = "both", expand = "yes")

'''
bg = itk.PhotoImage(file=path1)
canvas1 = Canvas(window, width = 400,height = 400)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 175, 150, image = bg, anchor = "center")
canvas1.create_text( 150, 50, text = "WELCOME TO RAILWAYS", fill = 'blue', font='Helvetica 15 bold')

def openAdmin(self):
    newWindow = tk.Toplevel(window)
    newWindow.title("Admin")
    newWindow.configure(bg='light blue')
    newWindow.geometry('400x400')

    passLabel = Label(newWindow,text = "Enter Password")
    passLabel.pack(padx=50, pady=20)

    passtxt = Entry(newWindow,width = 10 )
    passtxt.pack(padx=0, pady=0)
    def click():
        passentered = passtxt.get()
        if(passentered == "Raj123"):
            admin()
        else:
            messagebox.showerror("Error", "Wrong Password")

    bt3 = tk.Button(newWindow,text = 'Enter', fg = 'white', bg = 'black',command = click)
    bt3.pack(padx=0, pady=2)


bt1 = tk.Button(window,text = 'Admin', fg = 'white', bg = 'black', command= lambda: openAdmin("Admin"))
bt1.pack(padx = 50, pady = 50)
bt2 = tk.Button(window,text = 'User', fg = 'white' , bg = 'black', command = user)
bt2.pack(padx = 50, pady = 15)

bt1_can = canvas1.create_window( 100, 250,anchor = "nw",window = bt1)
bt2_can = canvas1.create_window( 150, 250,anchor = "nw",window = bt2)

window.mainloop()
cur.close()
con.close()
