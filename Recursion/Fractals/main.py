import tkinter as tk
from collections import namedtuple
import math

class Drawing:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        window = tk.Tk()
        self.canvas = tk.Canvas(window, height=width, width=height, bg="white")
        self.draw()
        self.canvas.pack()
        window.mainloop()


class MyDrawing(Drawing):
    def __init__(self, width, height):
        super().__init__(width, height)

    def draw(self):
        self.canvas.create_line(self.width/ 4,self.height/4, 3*self.width/4, self.height /4, 3*self.width/4, 3*self.height/4, self.width / 4, 3*self.height /4, self.width/4, self.height /4)


Point = namedtuple('Point', ['x', 'y'])


class KochSnowflake(Drawing):

    def __init__(self, width, height):
         super().__init__(width, height)

    @staticmethod
    def peaked_line_points(start, end):
        diffx = end.x - start.x
        diffy = end.y - start.y
        print(f"diffx:  {diffx} --- {diffy}")
        length = math.sqrt(diffx*diffx + diffy*diffy)

        first_third = Point(start.x + (diffx / 3.0), start.y + (diffy / 3.0))
        second_third = Point(start.x + 2*(diffx / 3.0), start.y + 2*(diffy / 3.0))

        current_theta = math.asin(diffy / length)
        if (diffx < 0):
            current_theta = math.pi - current_theta

        new_theta = current_theta + math.asin(0.5)

        peak_height = length / 3.0 * math.sqrt(3.0)

        peak = Point(start.x + math.cos(new_theta)*peak_height,
                     start.y + math.sin(new_theta)*peak_height)

        return [start, first_third, peak, second_third, end]




    def draw_line(self, start, end, depth):
        if depth == 0:
            self.canvas.create_line(start, end)
            return

        points = KochSnowflake.peaked_line_points(start, end)

        self.draw_line(points[0], points[1], depth -1)
        self.draw_line(points[1], points[2], depth -1)
        self.draw_line(points[2], points[3], depth -1)
        self.draw_line(points[3], points[4], depth -1)


    def draw(self):
        self.draw_line(Point(0.1* self.width, 0.8*self.height), Point(0.9*self.width, 0.8*self.height), 7)




# MyDrawing(800, 800)
KochSnowflake(800, 800)
