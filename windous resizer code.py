from tkinter import *
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter import messagebox as tkmsg

#######  window resizer funcion
if __name__=="__main__":
    def Window_size(width,height):
        root.geometry(f"{width}x{height}")
        root.minsize(width,height)
        root.maxsize(width,height)

root = ttkb.Window(themename="superhero") 

####### app function

if __name__=="__main__":
    def set_size():
        try:
                Height = int(height_var.get())
                Width = int(width_var.get())
                if Height == None or Width == None:
                        tkmsg.showerror("error","fill the field")
                else:
                        root.geometry(f"{Width}x{Height}")
                        root.minsize(Width,Height)
                        root.maxsize(Width,Height)  
        except:
                tkmsg.showerror("error","fill the field")
        #### label display

        Display = Display_var_lab.get()
        Display_var_lab.set(f"{Width}X{Height}")     
        
if __name__=="__main__":
   def reset_size():
        root.geometry(f"{490}x{300}")
        root.minsize(490,300)
        root.maxsize(490,300)   
        Display = Display_var_lab.get()                  
        Display_var_lab.set("490X300")


######  menubar functions


######  app title

title_app = ttkb.Label(
        master=root,
        text="Window Resizer",
        font=("ds-digital",22),
        bootstyle='success'
)
title_app.pack(side=TOP,pady=5)

#########  frame 1 height and width

Frame_1 = ttkb.Frame(root)
Frame_1.pack(side=TOP,pady=3)

### labels


Width_label = ttkb.Label(
        master=Frame_1,text="Width",
        font=("ds-digital",18),
        foreground="#e94822"
        )

Height_label = ttkb.Label(
        master=Frame_1,text="Heigth",
        font=("ds-digital",18),
        foreground="#e94822"
        )

Width_label.grid(row=0,pady=3,column=0,sticky=W)
Height_label.grid(row=1,column=0,sticky=W)

###  variables

width_var = IntVar()
height_var = IntVar()

width_var.set(490)
height_var.set(300)

#######  entry box

Width_box = ttkb.Entry(
    Frame_1,
    width=20,
    font=("ds-digital",18),
    bootstyle = "danger",
    textvariable=width_var
          )
height_box = ttkb.Entry(
    Frame_1,
    width=20,
    font=("ds-digital",18),
    bootstyle = "danger",
    textvariable=height_var
          )
Width_box.grid(row=0,pady=3,column=1)
height_box.grid(row=1,pady=3,column=1)


####  display label

Display_var_lab = StringVar()

Display_label = ttkb.Label(
        master=root,
        textvariable=Display_var_lab,
        font=("arial",16),
        bootstyle='warning'
)

Display_label.pack(side=TOP,pady=6)
#########  button frame 

Frame_2 = ttkb.Frame(master=root)
Frame_2.pack(side=TOP,pady=6)

#######  button

btn_style = ttkb.Style()
btn_style.configure('success.TButton',font=("ds-digital",14))

btn_set = ttkb.Button(master=Frame_2,
                      text="Reset Size",
                      command=reset_size,
                      width=12,style="success.TButton"
                      )

btn_set.grid(row=0,padx=3,column=0)

btn_reset_set = ttkb.Button(master=Frame_2,
                      text="Set Size",
                      command=set_size,
                      width=12,style="success.TButton"
                      )

btn_reset_set.grid(row=0,column=1,padx=3)


root.title("window resizer")
Window_size(490,300)
root.mainloop()