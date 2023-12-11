import tkinter as tk

# root = tk.Tk()
#
# root.geometry("1920x1080")
# root.title("game")
#
# label = tk.Label(root, text="Hello world!", font=('Arial', 18))
# label.pack(pady=20)
#
# textbox = tk.Text(root, height=1, width=50, font=("Arial", 18))
# textbox.pack(padx=10)
#
# # myenter = tk.Entry(root)
# # myenter.pack()
#
# btn = tk.Button(root, text="click", font=('Arial', 18), background='green')
# btn.pack(pady=20)



# root.mainloop()


class MyGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x400")
        self.root.title('app')
        self.shart = tk.Label(self.root, text="The game's task is \n you input among numbers\n"
                                              "and i think about one number\n in between this numbers.\n "
                                              "Then you find number\n which i thinked in some time.", font=('Arial', 15))
        self.shart.pack(pady=40)
        self.btn = tk.Button(self.root, text='Ok', width=10, font=('Arial', 18), command=self.show_msg)
        self.btn.pack(pady=20)
        self.root.mainloop()

    def show_msg(self):
        self.root.destroy()
        self.numbers = tk.Tk()
        self.numbers.geometry("500x400")
        self.numbers.title('numbers')
        self.label = tk.Label(self.numbers, text="From", font=('Arial', 15))
        self.label.pack(pady=10)
        self.first_n = tk.Entry(self.numbers,  font=('Arial', 16))
        self.first_n.pack(pady=5)

        self.label2 = tk.Label(self.numbers, text="To", font=('Arial', 15))
        self.label2.pack(pady=10)
        self.secod_n = tk.Entry(self.numbers,  font=('Arial', 16))
        self.secod_n.pack(pady=5)

        self.label3 = tk.Label(self.numbers, text="Input Time", font=('Arial', 15))
        self.label3.pack(pady=10)
        self.secod_n = tk.Entry(self.numbers,  font=('Arial', 16))
        self.secod_n.pack(pady=5)


        self.nums = tk.Button(self.numbers, text='Submit', font=('Arial', 16), fg='white', background='green', command=self.game)
        self.nums.pack(pady=30)

    def game(self):
        self.numbers.destroy()
        self.game = tk.Tk()
        self.game.geometry("500x400")
        self.game.title('game')

MyGUI()
