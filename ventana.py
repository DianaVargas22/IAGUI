
from tkinter import filedialog 
from tkinter import *

ventana = Tk()
ventana.geometry('500x400')
ventana.title("Proyecto")
ventana.resizable(0, 0)


def browseFiles(): 
    filename = filedialog.askopenfilename(
       initialdir = "/", 
      title = "Select a File", 
      filetypes = (("Text files", 
         "*.txt*"), 
         ("all files", 
         "*.*")))    
    print(filename)


#Variables
param_data = StringVar()
button_explore = Button(ventana,  
                        text = "Browse Files", 
                        command = browseFiles) 
add_name_label = Label(ventana, text="Parametro")
add_name_entry = Entry(ventana, textvariable=param_data)

boton = Button(ventana, text="Entrenar")


       

def home():
   home_label = Label(ventana, text="Predice la bolsa ")
   home_label.config(
      fg="white",
      bg="black",
      font=("Arial", 15),
      padx=200,
      pady=20
   )
   home_label.grid(row=0, column=0, columnspan=3)

   button_explore.grid(row=1, column=0, sticky=NW)
   button_explore.config(
      padx=20,
      pady=5,
      bg="green",
      fg="white"
   )

   add_name_label.grid(row= 2, column=0, padx=5, pady=5, sticky=NW)
   add_name_entry.grid(row= 2, column=1, padx=5, pady=5, sticky=NW)

   boton.grid(row=3, column=1, sticky=NW)
   boton.config(
      padx=15,
      pady=5,
      bg="green",
      fg="white"
   )

   
   return True

home()

ventana.mainloop()
