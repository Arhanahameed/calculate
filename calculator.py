from tkinter import *
window = Tk()
window.title("simple calculator")
window.iconbitmap("C:/Users/admin/Desktop/pythonpractise/Modules/GUI/icon.ico")
e = Entry(width=60,borderwidth=5)
e.grid(row=0,column=0,columnspan=3)

def btonclc(number):
    current= e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def clear():
    e.delete(0,END)

def buttonadd():
    global f_num,math
    math =1
    firstnum = e.get()
    e.delete(0,END)
    f_num = int(firstnum)

def buttonsub():
    global f_num,math
    math = 2
    firstnum = e.get()
    e.delete(0,END)
    f_num = int(firstnum)
    
def buttonmul():
    global f_num,math
    math=3
    firstnum = e.get()
    e.delete(0,END)
    f_num = int(firstnum)


def buttondiv():
    global f_num , math
    math = 4
    firstnum = e.get()
    e.delete(0,END)
    f_num = int(firstnum)

def equal():
    second_num = e.get()
    s_num = int(second_num)
    e.delete(0,END)
    if math==1:
        e.insert(0,f_num+s_num) 
    elif math ==2:
        e.insert(0,f_num-s_num)
    elif math==3:
        e.insert(0,f_num* s_num)
    else:
        e.insert(0,f_num/ s_num)    







button1=Button(text=1,padx=40,pady=20,command=lambda:btonclc(1),).grid(row=1,column=0)
button2=Button(text=2,padx=40,pady=20,command=lambda:btonclc(2)).grid(row=1,column=1)
button3=Button(text=3,padx=40,pady=20,command=lambda:btonclc(3)).grid(row=1,column=2)
button4=Button(text=4,padx=40,pady=20,command=lambda:btonclc(4)).grid(row=2,column=0)
button5=Button(text=5,padx=40,pady=20,command=lambda:btonclc(5)).grid(row=2,column=1)
button6=Button(text=6,padx=40,pady=20,command=lambda:btonclc(6)).grid(row=2,column=2)
button7=Button(text=7,padx=40,pady=20,command=lambda:btonclc(7)).grid(row=3,column=0)
button8=Button(text=8,padx=40,pady=20,command=lambda:btonclc(8)).grid(row=3,column=1)
button9=Button(text=9,padx=40,pady=20,command=lambda:btonclc(9)).grid(row=3,column=2)
button0 =Button(text=0,padx=40,pady=20,command=lambda:btonclc(0)).grid(row=4,column=0)
buttonclear =Button(text="clear",padx=90,pady=20,borderwidth=3,command= clear).grid(row=4,column=1,columnspan=2)
buttonequal= Button(text= "=" ,padx =100,pady=20,borderwidth=3 , command=equal).grid(row=5,column=1,columnspan=2)
button_add= Button(text="+",padx=40,pady=20 ,command= buttonadd).grid(row=5,column=0)
button_sub= Button(text="-",padx=40,pady=20,command= buttonsub).grid(row=6,column=0)
button_mul= Button(text="*",padx=40,pady=20,command=buttonmul).grid(row=6,column=1)
button_div= Button(text="/",padx=40,pady=20 , command = buttondiv).grid(row=6,column=2)
window.mainloop()




