import tkinter as tk


window = tk.Tk()

width = 800
height = 800

canvas = tk.Canvas(window,  width=width, height=height, background='white')

border = 50

canvas.create_line(border, border, width-border, height-border)
canvas.create_line(border, height-border, width-border,border)

canvas.pack()

window.mainloop()
