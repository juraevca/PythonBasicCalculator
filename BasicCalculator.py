from tkinter import *

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("0")      
        

def btnEqualsInput():
    try:
        global operator

        i=19
        while i>0:
            operator=operator.replace('*0','*')
            operator=operator.replace('-0','-')
            operator=operator.replace('+0','+')
            operator=operator.replace('/0','/')
            i-=1


        sumup=str(eval(operator.lstrip("0")))
        text_Input.set(sumup)
        operator=""
    except:
        text_Input.set("error")
        operator=""

#----------------------------------------------------------------------

root = Tk()
root.title("My Calculator")
root.resizable(width = False, height = False)
operator=""
text_Input=StringVar()

#----------------------------------------------------------------------
#design parameters

btn_bg = "light blue"
btn_fg="dark blue"
btn_activebackground="light blue"

val_padx=24
val_pady=11

root.configure(background="powder blue") 

#-----------------------------------------------------------------------
txtDisplay = Entry(root, font= ('arial', 28, 'bold'), textvariable=text_Input,
                   bd=5, insertwidth=9, bg="powder blue", justify='right').grid(columnspan=4, ipadx=0)


#------------------------------------------------------------------------

btn7=Button(root, padx=val_padx, bd=8, pady=val_pady, fg="dark blue", font=('arial', 20, 'bold'),
            text="7", bg="powder blue", command=lambda:btnClick(7), activebackground="light blue").grid(row=1, column=0)
btn8=Button(root, padx=val_padx, pady=val_pady, bd=8, fg="dark blue", font=('arial', 20, 'bold'),
            text="8", bg="powder blue", command=lambda:btnClick(8)).grid(row=1, column=1)
btn9=Button(root, padx=val_padx, pady=val_pady, bd=8, fg="dark blue", font=('arial', 20, 'bold'),
            text="9", bg="powder blue", command=lambda:btnClick(9)).grid(row=1, column=2)
Addition=Button(root, padx=val_padx, pady=val_pady, bd=8, fg="dark blue", font=('arial', 20, 'bold'),
            text="+", bg="powder blue", command=lambda:btnClick("+")).grid(row=1, column=3)

#-------------------------------------------------------------------------

btn4=Button(root, padx=val_padx, pady=val_pady, bd=8, fg="dark blue", font=('arial', 20, 'bold'),
            text="4", bg="powder blue", command=lambda:btnClick(4)).grid(row=2, column=0)
btn5=Button(root, padx=val_padx, pady=val_pady, bd=8, fg="dark blue", font=('arial', 20, 'bold'),
            text="5", bg="powder blue", command=lambda:btnClick(5)).grid(row=2, column=1)
btn6=Button(root, padx=val_padx, pady=val_pady, bd=8, fg="dark blue", font=('arial', 20, 'bold'),
            text="6", bg="powder blue", command=lambda:btnClick(6)).grid(row=2, column=2)
Subtraction=Button(root, padx=val_padx, pady=val_pady, bd=8, fg="dark blue", font=('arial', 20, 'bold'),
            text="-", bg="powder blue", command=lambda:btnClick("-")).grid(row=2, column=3)

#-------------------------------------------------------------------------

btn1=Button(root, padx=val_padx, pady=val_pady, bd=8, fg="dark blue", font=('arial', 20, 'bold'),
            text="1", bg="powder blue", command=lambda:btnClick(1)).grid(row=3, column=0)
btn2=Button(root, padx=val_padx, pady=val_pady, bd=8, fg="dark blue", font=('arial', 20, 'bold'),
            text="2", bg="powder blue", command=lambda:btnClick(2)).grid(row=3, column=1)
btn3=Button(root, padx=val_padx, pady=val_pady, bd=8, fg="dark blue", font=('arial', 20, 'bold'),
            text="3", bg="powder blue", command=lambda:btnClick(3)).grid(row=3, column=2)
Multiply=Button(root, padx=val_padx, pady=val_pady, bd=8, fg="dark blue", font=('arial', 20, 'bold'),
            text="*", bg="powder blue", command=lambda:btnClick("*")).grid(row=3, column=3)

#-------------------------------------------------------------------------

btn0=Button(root, padx=val_padx, pady=val_pady, bd=8, fg="dark blue", font=('arial', 20, 'bold'),
            text="0", bg="powder blue", command=lambda:btnClick(0)).grid(row=4, column=0)
btnClear=Button(root, padx=val_padx, pady=val_pady, bd=8, fg="dark blue", font=('arial', 20, 'bold'),
            text="C", bg="powder blue", command=btnClearDisplay).grid(row=4, column=1)
btnEquals=Button(root, padx=val_padx, pady=val_pady, bd=8, fg="dark blue", font=('arial', 20, 'bold'),
            text="=", bg="powder blue", command=btnEqualsInput).grid(row=4, column=2)
Division=Button(root, padx=val_padx, pady=val_pady, bd=8, fg="dark blue", font=('arial', 20, 'bold'),
            text="/", bg="powder blue", command=lambda:btnClick("/")).grid(row=4, column=3)

#-------------------------------------------------------------------------


root.mainloop()
