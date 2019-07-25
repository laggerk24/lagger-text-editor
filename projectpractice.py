import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg,font,colorchooser,filedialog,commondialog
import os
def func():
    print('yoyo')
#MENU BAR________________________________________________________

win = tk.Tk()
win.title('LAGGER\'S TEXT EDITOR')
mainmenu = tk.Menu(win)
win.geometry('1290x720')
filemenu=tk.Menu(mainmenu)
###var declaration
theme_var = tk.StringVar()


##menu declaration
filemenu = tk.Menu(mainmenu,tearoff=False)
editmenu = tk.Menu(mainmenu,tearoff=False)
viewmenu = tk.Menu(mainmenu,tearoff=False)
helpmenu = tk.Menu(mainmenu,tearoff=False)
thememenu =tk.Menu(mainmenu,tearoff=False)

#menu cascade
mainmenu.add_cascade(label='File',menu=filemenu)
mainmenu.add_cascade(label='Edit',menu=editmenu)
mainmenu.add_cascade(label='View',menu=viewmenu)
mainmenu.add_cascade(label='Theme',menu=thememenu)
mainmenu.add_cascade(label='Help',menu=helpmenu)
win.config(menu=mainmenu)

#############################BodY###############################################


###############TOOOL BAR ####################################
##file icon declaration
new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
saveas_icon = tk.PhotoImage(file='icons2/save.png')
save_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')


##edit icon declaration
copy_icon = tk.PhotoImage(file='icons2/copy.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
find_icon = tk.PhotoImage(file='icons2/find.png')
##view icon declaration
tool_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_icon = tk.PhotoImage(file='icons2/status_bar.png')
##theme icon
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
icon =(light_default_icon,light_plus_icon,monokai_icon,night_blue_icon,red_icon,dark_icon)
##tool bar 
###########fonts######
toolbar_label = ttk.Label(win)
toolbar_label.pack(fill=tk.X,side=tk.TOP)
font_list = tk.font.families()
font_var = tk.StringVar()
font_box = ttk.Combobox(toolbar_label,width=20,textvariable = font_var,state='readonly')
font_box['values'] = font_list
font_box.current(font_list.index('Lato'))
font_box.grid(row=0,column=0,padx=5)
#######size#########
size_var = tk.IntVar()
size_box = ttk.Combobox(toolbar_label,width = 15,textvariable =size_var,state= 'readonly')
size_box['values'] = list(range(8,81))
size_box.current(4)
size_box.grid(row=0,column =1,padx =5)

####BOLD<ITALICS<ALLIGNMENT
##bold
bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(toolbar_label,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)
##italic
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(toolbar_label,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)
##underline
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(toolbar_label,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)
#font color
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_btn = ttk.Button(toolbar_label,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)
#allign left right center
align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
align_right_icon = tk.PhotoImage(file='icons2/align_right.png')

align_left_btn = ttk.Button(toolbar_label,image=align_left_icon)
align_center_btn = ttk.Button(toolbar_label,image=align_center_icon)
align_right_btn = ttk.Button(toolbar_label,image=align_right_icon)

align_left_btn.grid(row=0,column=6,padx=5)
align_center_btn.grid(row=0,column=7,padx=5)
align_right_btn.grid(row=0,column=8,padx=5)
#-----------------------------------------------------------------------tool bar ending----------------
##text editor-----------------------------------------#####################
text = tk.Text(win)
text.config(wrap='word',relief=tk.FLAT)
scroll = tk.Scrollbar(win)
scroll.pack(side=tk.RIGHT,fill=tk.Y)
text.pack(fill=tk.BOTH,expand=True)
text.focus_set()
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
#_________________---------------------------text editor ending------------------------------------------------

#font binding----------
current_text_font = 'Lato'
current_text_fontsize = 12

def change_font(event=None):
    global current_text_font 
    current_text_font = font_var.get()
    text.configure(font=(current_text_font,current_text_fontsize))
def change_fontsize(win):
    global current_text_fontsize
    current_text_fontsize = size_var.get()
    text.configure(font=(current_text_font,current_text_fontsize))
font_box.bind('<<ComboboxSelected>>',change_font)
size_box.bind('<<ComboboxSelected>>',change_fontsize)
######---------------buttons functionality--------------------------------------------------------
##---bold----

def bold_text():
    text_property = tk.font.Font(font=text['font'])
    if text_property.actual()['weight'] == 'normal':
        text.configure(font=(current_text_font,current_text_fontsize,'bold'))
    if text_property.actual()['weight'] == 'bold':
        text.configure(font=(current_text_font,current_text_fontsize,'normal'))
bold_btn.configure(command=bold_text)
#-----------------italic------------------   
def italic_text():
    text_property = tk.font.Font(font=text['font'])
    if text_property.actual()['slant'] == 'roman':
        text.configure(font=(current_text_font,current_text_fontsize,'italic'))
    if text_property.actual()['slant'] == 'italic':
        text.configure(font=(current_text_font,current_text_fontsize,'roman'))
#---------------underline------------------
def underline_text():
    text_property = tk.font.Font(font=text['font'])
    if text_property.actual()['underline'] == 0:
        text.configure(font=(current_text_font,current_text_fontsize,'underline'))
    if text_property.actual()['underline'] == 1:
        text.configure(font=(current_text_font,current_text_fontsize,'normal'))


bold_btn.configure(command=bold_text)
italic_btn.configure(command=italic_text)
underline_btn.configure(command=underline_text)
#------------change font color functionality-------------------------
###------left alignment-------
def left_align():
    text_content = text.get(1.0,'end')
    text.tag_config('left',justify=tk.LEFT)
    text.delete(1.0,'end')
    text.insert(tk.INSERT,text_content,'left')
align_left_btn.configure(command=left_align)
###-------right-alignment-------
def right_align():
    text_content = text.get(1.0,'end')
    text.tag_config('right',justify=tk.RIGHT)
    text.delete(1.0,'end')
    text.insert(tk.INSERT,text_content,'right')
align_right_btn.configure(command=right_align)

###-------center-alignment--------
def center_align():
    text_content = text.get(1.0,'end')
    text.tag_config('center',justify=tk.CENTER)
    text.delete(1.0,'end')
    text.insert(tk.INSERT,text_content,'center')
align_center_btn.configure(command=center_align)
###------color---configure----------
def colorchanger():
    color_var = tk.colorchooser.askcolor()
    text.configure(foreground=color_var[1])

font_color_btn.configure(command=colorchanger)



text.configure(font=('Lato',12))
###########---------------------------------buttons functionality end----------------------------------------------------------------------

###-----------------status bar-----------
statusbar_label = ttk.Label(win,text='Status Bar')
statusbar_label.pack(side=tk.BOTTOM)
text_changed = False
def changed(win):
    global text_changed
    if text.edit_modified():
        text_changed = True
        words = len(text.get(1.0,'end-1c').split())
        characters = len(text.get(1.0,'end-1c'))
        statusbar_label.configure(text=f'words = {words}  characters = {characters}')
        text.edit_modified(False)
text.bind('<<Modified>>',changed)


#___________________status bar ending___________
url = ''

##file menu ----------------------------------------------------
#new command
def new_file(event=None):
    global url
    url = ''
    text.delete(1.0,'end')
filemenu.add_command(label='New File',accelerator='Ctrl+N',image=new_icon,compound=tk.LEFT,command=new_file)
#Open command
def Open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text file','*.txt'),('All Files','*.*')))
    try:
        with open(url, 'r') as fr:
            text.delete(1.0,tk.END)
            text.insert(1.0,fr.read())
    except FileNotFoundError:
        print('file not found ')
    except:
        print('unexpected')
    win.title(os.path.basename(url))
filemenu.add_command(label='Open...',accelerator='Ctrl+O',image=open_icon,compound=tk.LEFT,command=Open_file)
##Save command
print(url)
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
               fw.write(content)
               fw.close()
        else:
            url = filedialog.asksaveasfilename(mode='r+',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
            content2 = text.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return
filemenu.add_command(label='Save',accelerator='Ctrl+S',image=save_icon,compound=tk.LEFT,command=save_file)

def save_as_file(event=None):
    global url
    try:
        print(url)
        url = filedialog.asksaveasfilename(mode='w',defaultextension='.txt',filetypes=(('Text Files','*.txt'),('All Files','*.*')))
        content = text.get(1.0,tk.END)
        url.write(content)
        url.close()
    except:
        return
filemenu.add_command(label='Save As',accelerator='Ctrl+Alt+S',image=saveas_icon,compound=tk.LEFT,command=save_as_file)
filemenu.add_separator()
filemenu.add_command(label='Exit',accelerator='Ctrl+Q',image=exit_icon,compound=tk.LEFT)


##edit menu
editmenu.add_command(label='Cut',accelerator="Ctrl+X",image=cut_icon,compound=tk.LEFT)
editmenu.add_command(label='Copy',accelerator="Ctrl+C",image=copy_icon,compound=tk.LEFT)
editmenu.add_command(label='Paste',accelerator="Ctrl+V",image=paste_icon,compound=tk.LEFT)
editmenu.add_separator()
editmenu.add_command(label='Find',accelerator="Ctrl+F",image=find_icon,compound=tk.LEFT)

##view menu
viewmenu.add_checkbutton(label='Tool Bar',image=tool_icon,compound=tk.LEFT)
viewmenu.add_checkbutton(label='Status bar',image=status_icon,compound=tk.LEFT)

##help menu
helpmenu.add_command(label='View Help',command=func)
helpmenu.add_command(label='Send Feedback')
helpmenu.add_separator()
helpmenu.add_command(label='Lagger',command=func)

##theme menu
theme = {
    'Light(default)':('#000000','#ffffff'),
    'Light PLus':('#474747','#e0e0e0'),
    'Monokai':('#d3b774','#474747'),
    'Night Blue':('#ededed','#6b9dc2'),
    'Red':('#2d2d2d','ffe8e8#'),
    'Dark':('#c4c4c4','#2d2d2d')
}
count = 0
for i in theme:
    thememenu.add_radiobutton(label=i,image=icon[count],compound=tk.LEFT,variable=theme_var)
    count +=1
#################################DEFINATIONS CLOSED#################



win.mainloop()
