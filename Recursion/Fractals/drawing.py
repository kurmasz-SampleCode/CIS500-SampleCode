import tkinter as tk

class Drawing:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        window = tk.Tk()
        self.canvas = tk.Canvas(window, height=width, width=height, bg="white")
        self.draw()
        self.canvas.pack()
        window.mainloop()


class Square(Drawing):
    def __init__(self, width, height):
        super().__init__(width, height)

    def draw(self):
        self.canvas.create_line(self.width/ 4,self.height/4, 3*self.width/4, self.height /4, 3*self.width/4, 3*self.height/4, self.width / 4, 3*self.height /4, self.width/4, self.height /4)

if __name__ == '__main__':
    Square(800,800)
