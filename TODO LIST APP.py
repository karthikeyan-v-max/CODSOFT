import tkinter 
from tkinter import *
from tkinter import ttk
class todo:
    def __init__(self,root):
        self.root = root
        self.root.title("To-Do-List")
        self.root.geometry("650x410+300+150")

        self.label = Label(self.root, text="TO-DO-LIST-APP", font= 'ariel, 25 bold',width = 10, bd = 5, bg = 'purple', fg='black')
        self.label.pack(side = 'top', fill = BOTH)

        self.label2 = Label(self.root, text="ADD TASK", font= 'ariel, 18 bold',width = 10, bd = 5, bg = 'light blue', fg='black')
        self.label2.place(x = 40, y = 54)

        self.label3 = Label(self.root, text="TASKS", font= 'ariel, 18 bold',width = 10, bd = 5, bg = 'light blue', fg='black')
        self.label3.place(x = 320, y = 54)

        self.main_text = Listbox(self.root, height = 9, bd=5, width = 23, font = "ariel, 20 italic bold")
        self.main_text.place(x=280, y=103)

        self.text = Text(self.root, bd = 5, height = 2,width = 30, font = "ariel, 10 bold")
        self.text.place(x=20, y=120)
    #add task

        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open("data.txt", "w") as f1:
                f1.write(content)
                f1.seek(0)
                f1.close()
            self.text.delete(1.0, END)

    #delete
        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open("data.txt", "r+") as f2:
                new_f = f2.readlines()
                f2.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f2.write(line)
                f2.truncate()
            self.main_text.delete(delete_)

        with open("data.txt", "r") as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()

        self.button1 = Button(self.root, text="ADD", font = "sarif, 20 bold italic",width = 10, bg="orange", fg = "black", command = add)
        self.button1.place(x = 30,y = 180) 

        self.button2 = Button(self.root, text="DELETE", font = "sarif, 20 bold italic",width = 10, bg="red", fg = "black", command = delete )
        self.button2.place(x = 30, y = 280)

def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__" :
    main()
 