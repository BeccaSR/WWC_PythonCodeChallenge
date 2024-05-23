# Day 53 Challenge:
# Create a program that allows users to draw on a canvas using a GUI.

# import Tkinter library for GUI building
import tkinter as tk

# create the main window
window = tk.Tk()
window.geometry('600x400')
window.title('Let\'s Draw!')

# create the canvas
canvas = tk.Canvas(window, bg='white')
canvas.pack()

# drawing on the canvas
def draw(event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        canvas.create_oval(x1, y1, x2, y2, fill="black", width=2)

# clearing the canvas
def clear_canvas(canvas):
    '''
    This function takes to canvas object as an argument.
    It uses the 'delete' method to remove all drawn lines from the canvas.
    '''
    canvas.delete('all')

# bind mouse button press and release events to the functions
canvas.bind('<B1-Motion>', lambda event: draw(event))

# create 'Draw Away!' label widget, and 'Clear Canvas' button widget
label = tk.Label(window, text='Draw Away!')
label.pack(padx=10, pady=10)
button = tk.Button(window, text='Clear Canvas', command=lambda: clear_canvas(canvas))
button.pack(padx=10, pady=10)

# start the Tkinter event loop
window.mainloop()