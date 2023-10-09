from tkinter import *
import requests

root=Tk()
root.title("URL Shortner")
Label1=Label(root,text="Enter the URL here: ")
Label1.grid(row=0,column=0)
e=Entry(root,width=40, borderwidth=5)
e.grid(row=1, column=0, columnspan=3)
Label2=Label(root, text="Enter the link name: ")
Label2.grid(row=2, column=0)
f=Entry(root,width=40,borderwidth=5)
f.grid(row=3, column=0, columnspan=3)

def short_link(link,name):
    apikey='ff6e2056b0c2cde3eefaf26974a8bf7d6c562'
    base_key='https://cutt.ly/api/api.php'
    payload={'key':apikey, 'short':link, 'name':name}
    request=requests.get(base_key,params=payload)
    data=request.json()


    Label_final=Label(root,text=data)
    Label_final.grid(row=5,column=0,columnspan=3)
button_enter=Button(root, text="Shorten link", padx=30, pady=15, command=lambda: short_link(e.get(),f.get()))
button_enter.grid(row=4, column=0)
root.mainloop()