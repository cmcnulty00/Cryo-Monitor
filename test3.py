import tkinter as tk
from tkinter import * 

root = tk.Tk()
root.geometry("400x400")  # Size of the window 
root.title("Larpix Monitor")  # Adding a title

t1,t2=0,0

def add_temps():

	# Define Function to print the input value
	def display_input():

		channel_1 = var1.get()
		channel_2 = var2.get()
		print("\n\nInput for Sensor 1:", channel_1)
		print("Input for Sensor 2:", channel_2)

	# child window 
	child=Toplevel(root) # Child window 
	child.geometry("200x200")  # Size of the window 
	child.title("Temperature")

	# Define empty variables
	var1 = IntVar()
	var2 = IntVar()

	# Define a Checkbox
	t1 = Checkbutton(child, text="Sensor 1", variable=var1, onvalue=1, offvalue=0, command=display_input)
	t1.grid(column=0, row=1)
	t2 = Checkbutton(child, text="Sensor 2", variable=var2, onvalue=1, offvalue=0, command=display_input)
	t2.grid(column=0, row=2)

	done_button = tk.Button(child, text = "Done", command=lambda:child.destroy())
	done_button.grid(column=0, row=4)

t_button = tk.Button(root, text = "Add Extra Temperature Sensors", command=lambda:add_temps())
t_button.grid(column=0, row=0)

quit_button = tk.Button(root, text = "Quit", command=root.destroy)
quit_button.grid(column=0, row=3)

#b3 = tk.Button(root, text=' Close Child',
#                   command=root.destroy)
#b3.grid(row=3,column=2)


root.mainloop()
