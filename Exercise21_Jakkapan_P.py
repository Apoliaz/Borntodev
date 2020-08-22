from tkinter import *
import math

def leftClickButton(event):
    result = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if result >= 30.0:
        result = "อ้วนมาก"
    elif result > 24.9 and result < 30.0:
        result = "อ้วน"
    elif result > 22.9 and result <= 24.9:
        result = "น้ำหนักเกิน"
    elif result > 18.5 and result <= 22.9:
        result = "น้ำหนักปกติ เหมาะสม"
    elif result < 18.5:
        result = "ผอมเกินไป"
    labelResult.configure(text=result)

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)

MainWindow.mainloop()