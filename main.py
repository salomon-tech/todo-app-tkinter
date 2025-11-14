from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.config(bg="#0b0f16")
root.title("Todo app")
root.geometry("800x500")
root.resizable(False, False)

#functions

#a empty list for tasks
tasks = []

#fuction to add task
def add_task():
    task = input_form.get()
    if task != "":
        task_display.insert(tk.END, task)
        input_form.delete(0, tk.END)
    
    else:
        messagebox.showwarning("to add task you need to create that !")

#function to delete task
def delete_task():
    try:
        index = task_display.curselection()[0]
        task_display.delete(index)
    except:
        messagebox.showwarning("you need to select task before deleting it !")

#edit task
def edit_task():
    try:
        index = task_display.curselection()[0]
        new_task = input_form.get()
        task_display.delete(index)
        task_display.insert(index, new_task)
    except:
        messagebox.showwarning("you need to select task before editing it !")

#load_tasks_to_edit
def load_task_to_edit():
    try:
        index = task_display.curselection()[0]
        selected_task = task_display.get(index)
        input_form.delete(0, tk.END)
        input_form.insert(0, selected_task)
    except:
        messagebox.showwarning("you need to select task before loading it ! ")


#export task to txt file
def export_task():
    with open("task.txt", "w", encoding="utf-8") as file:
        tasks = task_display.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("your file has been success exported ! ")


#import task from txt file
def import_task():
    try:
        with open("task.txt", "r", encoding="utf-8") as file:
            for line in file:
                task_display.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass


#design
app_title = tk.Label(root, text="Todo Tkinter", font=(("Areal", 30, "bold")), width=50, fg="#727451", bg="#0b0f16")
app_title.pack(padx=10)

input_form = tk.Entry(root, width=45, font=(("Areal", 18)), bd=2)
input_form.place(x= 10, y=120)

add_task_button = tk.Button(root, text="add", font=(("Areal", 12)), width=18, bg="#4344ff", bd=3, command=add_task)
add_task_button.place(x = 620, y=121)

add_task_button = tk.Button(root, text="edit", font=(("Areal", 12)), width=8, bg="#4344ff", bd=3, command=edit_task)
add_task_button.place(x = 620, y=180)

add_task_button = tk.Button(root, text="load to edit", font=(("Areal", 12)), width=8, bg="#4344ff", bd=3, command=load_task_to_edit)
add_task_button.place(x = 710, y=180)

add_task_button = tk.Button(root, text="delete", font=(("Areal", 12)), width=18, bg="#4344ff", bd=3, command=delete_task)
add_task_button.place(x = 620, y=230)

add_task_button = tk.Button(root, text="export to txt", font=(("Areal", 12)), width=18, bg="#4344ff", bd=3, command=export_task)
add_task_button.place(x = 620, y=280)

add_task_button = tk.Button(root, text="import from txt", font=(("Areal", 12)), width=18, bg="#4344ff", bd=3, command=import_task)
add_task_button.place(x = 620, y=330)

add_task_button = tk.Button(root, text="exit", font=(("Areal", 12)), width=18, bg="#4344ff", bd=3, command=exit)
add_task_button.place(x = 620, y=450)

task_display = tk.Listbox(root, font=(("Areal", 18)), width=45, height=11)
task_display.place(x= 10, y = 180)


root.mainloop()