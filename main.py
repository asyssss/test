from tkinter import *
from tkinter import messagebox
import random

HEIGHT = 600
WIDTH = 600

tasks = []

root = Tk()
root.title('To-do List')
root.geometry('%dx%d' % (WIDTH, HEIGHT))
root.resizable(False, False)

img = PhotoImage(file='todo_bg.gif')
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

root.option_add('*Font', '{Comic Sans MS} 10')
root.option_add('*Background', 'white')

frame = Frame(root, bd=10)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label_title = Label(frame, text='My Super To-do List', fg='blue', font='{Comic Sans MS} 16')
label_title.place(relx=0.3)

label_display = Label(frame, text='')
label_display.place(relx=0.3, rely=0.1)

text_input = Entry(frame, width=15)
text_input.place(relx=0.3, rely=0.15, relwidth=0.6)

button_add_task = Button(frame, text='Add task', command=add_task)
button_add_task.place(rely=0.15, relwidth=0.25)

button_del = Button(frame, text='Delete', command=del_one)
button_del.place(rely=0.25, relwidth=0.25)

button_del_all = Button(frame, text='Delete All', command=del_all)
button_del_all.place(rely=0.35, relwidth=0.25)

button_sort_asc = Button(frame, text='Sort(A-Y)', command=sort_asc)
button_sort_asc.place(rely=0.45, relwidth=0.25)

button_sort_desc = Button(frame, text='Sort(Y-A)', command=sort_desc)
button_sort_desc.place(rely=0.55, relwidth=0.25)

button_random = Button(frame, text=' Choose Random', command=choose_random)
button_random.place(rely=0.65, relwidth=0.25)

button_number_of_tasks = Button(frame, text=' Number of tasks', command=show_number_of_tasks)
button_number_of_tasks.place(rely=0.75, relwidth=0.25)

button_exit = Button(frame, text=' Exit', command=exit)
button_exit.place(rely=0.85, relwidth=0.25)

