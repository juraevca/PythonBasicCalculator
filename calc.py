import tkinter as tk


class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Calculator')
        self.pack(expand=1, fill=tk.BOTH)
        self.option_add('*Font', 'Hack 24 bold')
        self.create_widgets()

    def create_widgets(self):
        user_input = tk.StringVar()

        input_box = tk.Entry(self, relief=tk.SUNKEN,
                             textvariable=user_input,
                             bd=10, justify='center',
                             font=("Hack", 32), bg="black")
        input_box.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
        input_box.bind("<KeyPress-Return>",
                       lambda e, obj=user_input: App.calc(obj), "+")

        erase = App.build_frame(self, tk.TOP)
        for clear_button in ("C", "CE"):
            App.button(erase, tk.LEFT, clear_button,
                       lambda obj=user_input: obj.set(''))

        for row in ("789/", "456*", "123-", "0.+"):
            row_frame = App.build_frame(self, tk.TOP)
            for n in row:
                App.button(row_frame, tk.LEFT, n,
                           lambda x=user_input, y=n: x.set(x.get() + y))

        equals_frame = App.build_frame(self, tk.TOP)
        equals_button = App.button(equals_frame, tk.LEFT, "=")
        equals_button.bind("<ButtonRelease-1>",
                           lambda e, obj=user_input: App.calc(obj), "+")

    @staticmethod
    def build_frame(source, side):
        obj = tk.Frame(source, borderwidth=4, bd=4, bg="dark gray")
        obj.pack(side=side, expand=tk.YES, fill=tk.BOTH)
        return obj

    @staticmethod
    def button(source, side, text, command=None):
        obj = tk.Button(source, text=text, command=command)
        obj.pack(side=side, expand=1, fill=tk.BOTH)
        return obj

    @staticmethod
    def calc(display):
        exp = display.get()
        ops = None
        for op in "*/-+":
            if op in exp:
                ops = exp.split(op)
        if not ops:
            display.set("Error")
            return
        is_a_num = True
        for field in ops:
            if not field.isnumeric():
                if "." not in field:
                    is_a_num = False
                else:
                    for element in field.split("."):
                        if not element.isnumeric():
                            is_a_num = False
        if not is_a_num:
            display.set("Error")
            return
        result = eval(exp)
        display.set(result)


if __name__ == "__main__":
    App(tk.Tk()).mainloop()
