import tkinter as tk


class Watch:
    def __init__(self):
        self.h = 0
        self.m = 59
        self.s = 57

    def update_time(self):
        self.s += 1
        if self.s == 60:
            self.m += 1
            self.s = 0
            if self.m == 60:
                self.h += 1
                self.m = 0

        time_str = f"{self.h:02d}:{self.m:02d}:{self.s:02d}"
        label_time.config(text=time_str)
        label_time.after(1000, self.update_time)


watch = Watch()

win = tk.Tk()
label_time = tk.Label(win, text="00:00:00", font=("Times New Roman", 40, "bold"), fg="red")
label_time.pack()

watch.update_time()

win.mainloop()
