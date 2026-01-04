import tkinter as tk 

#main window
root = tk.Tk()  
root.title("To-Do List") 
root.geometry("500x600") 

#Label Widget

title_label = tk.Label(root, text = "To-Do List App", font = ("Pacifico", 30, "bold"))
title_label.pack(pady=20) 

#Entry Widget 
to_do_list_entry = tk.Entry(root, font = ("Helvetica", 20), width = 30) 
to_do_list_entry.pack(pady = 40) 

#Function for Addding tasks 

def add_task():
    task = to_do_list_entry.get() 
    if task:
        print(f"Task Added:{task}")
        to_do_list_box.insert(tk.END, task)
    else:
        print("Enter a task!")  

#Button Widgets
add_task_button= tk.Button (root, text = "Add Task", font = ("Helvetica", 20), command = add_task)

#Packing the button    
add_task_button.pack(pady = 40)

#Listbox 
to_do_list_box = tk.Listbox( 
    root, 
    font = ("Helvetica", 20),
    width = 50,
    height = 100,
    bg = "pink"
)

#Packing the Listbox 
to_do_list_box.pack(
    pady = 20
)

#Running the application
root.mainloop()