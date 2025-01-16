from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def etch_sketch_app_forward():
    tim.forward(10)

def etch_sketch_app_backward():
    tim.backward(10)

def etch_sketch_app_left():
    # new_heading = tim.heading() + 10
    # tim.setheading(new_heading)

    tim.left(10)
    tim.forward(20)


def etch_sketch_app_right():
    # new_heading = tim.heading() - 10
    # tim.setheading(new_heading)
    tim.right(10)
    tim.backward(20)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(etch_sketch_app_forward, 'W')
screen.onkey(etch_sketch_app_backward, 'S')
screen.onkey(etch_sketch_app_left, 'A')
screen.onkey(etch_sketch_app_right, 'D')
screen.onkey(clear, 'c')
screen.exitonclick()