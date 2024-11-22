import tkinter as tk
from time import strftime

class DigitalClock:
    def __init__(self,root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("300x150")
        self.root.configure(bg='black')

        self.time_label = tk.Label(self.root , font=("red", 48), bg="black" , fg='lightblue', pady=20)
        self.time_label.pack()

        self.clock_screen()

    def clock_screen(self):
        current_time = strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.time_label.after(1000 , self.clock_screen)

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClock(root)
    root.mainloop()
