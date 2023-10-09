from tkinter import *
import time
root=Tk()
root.title("Chatbot")
label_title=Label(root, text="Start talking to your Chatbot by saying something: ", font=('Ariel', 15))
label_title.grid(row=0,column=0)

x=1
y=10
check=True
question=""
answer=""
title_dest=False

def send():

    global x, check, question, answer, title_dest,label_title
    if title_dest==False:
        label_title.destroy()
        title_dest=True
    if check==False:
        label_user = Label(root, text="User: " + str(e.get()),font=('Times', 12))
        label_user.grid(sticky="W", row=x, column=0)
        answer=str(e.get())
        qna[question]=answer
        x += 1
        label_chatbot=Label(root, text="Chatbot: Thank you, I've learned something new!",font=('Times', 12))
        label_chatbot.grid(sticky="W", row=x, column=0)
        x+=1
        check = True
    else:
        label_user = Label(root, text="User: " + str(e.get()),font=('Times', 12))
        label_user.grid(sticky="W", row=x, column=0)
        x += 1

        if str(e.get()) in qna:
            label_chatbot = Label(root, text="Chatbot: " + str(qna[e.get()]),font=('Times', 12))
        else:
            question = str(e.get())
            label_chatbot = Label(root,
                                  text="Chatbot: I'm sorry, I don't have an answer to that. Could you type the answer in the box so I can learn?",font=('Times', 12))
            check = False
            e.delete(0, END)




        label_chatbot.grid(sticky="W", row=x, column=0)
        x += 1

    e.delete(0,END)


e=Entry(root, width=50)

e.grid(row=1000, column=0)
button_send=Button(root, text="Send", padx=20, pady=20, command=send)
button_send.grid(row=1000, column=4)

qna={"hey":"Hello there!",
     "how are you?": "I'm fine, what about you?",
     "what do you like to eat?": "I'm a chatbot, I do not eat. What do you like to eat?",
     "what is the capital of pakistan?": "the capital of pakistan is islamabad",
     "what year is it?": "it is 2023",
     "what time is it right now?": time.ctime(),
     "thank you": "you're most welcome!"
     }








root.mainloop()