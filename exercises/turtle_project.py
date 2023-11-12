"""TODO: We are creatinga beautiful cottage before a sunset."""
__author__ = "730649407"


from turtle import Turtle, colormode, done
from random import randint
colormode(255)




def main() -> None:
   """This is the main function where I call all of the other functions to draw my masterpiece."""
   baby_turtle: Turtle = Turtle()
   baby_turtle.speed(10)


   colored_background(baby_turtle, 235, 34, 20, -300, 300)
   colored_background(baby_turtle, 243, 70, 18, -300, 200)
   colored_background(baby_turtle, 243, 145, 18, -300, 100)
   colored_background(baby_turtle, 18, 123, 243, -300, 0)
   colored_background(baby_turtle, 21, 134, 13, -300, -100)
   square(baby_turtle, -250, -100)
   triangle(baby_turtle, -250, 100, 200)
   window(baby_turtle, -175, 25)
   door(baby_turtle, -175, -100)


   triangle(baby_turtle, 0, -100, 75)
   triangle(baby_turtle, 85, -100, 75)
   triangle(baby_turtle, 170, -100, 75)


   fun_message(baby_turtle, 0, -300)


   baby_turtle.hideturtle()


   done()




def go_to_location(object: Turtle, x: float, y: float, direction: int) -> None:
   """This function simplifies the process by moving the object to a given location. That way you can simply pass in the location as an argument and it will go to the location without having to retype this code in every function. It also uses the setheading method (line 42)."""
   object.penup()
   object.goto(x, y)
   object.pendown()
   object.setheading(direction)




def background_outline(object: Turtle, x: float, y: float) -> None:
   """This function has the object go to a certain location (line 49) and then draw a large rectangle across the scene. This function is used to create multiple rectangles in order to generate a background. It is called more than twice. It uses a loop to create the rectangle (line 52)."""
   go_to_location(object, x, y, 0)


   i: int = 0
   while (i < 2):
       object.forward(600)
       object.right(90)
       object.forward(100)
       object.right(90)
       i += 1




def colored_background(object: Turtle, r: int, g: int, b: int, x: float, y: float) -> None:
   """This function calls the background_outline function (line 67) in order to fill the color for the rectangles (line 65) something other than white. By doing so, I'm painting a beautiful sunset that layers the colors red, orange, and yellow. The blue rectangle intends to show a river and the green rectangle is grass. This procedure is called multiple times to create a clever sunset."""
   object.fillcolor(r, g, b)
   object.begin_fill()
   background_outline(object, x, y)
   object.end_fill()




def square(object: Turtle, x: float, y: float) -> None:
   """This draws a white square using a loop (line 78) which is the outline of the house."""
   go_to_location(object, x, y, 90)


   object.color("white")
   object.begin_fill()
  
   counter: int = 0
   while (counter < 4):
       object.forward(200)
       object.right(90)
       counter += 1
   object.end_fill()




def rand_color() -> int:
   """Calls the randint function from the random library to return a random integer between 1 and 250 (line 88). I will call it to generate numbers for my rgb sequence in various other functions."""
   random_integers = randint(1, 250)
   return random_integers




def triangle(object: Turtle, x: float, y: float, distance: int) -> None:
   """This draws a tringle. It passes in color and distance as parameters so one can decide what color (lines 98-103) and size (line 107) they want the triangle to be. It will be used to create the hat of the house and some bushes next to the house. Calls the rand_color function to randomly generate the fill color of this object."""
   go_to_location(object, x, y, 0)


   r: int = rand_color()
   g: int = rand_color()
   b: int = rand_color()


   object.color(r, g, b)
   object.begin_fill()


   counter: int = 0
   while (counter < 3):
       object.forward(distance)
       object.left(120)
       counter += 1
   object.end_fill()




def window(object: Turtle, x: float, y: float) -> None:
   """This function creates a window. I used a loop (line 125) for the basic square component. This uses brown as the marker color. Calls the rand_color method (lines 118-122) to randomly generate the fill color of this object."""
   go_to_location(object, x, y, 90)


   r: int = rand_color()
   g: int = rand_color()
   b: int = rand_color()


   object.color(r, g, b)


   counter: int = 0
   while (counter < 4):
       object.forward(50)
       object.right(90)
       counter += 1


   object.forward(25)
   object.right(90)
   object.forward(50)
   object.right(90)
   object.forward(25)
   object.right(90)
   object.forward(25)
   object.right(90)
   object.forward(50)




def door(object: Turtle, x: float, y: float) -> None:
   """This creates a vertical rectangle to represent the door. It calls other functions and uses the fill color. It has a loop (line 154) for the rectangle. Calls the rand_color method (lines 146-151) to randomly generate the fill color of this object."""
   go_to_location(object, x, y, 90)


   r: int = rand_color()
   g: int = rand_color()
   b: int = rand_color()


   object.color(r, g, b)
   object.begin_fill()


   counter: int = 0
   while (counter < 4):
       object.forward(100)
       object.right(90)
       counter += 1
   object.end_fill()




def fun_message(object: Turtle, x: float, y: float) -> None:
   """This will generate a fun message on the screen. It uses the write method (line 165) which wasn't mentioned anywhere in the turtle tutorial."""
   object.penup()
   object.goto(x, y)
   object.pendown()
   object.write("Have a great day!", move=True, align='center', font=('Courier', 28, 'normal'))




if __name__ == "__main__":
   main()