import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win = tk.Tk()
win.title('yo')


name_label = ttk.Label(win,text='enter your name - ')
name_label.grid(row = 0,column = 0,sticky=tk.W)
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win,width = 16,textvariable = name_var)
name_entrybox.grid(row = 0,column = 1)
name_entrybox.focus()
email_label = ttk.Label(win,text='enter your email id - ')
email_label.grid(row = 1,column=0,sticky=tk.W)
email_var  = tk.StringVar()
email_entrybox = ttk.Entry(win,width = 16,textvariable = email_var)
email_entrybox.grid(row = 1,column = 1)

age_lable = ttk.Label(win,text='enter your age - ')
age_lable.grid(row = 2,column = 0,sticky=tk.W)
age_var = tk.IntVar()
age_entrybox = ttk.Entry(win,width = 16,textvariable = age_var)
age_entrybox.grid(row=2, column = 1)

gender_lable = ttk.Label(win,text='whats your gender - ')
gender_lable.grid(row=3,column=0,sticky=tk.W)
gender_var = tk.StringVar()
gender_box = ttk.Combobox(win,textvariable = gender_var,state='readonly')
gender_box['values'] = ('male','female','others')
gender_box.current(0)
gender_box.grid(row= 3 ,column=1)

bottn_var = tk.StringVar()
bottn1 = ttk.Radiobutton(win,text='student',value='student',variable=bottn_var)
bottn1.grid(row=4 ,column=1)
bottn2 = ttk.Radiobutton(win,text='teacher',value='teacher',variable=bottn_var)
bottn2.grid(row=4,column=0)

checkbox = tk.IntVar()
cbox = ttk.Checkbutton(win,text='would you like to become the hero',variable=checkbox)
cbox.grid(row=5,columnspan=3)

def action() :
    name = name_var.get()
    email = email_var.get()
    age = age_var.get()
    gender = gender_var.get()
    ocupation = bottn_var.get()
    if checkbox.get()==1:
        hero = 'yes'
    else:
        hero ='no'
    with open('file.csv','a',newline='') as f:
        csvwriter = DictWriter(f,fieldnames=['name','email','age','gender','occupation','hero'])
        if os.stat('file.csv').st_size ==0:
            csvwriter.writeheader()
        csvwriter.writerow(
            {
                'name':name,
                'email':email,
                'age':age,
                'gender':gender,
                'occupation':ocupation,
                'hero':hero
            }
        )
    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    name_label.configure(foreground='red')
    



bottn_bottn = ttk.Button(win,text='submit',command=action)
bottn_bottn.grid(row=6,column=0)



win.mainloop()

