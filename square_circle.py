import turtle
def draw_suqare(st):
    for i in range(1,5):
        st.forward(200)
        st.right(90)
def draw_art():
    window=turtle.Screen()
    window.bgcolor("black")
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(6)
    brad.pensize(2)
    for i in range(1,37):
        draw_suqare(brad)
        brad.right(10)
    window.exitonclick()
draw_art()