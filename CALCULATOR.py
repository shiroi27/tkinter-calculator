from tkinter import Tk , Entry , Button , StringVar

class Calculator:
    def __init__(self,master):
        master.title(" CALCULATOR ") # For the title
        master.geometry('539x600+100+100') # width x height + x offset + y offset
        master.config(bg="#84e7e1")
        master.resizable(False,False)
        
        self.equation = StringVar()
        self.entry_value=''
        Entry(width=31,bg = "#F4DE50",fg="#000000",font=('Times New Roman', 70, 'bold') ,textvariable=self.equation).place(x=0,y=0,height = 100)
        
        # Button Style Config
        btn_kwargs = {
            "bg": "#84e7e1",
            "fg": "#000000",
            "font": ('Times New Roman', 30, 'bold'),
            "activebackground": "#00ffe1",    # Neon hover
            "highlightbackground": "#00ffe1", # Neon border
            "highlightcolor": "#00ffe1",
            "highlightthickness": 2,
            "relief": "flat",
            "bd": 0
        }
        # Row 1
        Button( text="(",command=lambda:self.show("("), **btn_kwargs).place(x = 0, y = 100, width=130, height=100)
        Button( text=")",command=lambda:self.show(")"), **btn_kwargs).place(x = 135, y = 100, width=130, height=100)
        Button( text="%",command=lambda:self.show("%"), **btn_kwargs).place(x = 270, y = 100, width=130, height=100)
        Button( text="/",command=lambda:self.show("/"), **btn_kwargs).place(x = 405, y = 100, width=130, height=100)
        # Row 2
        Button( text="1",command=lambda:self.show(1), **btn_kwargs).place(x = 0, y = 200, width=130, height=100)
        Button( text="2",command=lambda:self.show(2), **btn_kwargs).place(x = 135, y = 200, width=130, height=100)
        Button( text="3",command=lambda:self.show(3), **btn_kwargs).place(x = 270, y = 200, width=130, height=100)
        Button( text="*",command=lambda:self.show("*"), **btn_kwargs).place(x = 405, y = 200, width=130, height=100)
        # Row 3
        Button( text="4",command=lambda:self.show(4), **btn_kwargs).place(x = 0, y = 300, width=130, height=100)
        Button( text="5",command=lambda:self.show(5), **btn_kwargs).place(x = 135, y = 300, width=130, height=100)
        Button( text="6",command=lambda:self.show(6), **btn_kwargs).place(x = 270, y = 300, width=130, height=100)
        Button( text="+",command=lambda:self.show("+"), **btn_kwargs).place(x = 405, y = 300, width=130, height=100)
        # Row 4
        Button( text="7",command=lambda:self.show(7), **btn_kwargs).place(x = 0, y = 400, width=130, height=100)
        Button( text="8",command=lambda:self.show(8), **btn_kwargs).place(x = 135, y = 400, width=130, height=100)
        Button( text="9",command=lambda:self.show(9), **btn_kwargs).place(x = 270, y = 400, width=130, height=100)
        Button( text="-",command=lambda:self.show("-"), **btn_kwargs).place(x = 405, y = 400, width=130, height=100)
        # Row 5
        Button( text="AC",command=self.clear, **btn_kwargs).place(x = 0, y = 500, width=130, height=100)
        Button( text="0",command=lambda:self.show(0), **btn_kwargs).place(x = 135, y = 500, width=130, height=100)
        Button( text=".",command=lambda:self.show("."), **btn_kwargs).place(x = 270, y = 500, width=130, height=100)
        Button( text="=",command=self.solve, **btn_kwargs).place(x = 405, y = 500, width=130, height=100)

    def show (self , value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)
        
    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)
        
    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)
        
        
root = Tk() # Create the main window
cal = Calculator(root)
root.mainloop() # keep the window open