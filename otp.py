from tkinter import *
from twilio.rest import Client

import random

root=Tk()
otp=0
s=Entry(root)
button_submit=Button(root)
Label_approved=Label(root)
Label_denied=Label(root)
x=True
def restart():
    global button_submit,s,Label_approved,Label_denied
    button_submit.destroy()
    s.destroy()
    if x==True:
        Label_approved.destroy()
    else:
        Label_denied.destroy()
def check():
    global otp,s
    if otp== int(s.get()):
        Label_approved=Label(root, text="You have been verified")
        Label_approved.grid(row=6, column=1)
        x=True
    else:
        Label_denied=Label(root,text="Incorrect OTP")
        Label_denied.grid(row=6, column=1)
        x=False
    button_restart=Button(root, text="Restart", padx=30, pady=15, command=restart)
    button_restart.grid(row=7, column=1)

def submit():
    global s
    Label_otp=Label(root, text="Enter OTP here: ")
    Label_otp.grid(row=3, column=0, columnspan=3)
    s=Entry(root, width=30)
    s.grid(row=4, column=0, columnspan=3)
    button_submit= Button(root, text="Submit", padx=30, pady=15, command=check)
    button_submit.grid(row=5, column=1)

def send():
    global otp
    otp= random.randint(1000,9999)
    account_sid="ACb5364b3c61b45f779781f8405894089f"
    account_token='8040580347f8030ba417daf20b7caa30'
    client=Client(account_sid,account_token)
    msg=client.messages.create(body= "Your OTP for Affreej Login is: "+str(otp), from_="+12623023736", to=str(e.get()))
    submit()
root.title("OTP Verification")
label_number= Label(root, text="Enter your phone number (with country code): ")
label_number.grid(row=0, column=0, columnspan=3)

e=Entry(root, width=50, borderwidth=10)
e.grid(row=1, column=0, columnspan=3)
button_send=Button(root, text="Send OTP", padx=40, pady=30, borderwidth=10, command= send)
button_send.grid(row=2, column=1)


root.mainloop()