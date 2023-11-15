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
        x1 = self.width / 4
        x2 = 3*x1

        y1 = self.height / 4
        y2 = 3*y1
        self.canvas.create_line(x1, y1, x2, y1, x2, y2, x1, y2, x1, y1, fill='blue')


class Triangle(Drawing):
    def __init__(self, width, height):
        super().__init__(width, height)

    def draw(self):

        triangle_height = self.height * 0.8
        half_triangle_width = triangle_height / math.sqrt(3)

        x1 = self.width/2
        y1 = (self.height - triangle_height) / 2.0

        x2 = x1 - half_triangle_width
        y2 = y1 + triangle_height

        x3 = x1 + half_triangle_width
        y3 = y1 + triangle_height

        self.canvas.create_line(x1, y1, x2, y2, x3, y3, x1, y1, fill='red')


if __name__ == '__main__':
    Square(800,800)
    Triangle(800, 800)
