from tkinter import * #import every single modules from tkinter
import tkinter.messagebox #uses the module messagebox that will be use for validation of input errors
import math #math libraries for mathematical computations
from functools import partial
from currency_converter import CurrencyConverter
from unitconvert import digitalunits
from unitconvert import volumeunits
from unitconvert import lengthunits
from unitconvert import timeunits
from tkinter import ttk


root = Tk()
root.geometry("600x600")
root.title("Scientific Calculator")

#temporary variable that can be used as a global variable in temperature computation
tempVal = "Celsius"

switch = None

#Functions for onPress Displays and computations. this will make sure that everything you click inside the program will output. line 14 - 317

def onPressed1():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')


def onPressed2():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')


def onPressed3():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')


def onPressed4():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')


def onPressed5():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')


def onPressed6():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')


def onPressed7():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')


def onPressed8():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')


def onPressed9():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')


def onPressed0():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


def key_event(*args):
    if disp.get() == '0':
        disp.delete(0, END)


def onPressed_plus():
    pos = len(disp.get())
    disp.insert(pos, '+')


def onPressed_minus():
    pos = len(disp.get())
    disp.insert(pos, '-')


def onPressed_multiply():
    pos = len(disp.get())
    disp.insert(pos, '*')


def onPressed_divide():
    pos = len(disp.get())
    disp.insert(pos, '/')


def onPressed_clear(*args):
    disp.delete(0, END)
    disp.insert(0, '0')


def onPressed_sin():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.sin(math.radians(ans))
        else:
            ans = math.sin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("MATH ERROR", "CHECK YOUR INPUT")


def onPressed_cosine():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.cos(math.radians(ans))
        else:
            ans = math.cos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("MATH ERROR", "CHECK YOUR INPUT")


def onPressed_tangent():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.tan(math.radians(ans))
        else:
            ans = math.tan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("MATH ERROR", "CHECK YOUR INPUT")


def onPressed_asin():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.asin(ans))
        else:
            ans = math.asin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("MATH ERROR", "CHECK YOUR INPUT")


def onPressed_acosine():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.acos(ans))
        else:
            ans = math.acos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("MATH ERROR", "CHECK YOUR INPUT")


def onPressed_atangent():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.atan(ans))
        else:
            ans = math.atan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("MATH ERROR", "CHECK YOUR INPUT")


def onPressed_power():
    pos = len(disp.get())
    disp.insert(pos, '**')


def onPressed_squared():
    ans = int(disp.get())
    ans = math.pow(ans,2)
    disp.delete(0,END)
    disp.insert(0,int(ans))

    
def onPressed_roundoff():
    try:
        ans = float(disp.get())
        ans = round(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("MATH ERROR", "CHECK YOUR INPUT")


def onPressed_log():
    try:
        ans = float(disp.get())
        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("MATH ERROR", "CHECK YOUR INPUT")


def onPressed_factorial():
    try:
        ans = float(disp.get())
        ans = math.factorial(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("MATH ERROR", "CHECK YOUR INPUT")


def onPressed_sqrt():
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("MATH ERROR", "CHECK YOUR INPUT")


def onPressed_decimal():
    pos = len(disp.get())
    disp.insert(pos, '.')


def onPressed_pi():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))


def onPressed_pOpen():
    pos = len(disp.get())
    disp.insert(pos, '(')


def onPressed_pClose():
    pos = len(disp.get())
    disp.insert(pos, ')')


def onPressed_delete():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])


def onPressed_ln():
    try:
        ans = float(disp.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("MATH ERROR", "CHECK YOUR INPUT")


def onPressed_modulo():
    pos = len(disp.get())
    disp.insert(pos, '%')


def onPressed_equal(*args):
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)

    except:
        tkinter.messagebox.showerror("MATH ERROR", "CHECK YOUR INPUT")


#Functions for temp, and currency
def onPressed_options(options):

    def store_temp(sel_temp):
        
        global tempVal
        tempVal = sel_temp
        print(tempVal)

    # temp convertion
    def tempConverter_compute(rlabel1, rlabe12, inputn):
        tem = inputn.get()
        global tempVal
        if tempVal == 'Celsius':
            f = float((float(tem) * 9 / 5) + 32)
            k = float((float(tem) + 273.15))
            rlabel1.config(text="%f Fahrenheit" % f)
            rlabe12.config(text="%f Kelvin" % k)
        if tempVal == 'Fahrenheit':
            c = float((float(tem) - 32) * 5 / 9)
            k = c + 273
            rlabel1.config(text="%f Celsius" % c)
            rlabe12.config(text="%f Kelvin" % k)
        if tempVal == 'Kelvin':
            c = float((float(tem) - 273.15))
            f = float((float(tem) - 273.15) * 1.8000 + 32.00)
            rlabel1.config(text="%f Celsius" % c)
            rlabe12.config(text="%f Fahrenheit" % f)
        return

    if options == "Temp":
        tempWin = Toplevel(root)
        tempWin.geometry('400x150+100+200')
        tempWin.title('Temperature Converter')
        tempWin.configure(background='#333333')
        tempWin.resizable(width=False, height=False)
        tempWin.grid_columnconfigure(1, weight=1)
        tempWin.grid_rowconfigure(0, weight=1)

        numberInput = StringVar()
        var = StringVar()

# label and entry field
        inputLabel = Label(tempWin, text="Enter temperature", fg="white", bg="#333333")
        inputEntry = Entry(tempWin, textvariable=numberInput)
        inputLabel.grid(row=1)
        inputEntry.grid(row=1, column=1)

# result label's for showing the other two temperatures
        resultLabel1 = Label(tempWin, fg="white", bg="#333333")
        resultLabel1.grid(row=3, columnspan=4)
        resultLabel2 = Label(tempWin, fg="white", bg="#333333")
        resultLabel2.grid(row=4, columnspan=4)

# drop down initalization and setup
        optionsMenu_list = ["Celsius", "Fahrenheit", "Kelvin"]
        optionsMenu = OptionMenu(tempWin, var, *optionsMenu_list, command=store_temp)
        var.set(optionsMenu_list[0])
        optionsMenu.grid(row=1, column=3)
        optionsMenu.config(fg="white", bg="#333333")
        optionsMenu["menu"].config(fg="white", bg="#333333")

# button click
        tempConverter_compute = partial(tempConverter_compute, resultLabel1, resultLabel2, numberInput)
        result_button = Button(tempWin, text="Convert", command=tempConverter_compute, fg="white", bg="#333333")
        result_button.grid(row=2, columnspan=4)

    if options == "Currency":

        def currencyConvertion():

            c = CurrencyConverter()

            from_curr = variable1.get()
            to_curr = variable2.get()

            if (Amount1_field.get() == ""):
                #this will show if you pressed convert without inputting an amount
                tkinter.messagebox.showinfo("ERROR!", "Please Enter the Amount.")
            elif (from_curr == "currency" or to_curr == "currency"):
                #this will show if you did not select a currency but pressed convert
                tkinter.messagebox.showinfo("ERROR!", "Currency Not Selected")
            #if any above conditions goes false, else will execute which will covert the currency
            else:
                new_amt = c.convert(float(Amount1_field.get()), from_curr, to_curr)
                new_amount = float("{:.4f}".format(new_amt))
                Amount2_field.insert(0, str(new_amount))
        
        #clears all fields
        def clear():
            Amount1_field.delete(0, END)
            Amount2_field.delete(0, END)

            
        #currency list as of now. YOU CAN ADD MORE BY ADDING THE CURRENCY'S ABBREVIATION INTO THE LIST ;)
        currencyList = ["PHP", "USD", "CAD", "EUR", "JPY", "CNY", "GBP", "KRW"]
        # sorts the list alphabetically
        currencyList.sort()

        currencyWin = Toplevel(root)
        currencyWin.geometry('400x150')
        currencyWin.title('currency')
        currencyWin.configure(background='#333333')
        
        variable1 = StringVar()
        variable2 = StringVar()

        label1 = Label(currencyWin, font= "Arial 15",text="Amount:", fg="white", bg="#333333")
        label1.grid(row=3, column=0, sticky=W)

        label1 = Label(currencyWin,font= "Arial 15", text="From Currency:", fg="white", bg="#333333")
        label1.grid(row=6, column=0, sticky=W)

        label1 = Label(currencyWin,font= "Arial 15", text="To Currency:", fg="white", bg="#333333")
        label1.grid(row=8, column=0, sticky=W)

        label1 = Label(currencyWin,font= "Arial 15", text="Converted Amount:", fg="white", bg="#333333")
        label1.grid(row=11, column=0, sticky=W)        

        FromCurrency_option = OptionMenu(currencyWin, variable1, *currencyList)
        ToCurrency_option = OptionMenu(currencyWin, variable2, *currencyList)
        FromCurrency_option.grid(row=6, column=1, ipadx=45, sticky=E)
        ToCurrency_option.grid(row = 8, column=1, ipadx=45, sticky=E)

        Amount1_field = Entry(currencyWin)
        Amount1_field.grid(row=3, column=1, ipadx=31, sticky=E)
        Amount2_field = Entry(currencyWin)
        Amount2_field.grid(row=11, column=1, ipadx=31, sticky=E)

        label2 = Button(currencyWin, text= "Convert", bd=2, command= currencyConvertion)
        label2.grid(row=10, column=1)

        label2 = Button(currencyWin, text= "Clear All", bd=2, command= clear)
        label2.grid(row=10, column=0)

    if options == "Data":
        dataWin = Toplevel(root)
        dataWin.geometry('400x150')
        dataWin.title('Data')
        dataWin.configure(background='#333333')

        userin = IntVar()
        resultin = IntVar()
        uf = StringVar()
        us = StringVar()

        def dataConvert():
            a = digitalunits.DigitalUnit(userin.get(),f'{uf.get()}',f'{us.get()}').doconvert()
            resultin.set(a)

        def reset():
            userinput.delete(0, END)
            result.delete(0, END)


        userinput = Entry(dataWin, textvariable= userin,width=10)
        userinput.grid(row=1, column=0, padx= 10, pady=10)

        unitfirst = ttk.Combobox(dataWin,textvariable=uf, width=5)
        unitfirst['value'] = ('B','kB','MB','GB','TB','PB','EB','ZB','YB')
        unitfirst.grid(row= 1, column = 1, ipadx=31, padx=10, pady=10)
        
        result = Entry(dataWin, textvariable=resultin, width=20)
        result.grid(row=2, column=0, padx=10, pady=10)

        unitsecond = ttk.Combobox(dataWin, textvariable=us,width=5)
        unitsecond['value'] = ('B','kB','MB','GB','TB','PB','EB','ZB','YB')
        unitsecond.grid(row=2, column=1 ,padx=10, pady=10)

        convertButton = Button(dataWin, command=dataConvert,text= "Convert", bd = 2, fg="white", bg="#333333")
        convertButton.grid(row=3, column=1, pady=10, padx= 10)

        resetButton = Button(dataWin, command=reset,text= "Reset", bd=2, fg="white", bg="#333333")
        resetButton.grid(row=3, column=0, padx=10, pady=10)

    if options == "Volume":
        volWin = Toplevel(root)
        volWin.geometry('400x150')
        volWin.title('Volume')
        volWin.configure(background='#333333')

        userin = IntVar()
        resultin = IntVar()
        uf = StringVar()
        us = StringVar()

        def volumeConvert():
            a = volumeunits.VolumeUnit(userin.get(),f'{uf.get()}',f'{us.get()}').doconvert()
            resultin.set(a)

        def reset():
            userinput.delete(0, END)
            result.delete(0, END)


        userinput = Entry(volWin, textvariable= userin,width=10)
        userinput.grid(row=1, column=0, padx= 10, pady=10)

        unitfirst = ttk.Combobox(volWin,textvariable=uf, width=5)
        unitfirst['value'] = ('ml','l','floz','gal')
        unitfirst.grid(row= 1, column = 1, ipadx=31, padx=10, pady=10)
        
        result = Entry(volWin, textvariable=resultin, width=20)
        result.grid(row=2, column=0, padx=10, pady=10)

        unitsecond = ttk.Combobox(volWin, textvariable=us,width=5)
        unitsecond['value'] = ('ml','l','floz','gal')
        unitsecond.grid(row=2, column=1 ,padx=10, pady=10)

        convertButton = Button(volWin, command=volumeConvert,text= "Convert", bd = 2, fg="white", bg="#333333")
        convertButton.grid(row=3, column=1, pady=10, padx= 10)

        resetButton = Button(volWin, command=reset,text= "Reset", bd=2, fg="white", bg="#333333")
        resetButton.grid(row=3, column=0, padx=10, pady=10)

    if options == "Time":
        timeWin = Toplevel(root)
        timeWin.geometry('400x150')
        timeWin.title('Time')
        timeWin.configure(background='#333333')

        userin = IntVar()
        resultin = IntVar()
        uf = StringVar()
        us = StringVar()

        def lenConvert():
            a = timeunits.TimeUnit(userin.get(),f'{uf.get()}',f'{us.get()}').doconvert()
            resultin.set(a)

        def reset():
            userinput.delete(0, END)
            result.delete(0, END)


        userinput = Entry(timeWin, textvariable= userin,width=10)
        userinput.grid(row=1, column=0, padx= 10, pady=10)

        unitfirst = ttk.Combobox(timeWin,textvariable=uf, width=5)
        unitfirst['value'] = ('ms','sec','min','hr', 'day', 'wk', 'mo', 'yr')
        unitfirst.grid(row= 1, column = 1, ipadx=31, padx=10, pady=10)
        
        result = Entry(timeWin, textvariable=resultin, width=20)
        result.grid(row=2, column=0, padx=10, pady=10)

        unitsecond = ttk.Combobox(timeWin, textvariable=us,width=5)
        unitsecond['value'] = ('ms','sec','min','hr', 'day', 'wk', 'mo', 'yr')
        unitsecond.grid(row=2, column=1 ,padx=10, pady=10)

        convertButton = Button(timeWin, command=lenConvert,text= "Convert", bd = 2, fg="white", bg="#333333")
        convertButton.grid(row=3, column=1, pady=10, padx= 10)

        resetButton = Button(timeWin, command=reset,text= "Reset", bd=2, fg="white", bg="#333333")
        resetButton.grid(row=3, column=0, padx=10, pady=10)

    if options == "Length":
        lenWin = Toplevel(root)
        lenWin.geometry('400x150')
        lenWin.title('Time')
        lenWin.configure(background='#333333')

        userin = IntVar()
        resultin = IntVar()
        uf = StringVar()
        us = StringVar()

        def lenConvert():
            a = lengthunits.LengthUnit(userin.get(),f'{uf.get()}',f'{us.get()}').doconvert()
            resultin.set(a)

        def reset():
            userinput.delete(0, END)
            result.delete(0, END)


        userinput = Entry(lenWin, textvariable= userin,width=10)
        userinput.grid(row=1, column=0, padx= 10, pady=10)

        unitfirst = ttk.Combobox(lenWin,textvariable=uf, width=5)
        unitfirst['value'] = ('mm','cm','m','in', 'ft', 'yd', 'km', 'mi')
        unitfirst.grid(row= 1, column = 1, ipadx=31, padx=10, pady=10)
        
        result = Entry(lenWin, textvariable=resultin, width=20)
        result.grid(row=2, column=0, padx=10, pady=10)

        unitsecond = ttk.Combobox(lenWin, textvariable=us,width=5)
        unitsecond['value'] = ('mm','cm','m','in', 'ft', 'yd', 'km', 'mi')
        unitsecond.grid(row=2, column=1 ,padx=10, pady=10)

        convertButton = Button(lenWin, command=lenConvert,text= "Convert", bd = 2, fg="white", bg="#333333")
        convertButton.grid(row=3, column=1, pady=10, padx= 10)

        resetButton = Button(lenWin, command=reset,text= "Reset", bd=2, fg="white", bg="#333333")
        resetButton.grid(row=3, column=0, padx=10, pady=10)        



#this will guarantee that it you press 1 it will output 1
data = StringVar()
optionsList = ["Scientific", "Temp", "Currency", "Data", "Volume", "Length", "Time"]
options = OptionMenu(root, data, *optionsList, command=onPressed_options)
data.set(optionsList[0])
options.pack(fill=BOTH)
disp = Entry(root, font="Arial 17", fg="black", bg="#abbab1", bd=0, justify=RIGHT, insertbackground="#abbab1", cursor="arrow")
disp.bind("<Return>", onPressed_equal)
disp.bind("<Escape>", onPressed_delete)
disp.bind("<Key-1>", key_event)
disp.bind("<Key-2>", key_event)
disp.bind("<Key-3>", key_event)
disp.bind("<Key-4>", key_event)
disp.bind("<Key-5>", key_event)
disp.bind("<Key-6>", key_event)
disp.bind("<Key-7>", key_event)
disp.bind("<Key-8>", key_event)
disp.bind("<Key-9>", key_event)
disp.bind("<Key-0>", key_event)
disp.bind("<Key-.>", key_event)
disp.insert(0, '0')
disp.focus_set()
disp.pack(expand=TRUE, fill=BOTH)


btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=TRUE, fill=BOTH)

button_squared = Button(btnrow1, text="n²", font="Arial 20", relief=RIDGE, bd=0, command=onPressed_squared, fg="white", bg="#333333")
button_squared.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_ln = Button(btnrow1, text="ln", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_ln, fg="white", bg="#333333")
button_ln.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_log = Button(btnrow1, text="log", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_log, fg="white", bg="#333333")
button_log.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_clear = Button(btnrow1, text="C", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_clear, fg="white", bg="#333333")
button_clear.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_delete = Button(btnrow1, text="⌫", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_delete, fg="white", bg="#333333")
button_delete.pack(side=LEFT, expand=TRUE, fill=BOTH)


# Buttons for Row 2: pi, sin, cosine, tangent, factorial

btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)

button_pi = Button(btnrow2, text=" π", font="Arial 20", relief=RIDGE, bd=0, command=onPressed_pi, fg="white", bg="#333333")
button_pi.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_sin = Button(btnrow2, text=" sin", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_sin, fg="white", bg="#333333")
button_sin.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_cosine = Button(btnrow2, text="cos", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_cosine, fg="white", bg="#333333")
button_cosine.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_tangent = Button(btnrow2, text="tan", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_tangent, fg="white", bg="#333333")
button_tangent.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_fact = Button(btnrow2, text=" n! ", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_factorial, fg="white", bg="#333333")
button_fact.pack(side=LEFT, expand=TRUE, fill=BOTH)


#  Buttons for Row 3: square root, open parentheses, close parentheses, modulo, divide

btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)

buttom_sqrt = Button(btnrow3, text=" √x ", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_sqrt, fg="white", bg="#333333")
buttom_sqrt.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_pOpen = Button(btnrow3, text="  (", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_pOpen, fg="white", bg="#333333")
button_pOpen.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_pClose = Button(btnrow3, text="  )", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_pClose, fg="white", bg="#333333")
button_pClose.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_modulo = Button(btnrow3, text="%", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_modulo, fg="white", bg="#333333")
button_modulo.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_divide = Button(btnrow3, text="÷", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_divide, fg="white", bg="#333333")
button_divide.pack(side=LEFT, expand=TRUE, fill=BOTH)


# Buttons for Row 4: sin-1, number7, number8, number9, multiply

btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)

buttom_asin = Button(btnrow4, text="sin−1", font="Arial 15", relief=RIDGE, bd=0, command=onPressed_asin, fg="white", bg="#333333")
buttom_asin.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_number7 = Button(btnrow4, text="7", font="Arial 17", relief=RIDGE, bd=0, command=onPressed7, fg="black", bg="#CFCFCF")
button_number7.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_number8 = Button(btnrow4, text="8", font="Arial 17", relief=RIDGE, bd=0, command=onPressed8, fg="black", bg="#CFCFCF")
button_number8.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_number9 = Button(btnrow4, text="9", font="Arial 17", relief=RIDGE, bd=0, command=onPressed9, fg="black", bg="#CFCFCF")
button_number9.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_multiply = Button(btnrow4, text="*", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_multiply, fg="white", bg="#333333")
button_multiply.pack(side=LEFT, expand=TRUE, fill=BOTH)


# Buttons for Row 5: cos-1, number4, number5, number6, minus

btnrow5 = Frame(root)
btnrow5.pack(expand=TRUE, fill=BOTH)

buttom_acosine = Button(btnrow5, text="cos-1", font="Arial 15", relief=RIDGE, bd=0, command=onPressed_acosine, fg="white", bg="#333333")
buttom_acosine.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_number4 = Button(btnrow5, text="4", font="Arial 17", relief=RIDGE, bd=0, command=onPressed4, fg="black", bg="#CFCFCF")
button_number4.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_number5 = Button(btnrow5, text="5", font="Arial 17", relief=RIDGE, bd=0, command=onPressed5, fg="black", bg="#CFCFCF")
button_number5.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_number6 = Button(btnrow5, text="6", font="Arial 17", relief=RIDGE, bd=0, command=onPressed6, fg="black", bg="#CFCFCF")
button_number6.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_minus = Button(btnrow5, text="-", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_minus, fg="white", bg="#333333")
button_minus.pack(side=LEFT, expand=TRUE, fill=BOTH)


# Buttons for Row 6: tan-1, number1, number2, number3, addition

btnrow6 = Frame(root)
btnrow6.pack(expand=TRUE, fill=BOTH)

buttom_atangent = Button(btnrow6, text="tan-1", font="Arial 16", relief=RIDGE, bd=0, command=onPressed_atangent, fg="white", bg="#333333")
buttom_atangent.pack(side=LEFT, expand=TRUE, fill=BOTH)

buttom_number1 = Button(btnrow6, text="1", font="Arial 17", relief=RIDGE, bd=0, command=onPressed1, fg="black", bg="#CFCFCF")
buttom_number1.pack(side=LEFT, expand=TRUE, fill=BOTH)

buttom_number2 = Button(btnrow6, text="2", font="Arial 17", relief=RIDGE, bd=0,  command=onPressed2, fg="black", bg="#CFCFCF")
buttom_number2.pack(side=LEFT, expand=TRUE, fill=BOTH)

buttom_number3 = Button(btnrow6, text="3", font="Arial 17", relief=RIDGE, bd=0, command=onPressed3, fg="black", bg="#CFCFCF")
buttom_number3.pack(side=LEFT, expand=TRUE, fill=BOTH)

buttom_plus = Button(btnrow6, text="+", font="Arial 16", relief=RIDGE, bd=0, command=onPressed_plus, fg="white", bg="#333333")
buttom_plus.pack(side=LEFT, expand=TRUE, fill=BOTH)


# Buttons for Row 7: power, roundoff, number0, decimal, equals

btnrow7 = Frame(root)
btnrow7.pack(expand=TRUE, fill=BOTH)

buttom_power = Button(btnrow7, text="  xⁿ", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_power, fg="white", bg="#333333")
buttom_power.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_roundoff = Button(btnrow7, text="  rnd", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_roundoff, fg="white", bg="#333333")
button_roundoff.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_number0 = Button(btnrow7, text="0", font="Arial 17", relief=RIDGE, bd=0, command=onPressed0, fg="black", bg="#CFCFCF")
button_number0.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_decimal = Button(btnrow7, text=" • ", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_decimal, fg="white", bg="#333333")
button_decimal.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_equals = Button(btnrow7, text="=", font="Arial 17", relief=RIDGE, bd=0, command=onPressed_equal, fg="white", bg="#333333")
button_equals.pack(side=LEFT, expand=TRUE, fill=BOTH)


#mainloop to run the tkinker window
root.mainloop()
