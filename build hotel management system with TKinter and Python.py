from tkinter import *
import time
from tkinter import ttk
####################### calculator function#########
def btn(numbers):
    global operator
    operator = operator + str(numbers)
    txt_input.set(operator)

def Clear():
    global operator
    operator= ''
    txt_input.set('')
    Display.insert(0,'Start Calculating...')

def Equal():
    global operator
    sumup= float(eval(operator))
    txt_input.set(sumup)
    operator = ''

########################## Total function##########
def TotalResult():
    varme1=Mealdicator.get()
    varme2=Meal.get()
    if(varme1=='Samosa'):
        varme3=(varme2*10)
        cost.set(varme3)
    elif(varme1 =='Kachori'):
        varme3=(varme2*10)
        cost.set(varme3)
    elif(varme1 =='Bread Cutlet'):
        varme3 = (varme2 * 15)
        cost.set(varme3)
    elif (varme1 =='Sandwich'):
        varme3 = (varme2 * 15)
        cost.set(varme3)
    elif (varme1 == 'Garlic Bread'):
        varme3 = (varme2 * 20)
        cost.set(varme3)
    else:
        varme3 = (varme2 * 0)
        cost.set(varme3)

    vardi1 = drinkdicator.get()
    vardi2 = drink.get()
    if (vardi1 == 'Fruit beer'):
        vardi3 = (vardi2 * 30)
        Drinks.set(vardi3)
    elif (vardi1 == 'Pepsi'):
        vardi3 = (vardi2 * 40)
        Drinks.set(vardi3)
    elif (vardi1 == 'Sprite'):
        vardi3 = (vardi2 * 30)
        Drinks.set(vardi3)
    elif (vardi1 == 'Mountain Dew'):
        vardi3 = (vardi2 * 35)
        Drinks.set(vardi3)
    elif (vardi1 == 'Coke'):
        vardi3 = (vardi2 * 40)
        Drinks.set(vardi3)
    else:
        vardi3 = (vardi2 * 0)
        Drinks.set(vardi3)

    num1 = float(cost.get())
    num2 = float(Drinks.get())
    delivery = (num1 +num2)

    if chkbl.get() ==1:
        Devcost.set(delivery + 20)
    else:
        Devcost.set(delivery)




    ################## total result ########
    num3 = (Devcost.get())

    Total.set(num3)
    FinalTotal =('{Total = ₹}',Total)

    num4= Total.get()
    Display.delete(0,END)
    Display.insert(0,FinalTotal)

    if(num4 <= '0.0'):
        Display.delete(0,END)
        Display.insert(0,'Please make a order')




















root=Tk()
root.geometry('1600x800+0+0')
root.title('Cantenn Management System')
########################## Window's  Partition###################################
Tops= Frame(root,width=1600,height=100,bg='blue',relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2= Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

f3 = Frame(root,width=35,height=700,relief=SUNKEN)
f3.pack(side=LEFT)

f4 = Frame(root,width=100,height=700,relief=SUNKEN)
f4.pack(side=LEFT)
################################### main screen ############################################
txt_input=StringVar(value='Snacks Corner')
Display = Entry(Tops, font=('arial',97,'bold'),fg='white',bd=50,bg='blue',
                justify='right',textvariable=txt_input)
Display.grid(columnspan=4)

################################## Time #######################
localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(f2,font=('arial',20,'bold'),text=localtime,fg='dark blue',bd=10,anchor=W)
lblInfo.grid(row=0,column=0,columnspan=4)

######################################### ROw 1 ##############################
operator=''

btn7 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='7',command=lambda :btn(7)).grid(row=1,column=0)
btn8 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='8',command=lambda :btn(8)).grid(row=1,column=1)
btn9 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='9',command=lambda :btn(9)).grid(row=1,column=2)
btnC = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='C',bg='green',command = Clear).grid(row=1,column=3)

######################################### ROw 2 ##############################
btn4 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='4',command=lambda :btn(4)).grid(row=2,column=0)
btn5 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='5',command=lambda :btn(5)).grid(row=2,column=1)
btn6 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='6',command=lambda :btn(6)).grid(row=2,column=2)
btnplus = Button(f2,padx=18,pady=5,bd=8,font=('arial',30,'bold'),text='+',bg='orange',command=lambda :btn('+')).grid(row=2,column=3)

######################################### ROw 3 ##############################
btn1 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='1',command=lambda :btn(1)).grid(row=3,column=0)
btn2 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='2',command=lambda :btn(2)).grid(row=3,column=1)
btn3 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='3',command=lambda :btn(3)).grid(row=3,column=2)
btnminus = Button(f2,padx=23,pady=5,bd=8,font=('arial',30,'bold'),text='-',bg='orange',command=lambda :btn('-')).grid(row=3,column=3)
######################################### ROw 4 #############################
btn0 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='0',command=lambda :btn(0)).grid(row=4,column=0)
btndot = Button(f2,padx=21,pady=5,bd=8,font=('arial',30,'bold'),text='.',bg='orange',command=lambda :btn('.')).grid(row=4,column=1)
btndivision = Button(f2,padx=20,pady=5,bd=8,font=('arial',30,'bold'),text='/',bg='orange',command=lambda :btn('/')).grid(row=4,column=2)
btnmultiply = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='x',bg='orange',command=lambda :btn('*')).grid(row=4,column=3)
######################################### ROw 5 ##############################
btnequals = Button(f2,padx=64,pady=2,bd=8,font=('arial',30,'bold'),text='=',bg='green',command=Equal).grid(row=5,column=0,columnspan=2)
btnopenbracket = Button(f2,padx=19,pady=2,bd=8,font=('arial',30,'bold'),text='(',bg='orange',command=lambda :btn('(')).grid(row=5,column=2)
btnclosebracket = Button(f2,padx=23,pady=2,bd=8,font=('arial',30,'bold'),text=')',bg='orange',command=lambda :btn(')')).grid(row=5,column=3 )

########################## Choose Meal ######################
Meal=IntVar()
Mealdicator=StringVar(value='Delecious Snacks')

lblMeal = Label(f1,font=('arial',16,'bold'),text='Choose meal',bd=10,anchor=W)
lblMeal.grid(row=0,column=0)
txtMeal = ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=Mealdicator)
txtMeal['value']=('Samosa','Kachori','Bread Cutlet','Sandwich','Garlic Bread')
txtMeal.grid( row=0,column=1)

lblQtoMeal=Label(f1,font=('arial',16,'bold'),text='Qty. of Meal',bd=10,anchor=W)
lblMeal.grid( row=1,column=0)
txtQtoMeal= Entry(f1,font=('arial',16,'bold'),textvariable=Meal,insertwidth=4,bg='white',justify='right')
txtQtoMeal.grid(row=1,column=1)

######################### choose drink #################################
drink=IntVar()
drinkdicator=StringVar(value='Fresh Drinks')

lbldrink = Label(f1,font=('arial',16,'bold'),text='Choose Drinks',bd=10,anchor=W)
lbldrink.grid(row=2,column=0)
txtdrink = ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=drinkdicator)
txtdrink['value']=('Fruit beer','Pepsi','Sprite','Mountain Dew','Coke')
txtdrink.grid( row=2,column=1)

lblQtodrink = Label(f1,font=('arial',16,'bold'),text='Qty. of drink',bd=10,anchor=W)
lbldrink.grid(row=3,column=0)
txtQtodrink = Entry(f1,font=('arial',16,'bold'),textvariable=drink,insertwidth=4,bg='white',justify='right')
txtQtodrink.grid(row=3,column=1)

######################################order delivery ###################
chkbl=IntVar()

lblHomeDev =Label(f1,font=('arial',16,'bold'),text='Order Online',bd=10,anchor=W)
lblHomeDev.grid(row=4,column=0)
check1 = Checkbutton(f1,text='Yes',variable=chkbl,font=('arial',16,'bold'))
check1.grid(row=4,column=1)

######################### Cost Display Screen ######################
cost= StringVar()
lblMeal = Label(f1, font=('arial',16,'bold'),text='Cost of Snacks(₹)',bd=16,anchor=W)
lblMeal.grid(row=0,column=2)
txtMeal = Entry(f1,font=('arial',16,'bold'),textvariable=cost,fg='white',bd=10,insertwidth=4,bg='blue',justify='right')
txtMeal.grid(row=0,column=3)

Drinks= StringVar()
lbldrink = Label(f1, font=('arial',16,'bold'),text='Cost of Drinks(₹)',bd=16,anchor=W)
lbldrink.grid(row=1,column=2)

txtdrink = Entry(f1,font=('arial',16,'bold'),textvariable=cost,fg='white',bd=10,insertwidth=4,bg='blue',justify='right')
txtdrink.grid(row=1,column=3)

Devcost = StringVar()
lblHomeDev =Label(f1, font=('arial',16,'bold'),text='Delivery Charges(₹)',bd=16,anchor=W)
lblHomeDev.grid(row=2,column=2)
txtHomeDev = Entry(f1,font=('arial',16,'bold'),textvariable=Devcost,fg='white',bd=10,insertwidth=4,bg='blue',justify='right')
txtHomeDev.grid(row=2,column=3)

Total = StringVar()
lbltotal =Label(f1, font=('arial',16,'bold'),text='Total (₹)',bd=16,anchor=W)
lbltotal.grid(row=4,column=2)
txttotal = Entry(f1,font=('arial',16,'bold'),textvariable=Total,fg='white',bd=10,insertwidth=4,bg='blue',justify='right')
txttotal.grid(row=4,column=3)

##################################  Control Buttons ########################
btnTotal = Button(f4,padx=10,pady=8,bd=16,fg='white',font=('arial',16,'bold'),width=8,text='Total',bg='orange',command= TotalResult)
btnTotal.grid(row=0,column=0)

btnScreen = Button(f4,padx=10,pady=8,bd=16,fg='white',font=('arial',16,'bold'),width=8,text='Clear',bg='blue')
btnScreen.grid(row=1,column=0)

btnReset = Button(f4,padx=10,pady=8,bd=16,fg='white',font=('arial',16,'bold'),width=8,text='Reset',bg='green')
btnReset.grid(row=2,column=0)

btnExit = Button(f4,padx=10,pady=8,bd=16,fg='white',font=('arial',16,'bold'),width=8,text='Exit',bg='red')
btnExit.grid(row=3,column=0)


root.mainloop()





















