from tkinter import *

#function to add values to the listbox
def add_values():
    my_list_box.insert("end",entry_widget.get())
    entry_widget.delete(0,"end")
#function to delete values
def delete_values():
    my_list_box.delete(ANCHOR)

root = Tk()
root.title("my todo list app")
root.geometry("400x450")
root.config(bg="lightgreen")

#mainframe 
main_frame = Frame(root,bg="lightgreen",bd=0)
main_frame.pack(fill="both")

#listbox
my_list_box = Listbox(main_frame,bg="lightblue",font=("Chiller Regular",20,"bold"),bd=0,highlightthickness=0,height=7,width=24,
                      selectbackground="lightgrey")
my_list_box.pack(side="left")

#entry frame
entry_frame = Frame(root,bg="lightgreen",bd=0)
entry_frame.pack(fill="both")

#entry widget
entry_widget = Entry(entry_frame,font=("Castellar Regular",20,"bold"),bd=0,bg="orange",width=24)
entry_widget.pack(side="left")

#button frame 
button_frame = Frame(root,bd=0,bg="lightgreen")
button_frame.pack(fill="both")

#buttons
add_button = Button(button_frame,text="ADD",bg="darkgreen",font=("Forte Regular",20,"bold"),command=lambda:add_values())
add_button.grid(row=0,column=0)

delete_button = Button(button_frame,text="DELETE",bg="red",font=("Forte Regular",20,"bold"),command=lambda:delete_values())
delete_button.grid(row=0,column=1,padx=30)

#scrollbar
my_scrollbar = Scrollbar(main_frame)
my_scrollbar.pack(side="right",fill="y")
my_list_box.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list_box.yview)




root.mainloop()

