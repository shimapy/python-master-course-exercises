# import and global variables
import tkinter as tk
expr = ""

class CalculatorApp():
    
    def __init__(self):
        self.create_form()
        self.calculat_string.set("")
        self.show_info_label.configure(text="")
    
    def number_btn_click(self, num:str):
        global expr
        expr += str(num)
        self.calculat_string.set(self.calculat_string.get() + num)

    def operator_btn_click(self, key:str):
        global expr
        expr += str(key)
        self.show_info_label.configure(text=self.calculat_string.get() + key)
        self.calculat_string.set("")

    def equal_btn_click(self):
        global expr
        try:
            self.show_info_label.configure(text=expr + "=")
            result = str(eval(expr))
            self.calculat_string.set(result)
            expr = result
        except ZeroDivisionError:
            expr = ""
            self.calculat_string.set("Cannot divide by zero")
        except Exception as e1:
            expr = ""
            # print(str(e1))
            self.calculat_string.set("error")

    def clear_btn_click(self):
        global expr
        expr = ""
        self.calculat_string.set("")
        self.show_info_label.configure(text="")
    
    # ui design
    def create_form(self):
        
        frm = tk.Frame(window, padx=40, pady=20)
        frm.grid()
        # input entry
        self.show_info_label = tk.Label(frm)
        self.show_info_label.grid(column=1, row=0, columnspan=4, sticky="nsew")
        self.calculat_string = tk.StringVar()
        self.calculate_entry = tk.Entry(frm, textvariable=self.calculat_string)
        self.calculate_entry.grid(column=1, row=1, columnspan=4, rowspan=2, sticky="nsew")
        # buttons
        tk.Button(frm, text="7", width=10, height=2, command=lambda: self.number_btn_click("7")).grid(column=1, row=3)
        tk.Button(frm, text="8", width=10, height=2, command=lambda: self.number_btn_click("8")).grid(column=2, row=3)
        tk.Button(frm, text="9", width=10, height=2, command=lambda: self.number_btn_click("9")).grid(column=3, row=3)
        tk.Button(frm, text="+", width=10, height=2, command=lambda: self.operator_btn_click("+")).grid(column=4, row=3)
        tk.Button(frm, text="4", width=10, height=2, command=lambda: self.number_btn_click("4")).grid(column=1, row=4)
        tk.Button(frm, text="5", width=10, height=2, command=lambda: self.number_btn_click("5")).grid(column=2, row=4)
        tk.Button(frm, text="6", width=10, height=2, command=lambda: self.number_btn_click("6")).grid(column=3, row=4)
        tk.Button(frm, text="-", width=10, height=2, command=lambda: self.operator_btn_click("-")).grid(column=4, row=4)
        tk.Button(frm, text="1", width=10, height=2, command=lambda: self.number_btn_click("1")).grid(column=1, row=5)
        tk.Button(frm, text="2", width=10, height=2, command=lambda: self.number_btn_click("2")).grid(column=2, row=5)
        tk.Button(frm, text="3", width=10, height=2, command=lambda: self.number_btn_click("3")).grid(column=3, row=5)
        tk.Button(frm, text="*", width=10, height=2, command=lambda: self.operator_btn_click("*")).grid(column=4, row=5)
        tk.Button(frm, text="c", width=10, height=2, command=self.clear_btn_click).grid(column=1, row=6)
        tk.Button(frm, text="0", width=10, height=2, command=lambda: self.number_btn_click("0")).grid(column=2, row=6)
        tk.Button(frm, text="=", width=10, height=2, command=self.equal_btn_click).grid(column=3, row=6)
        tk.Button(frm, text="/", width=10, height=2, command=lambda: self.operator_btn_click("/")).grid(column=4, row=6)


# running application
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Python Calculator")
    window.resizable(width=False, height=False)
    window.geometry("400x300")
    CalculatorApp()
    window.mainloop()
