import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from random import randint

SHARTLAR = """
Rules of Game
you have to input two number
and input time
"""

TITLE = "find_number"
USERTIME = 0
A = 0
B = 0


class Game:
    def __init__(self):
        self.A = A
        self.B = B
        self.countdownTime = USERTIME
        self.FOUND_STATUS = 1

        self.window = tk.Tk()
        self.window.title(TITLE)
        self.window.focus_set()
        self.window.geometry('600x400')
        self.window.configure(padx=20, pady=20)

        self.title = tk.Label(self.window, text=TITLE, font=('Arial', 18), pady=20)
        self.title.grid(row=0, column=0)

        self.mainEntry = tk.Entry(self.window, font=('Arial', 16), width=15)
        self.mainEntry.grid(row=1, column=0)

        self.confirmbtn = tk.Button(self.window, text='check', font=('Arial', 14), command=self.check)
        self.confirmbtn.grid(row=1, column=1)

        self.separator = ttk.Separator(self.window, orient='horizontal')
        self.separator.grid(row=2, column=0, columnspan=4, sticky='ew', padx=10, pady=20)

        self.countdownTitle = tk.Label(self.window, text='time', font=('Arial', 16), pady=20)
        self.countdownTitle.grid(row=3, column=0)

        self.countdownText = tk.Label(self.window, text=self.countdownTime, font=('Arial', 16), pady=10)
        self.countdownText.grid(row=4, column=0)

        self.window.columnconfigure(0, weight=2)
        self.window.columnconfigure(1, weight=3)
        self.window.columnconfigure(2, weight=4)
        self.window.columnconfigure(3, weight=2)

        self.assign_number()
        self.update_countdown()
        self.window.mainloop()

    def update_countdown(self):
        self.countdownText.config(text=str(self.countdownTime) + ' sekund')
        if self.countdownTime > 0:
            if self.FOUND_STATUS:
                self.countdownTime -= 1
                self.window.after(1000, self.update_countdown)

        else:
            self.confirmbtn.config(state='disabled')
            messagebox.showerror("Time limit", "time is up!!!")
            self.FOUND_STATUS = 0
            self.window.destroy()

    def assign_number(self):
        self.NUMBER = randint(self.A, self.B)

    def check(self):
        value = int(self.mainEntry.get())
        if value > self.NUMBER:
            messagebox.showerror("Wrong", "this number is bigger than my number. Try again")
        elif value < self.NUMBER:
            messagebox.showerror("Wrong", "this number is smaller than my number. Try again")
        else:
            self.FOUND_STATUS = 0
            self.countdownText.config(fg='green')
            messagebox.showinfo("Congratlation", f"{value} was my number. you have found it")
            if messagebox.askyesno("", "do you play again?"):
                self.window.after(300, self.window.destroy())
                GetRange()
            else:
                self.window.after(100, self.window.destroy())


class GetRange:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('600x400')
        self.window.title(TITLE)

        self.labelMain = tk.Label(self.window, text='input between two number', font=('Arial', 17))
        self.labelMain.pack()

        self.labelA = tk.Label(self.window, text='From:', font=('Arial', 16), pady=10)
        self.labelA.pack()

        self.entryA = tk.Entry(self.window, font=('Arial', 16), justify='center')
        self.entryA.pack()

        self.labelB = tk.Label(self.window, text='To:', font=('Arial', 16), pady=10)
        self.labelB.pack()

        self.entryB = tk.Entry(self.window, font=('Arial', 16), justify='center')
        self.entryB.pack()

        self.confirmbtn = tk.Button(self.window, text='Next', font=('Arial', 16), padx=10, pady=10,
                                    command=self.closeRange)
        self.confirmbtn.pack()

        self.window.mainloop()

    def closeRange(self):
        global A, B
        a = self.entryA.get()
        b = self.entryB.get()
        if a=='' or b=='':
            messagebox.showerror("Wrong", "wrong numbers")
        elif a >= b:
            messagebox.showerror("Wrong", "Wrong numbers")
            self.entryA.delete(0, 'end')
            self.entryB.delete(0, 'end')
        else:
            A = int(a)
            B = int(b)
            self.window.destroy()
            GetTime()


class GetTime:
    def __init__(self):
        self.time_window = tk.Tk()
        self.time_window.geometry('600x400')
        self.time_window.title(TITLE)

        self.labelT = tk.Label(self.time_window, text='input time', font=('Arial', 14), padx=10, pady=20)
        self.labelT.pack()

        self.entryT = tk.Entry(self.time_window, font=('Arial', 14), justify='center')
        self.entryT.pack()

        self.confirmbtn = tk.Button(self.time_window, text='Done', font=('Arial', 14), pady=10, command=self.closeTime)
        self.confirmbtn.pack()

        self.time_window.mainloop()

    def closeTime(self):
        global USERTIME

        usertime = self.entryT.get()
        if int(usertime) < 1:
            messagebox.showerror("Wrong", "Time limit is more than 1 secund")
            self.entryT.delete(0, 'end')
        else:
            USERTIME = int(usertime)
            self.time_window.destroy()
            Game()


class Welcome:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('600x400')
        self.window.title(TITLE)

        self.maintitle = tk.Label(self.window, text='Welcome!', font=('Arial', 20), bg='white', padx=10, pady=10)
        self.maintitle.pack()

        self.welcometext = tk.Label(self.window, text=SHARTLAR, justify='left', font=('Arial', 16), bg='white', padx=20,
                                    pady=30)
        self.welcometext.pack()

        self.closebtn = tk.Button(self.window, text='OK', font=('aria', 16), command=self.start_game)
        self.closebtn.pack()

        self.window.mainloop()

    def start_game(self):
        self.window.destroy()
        GetRange()


Welcome()