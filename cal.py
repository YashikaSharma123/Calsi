# Simple calculator:
from tkinter import *
from tkinter import messagebox
cal=Tk()
cal.title('Cal')

cal.resizable(0,0)

class calculator(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)
        self.createWidgets()

    def btnClick(self, text):
        self.entryText=self.text_display.get()
        self.textLength=len(self.entryText)

        if self.entryText=='0':
            self.replaceText(text)
        else:
            self.text_display.insert(self.textLength,text)
    def replaceText(self, text):
        self.text_display.delete(0, END)
        self.text_display.insert(0, text)

    def btnClear(self):

        self.replaceText('0')

    def btnEquals(self):
        self.expression = self.text_display.get()
        self.expression = self.expression.replace('%', '/ 100')

        try:
            self.result = eval(self.expression)
            self.replaceText(self.result)
        except:
           messagebox.showinfo('Error','Invalid Input')

    def createWidgets(self):

        self.text_display=Entry(self,font=('arial',20,'bold'),
                           bd=30,insertwidth=3,bg='cyan',justify='right')
        self.text_display.insert(0,'0')
        self.text_display.grid(columnspan=5)

        ##########################################################################################################

        self.button7=Button(self,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='7',
                            command =lambda: self.btnClick('7'))
        self.button7.grid(row=1,column=0)

        self.button8=Button(self,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='8',
                            command =lambda: self.btnClick('8'))
        self.button8.grid(row=1,column=1)

        self.button9=Button(self,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='9',
                            command =lambda: self.btnClick('9'))
        self.button9.grid(row=1,column=2)

        self.buttondev = Button(self, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='/',
                                command=lambda: self.btnClick('/'))
        self.buttondev.grid(row=1, column=3)

        self.buttonPow = Button(self, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='ln',
                                command=lambda: self.btnClick('ln'))
        self.buttonPow.grid(row=1, column=4)


        ##########################################################################################################

        self.button4 = Button(self, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='4',
                              command=lambda: self.btnClick('4'))
        self.button4.grid(row=2, column=0)

        self.button5 = Button(self, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='5',
                              command=lambda: self.btnClick('5'))
        self.button5.grid(row=2, column=1)

        self.button6 = Button(self, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='6',
                              command=lambda: self.btnClick('6'))
        self.button6.grid(row=2, column=2)

        self.buttonMul = Button(self, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='*',
                                command=lambda: self.btnClick('*'))
        self.buttonMul.grid(row=2, column=3)

        self.buttonPercentage = Button(self, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='%',
                                       command=lambda: self.btnClick('%'))
        self.buttonPercentage.grid(row=2, column=4)

        ###########################################################################################################

        self.button1 = Button(self, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='1',
                              command=lambda: self.btnClick('1'))
        self.button1.grid(row=3, column=0)

        self.button2 = Button(self, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='2',
                              command=lambda: self.btnClick('2'))
        self.button2.grid(row=3, column=1)

        self.button3 = Button(self, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='3',
                              command=lambda: self.btnClick('3'))
        self.button3.grid(row=3, column=2)

        self.buttonSub = Button(self, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='-',
                                command=lambda: self.btnClick('-'))
        self.buttonSub.grid(row=3, column=3)

        self.buttonClr = Button(self, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='C',
                                command= self.btnClear)
        self.buttonClr.grid(row=3, column=4)


    ###########################################################################################################

        self.button0 = Button(self, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='0',
                               command=lambda: self.btnClick('0'))
        self.button0.grid(row=4, column=0)

        self.buttonAdd = Button(self, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='.',
                                command=lambda: self.btnClick('.'))
        self.buttonAdd.grid(row=4, column=1)

        self.buttonAdd = Button(self, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='+',
                                command=lambda: self.btnClick('+'))
        self.buttonAdd.grid(row=4, column=2)

        self.buttonEqu = Button(self, padx=16, pady=16, bd=8, fg='blue', font=('arial', 20, 'bold'), text='=',
                                command= self.btnEquals)
        self.buttonEqu.grid(row=4, column=3, columnspan=2, sticky='NWNESWSE')

app=calculator(cal).grid()
cal.mainloop()