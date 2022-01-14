from turtle import Turtle

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.all_segment = []
        self.create_snake()
        self.head = self.all_segment[0]

    def create_snake(self):
        for pos in starting_pos:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(pos)
            self.all_segment.append(segment)
            segment.speed("slowest")

    def move(self):
        for seg_num in range(len(self.all_segment) - 1, 0, -1):
            new_x = self.all_segment[seg_num - 1].xcor()
            new_y = self.all_segment[seg_num - 1].ycor()
            self.all_segment[seg_num].goto(new_x, new_y)
        self.all_segment[0].forward(move_distance)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.all_segment.append(segment)
        segment.speed("slowest")

    def extend(self):
        self.add_segment((self.all_segment[-1].position()))

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
