from tkinter import *
import random

root=Tk()

root.title("Random country")
root.geometry("500x500")
root.configure(background = 'lavender')

enterco = Entry(root)
enterco.place(relx=0.5,rely=0.2,anchor=CENTER)
enterci = Entry(root)
enterci.place(relx=0.5,rely=0.3,anchor=CENTER)

country_list=Label(root)
city_list=Label(root)
rco = Label(root)
rci = Label(root)

list1 = []
list2 = []
def addthatboi():
    enteredco = enterco.get()
    list1.append(enteredco)
    country_list['text'] = "Your country list : " + str(list1)
    enteredci = enterci.get()
    list2.append(enteredci)
    city_list['text'] = "Your city list : " + str(list2)
    
def randnumber():
    length1 = len(list1)
    length2 = len(list2)
    random_no1 = random.randint(0, length1-1)
    rco['text'] = str(random_no1)
    generated_random_number = list1[random_no1]
    rco['text'] = "Country : " + str(generated_random_number) + ", totally not scuffed."
    random_no2 = random.randint(0, length2-1)
    rci['text'] = str(random_no2)
    generated_random_number2 = list2[random_no2]
    rci['text'] = "City : " + str(generated_random_number2) + ", totally not scuffed."

btn = Button(root, text="Add the country and city to the list", command=addthatboi)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

rco.place(relx=0.5,rely=0.8,anchor=CENTER)
rci.place(relx=0.5,rely=0.9,anchor=CENTER)
country_list.place(relx=0.5,rely=0.5,anchor = CENTER)
city_list.place(relx=0.5,rely=0.6,anchor=CENTER)

btn1=Button(root,text='Show random city name and country name',command=randnumber)
btn1.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()

#this code is totoally not scuffed and totally not copied off of byju's future school