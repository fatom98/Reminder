from tkinter import *
from tkinter import ttk

class Reminder(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.events = dict()
        with open("remind.txt", "r") as docr:
            for line in docr:
                task = str(line).split(",")[0]
                date = str(line).split(",")[1]
                date = str(date).split("\n")[0]
                self.events[task] = date
        self.initUI()

    def initUI(self):
        #Widgets
        self.main_label = Label(self, text = "Reminder",font = " TimesNewRoman 16", bg = "red", fg = "white")
        self.treeview = ttk.Treeview(height = 20)
        self.treeview["columns"] = ("Task", "Due Date")
        self.space = Label(height = 2, bg = "green")
        self.text = Text( width = 25, height = 2)
        self.append = Button(text = "Append", command = self.append)
        self.done = Button(text = "Done", width = 7, command = self.done)
        self.save = Button(text = "Save & Exit", command = self.save)

        #Treeview Headings
        self.treeview.heading("#0", text = "Number")
        self.treeview.heading("Task", text = "Task")
        self.treeview.heading("Due Date", text = "Due Date")

        #Treview Columns
        self.treeview.column("#0", width = 60, minwidth = 60, anchor = CENTER)
        self.treeview.column("Task", width = 250, minwidth = 250, anchor = CENTER)
        self.treeview.column("Due Date", width = 100, minwidth = 100, anchor = CENTER)

        #Packing
        self.pack(fill = X)
        self.main_label.pack(fill = X)
        self.treeview.pack(side = "top", anchor = "w")
        self.space.pack(anchor = "w", fill = X)
        self.text.pack(anchor = "w")
        self.append.pack(side = "left")
        self.done.pack(side = "right")
        self.save.pack(side = "bottom")

        #Call View Function
        self.view()

    def append(self):
        #Append Button Function
        self.entry = self.text.get("1.0", END)
        self.task = str(self.entry).split("\n")[0]
        self.date = str(self.entry).split("\n")[1]
        if len(self.date) == 0:
            self.date = "N/A"
        self.events[self.task] = self.date
        self.view()

    def done(self):
        #Done Button Function
        cursor = self.treeview.focus()
        event = self.treeview.item(cursor)["values"][0]
        self.events.pop(event)
        self.view()

    def view(self):
        #To Show the Dictionary
        self.treeview.delete(*self.treeview.get_children())
        for i, j in enumerate(self.events):
            self.treeview.insert("", "end", text = i + 1, values=(j, self.events[j]))
        self.text.delete("1.0", END)

    def save(self):
        #Save & Exit Button Function
        with open("remind.txt", "w") as docw:
            for i in self.events:
                docw.write(str(i) + "," + str(self.events[i]) + "\n")
        sys.exit()

if __name__ == '__main__':
    root = Tk()
    app = Reminder(root)
    root.geometry("413x600+945+97")
    root.title("Reminder")
    root.config(bg = "Green")
    root.mainloop()
