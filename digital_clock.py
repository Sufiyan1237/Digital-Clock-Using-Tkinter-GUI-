import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)  # update every 1 second

# Create the GUI window
root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=("Helvetica", 48), fg="green", bg="black")
label.pack(padx=20, pady=20)

update_time()  # initial call
root.mainloop()
