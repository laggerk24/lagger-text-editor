import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('LOOP GUI')

labels = ['name','age','sex','country','state','city']
for i in range(len(labels)):
    lablevariable = 'lable'+str(i)
    lablevariable = ttk.Label(win,text=labels[i])
    lablevariable.grid(row=i,column=0,sticky=tk.W,padx=40,pady=10)

data = {
    'name':tk.StringVar(),
    'age':tk.StringVar(),
    'sex':tk.StringVar(),
    'country':tk.StringVar(),
    'state':tk.StringVar(),
    'city':tk.StringVar()
}
add = 0
for key in data:
    print(key)
    entrybox = ttk.Entry(win,width=16,textvariable=data[key])
    entrybox.grid(row=add,column=1,padx=40,pady=10)
    add +=1

def submit():
    for k,p in data.items():
        print(f'{k} : {data.get(k).get()}')
submit_bottn = ttk.Button(win,text='submit',command=submit)
submit_bottn.grid(row=add+1,column =0)
win.mainloop()