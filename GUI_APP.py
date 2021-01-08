#THIS GUI APP IS CREATED BY ABHIMANYU SHARMA A.K.A N1nja0p
####IMPORT MODULES####
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win=tk.Tk()
#########NAME######
name_var=tk.StringVar()
name_label=ttk.Label(win,text="Enter Your Name : ")
name_entry_box=ttk.Entry(win,width=16,textvariable=name_var)
name_label.grid(row=0,column=0,sticky=tk.W)
name_entry_box.grid(row=0,column=1)
name_entry_box.focus()
########EMAIL########
email_var=tk.StringVar()
email_label=ttk.Label(win,text="Enter Your Email : ")
email_label.grid(row=1,column=0,sticky=tk.W)
email_entry_box=ttk.Entry(win,width=16,textvariable=email_var)
email_entry_box.grid(row=2,column=1)
##########AGE########
age_var=tk.StringVar()
age_label=ttk.Label(win,text="Enter Your Age : ")
age_label.grid(row=2,column=0,sticky=tk.W)
age_entry_box=ttk.Entry(win,width=16,textvariable=age_var)
age_entry_box.grid(row=1,column=1)
######COMBO BOX#######
gender_var=tk.StringVar()
gender_label=ttk.Label(win,text="Select Your Gender : ")
gender_label.grid(row=3,column=0,sticky=tk.W)
gender=ttk.Combobox(win,width=14,textvariable=gender_var,state='readonly')
gender['values']=('Male','Female','Non-Binary')
gender.grid(row=3,column=1)
gender.current(0)
#######RADIO BUTTON######
usertype=tk.StringVar()
radio=ttk.Radiobutton(win,text='Student',value='Student',variable=usertype)
radio.grid(row=4,column=0)
radio2=ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=usertype)
radio2.grid(row=4,column=1)
######CHECK BUTTON######
check_var=tk.IntVar()
check=ttk.Checkbutton(win,text='Subscribe To Our Newsletter',variable=check_var)
check.grid(row=5,columnspan=3,sticky=tk.W)
########ACTION######
def action():
    username=name_var.get()
    userage=email_var.get()
    useremail=age_var.get()
    user_gender=gender_var.get()
    user_type=usertype.get()
    if check_var.get()==0:
        subscribed='NO'
    else:
        subscribed="YES"
    #########WRITE TO CSV FILE##########
    with open('save.csv','a',newline="")as f:
        dict_writer=DictWriter(f,fieldnames=['Username','User Email Address','User Age','User Gender','User Type','Subscribed'])
        if os.stat('save.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'Username':username,
            'User Email Address':useremail,
            'User Age':userage,
            'User Gender':user_gender,
            'User Type':user_type,
            'Subscribed':subscribed,
        })
    name_entry_box.delete(0,tk.END)
    age_entry_box.delete(0,tk.END)
    email_entry_box.delete(0,tk.END)
##########SUBMIT BUTTON#######
submit_button=ttk.Button(win,text="Submit",command=action)
submit_button.grid(row=6,column=0)
win.title("Form")
win.mainloop()