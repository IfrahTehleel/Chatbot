import aiml
from Semantic_Networks import Semantics
from tkinter import *

main = Tk()
kernel = aiml.Kernel()
kernel.learn("clothee.aiml")


# i am using tkinter for the gui purpose

def ask_from_bot():
    # while True:
    query = textF.get()
    if query == "quit":
        exit()
    else:
        answer_from_bot = kernel.respond(query)
        Semantics(query)
        msgs.insert(END, "you : " + query)
        msgs.insert(END, "Bot : " + str(answer_from_bot))
        textF.delete(0, END)


main.geometry("900x800")  # width*height
main.title("The Clothee")
img = PhotoImage(file="logo.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)  # padding on y axis
frame = Frame(main)
sc = Scrollbar(frame)  # parent is frame
msgs = Listbox(frame, width=80, height=20)  # parent is frame
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=RIGHT, fill=BOTH, pady=5)
frame.pack()
# creating text field
textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)
btn = Button(main, text="Ask Clothee!", font=("Verdana", 20), command=ask_from_bot)
btn.pack()
main.mainloop()  # to display window
