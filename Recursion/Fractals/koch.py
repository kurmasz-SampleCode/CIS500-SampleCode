from collections import namedtuple
import math
from drawing import Drawing

# A named tuple that can bundle a pair of x and y values together.
Point = namedtuple('Point', ['x', 'y'])

class KochSnowflake(Drawing):

    DEPTH = 7

    def __init__(self, width, height):
         super().__init__(width, height)

    @staticmethod
    def peaked_line_points(start, end):
        diffx = end.x - start.x
        diffy = end.y - start.y
        length = math.sqrt(diffx*diffx + diffy*diffy)

        first_third = Point(start.x + (diffx / 3.0), start.y + (diffy / 3.0))
        second_third = Point(start.x + 2*(diffx / 3.0), start.y + 2*(diffy / 3.0))

        current_theta = math.asin(diffy / length)
        if diffx < 0:
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

        fill_factor = 0.9
        smaller_dimension = min(self.width, self.height)
        desired_total_height = smaller_dimension * fill_factor # desired total height of the snowflake
        triangle_height  = 0.75 * desired_total_height
        half_base = triangle_height / math.sqrt(3)

        peak = Point(self.width / 2, (self.height - desired_total_height) / 2)
        left_base = Point(peak.x - half_base, peak.y + triangle_height)
        right_base = Point(peak.x + half_base, peak.y + triangle_height)

        self.draw_line(peak, left_base, KochSnowflake.DEPTH)
        self.draw_line(left_base, right_base, KochSnowflake.DEPTH)
        self.draw_line(right_base, peak, KochSnowflake.DEPTH)


if __name__ == '__main__':
    KochSnowflake(1200, 1200)
