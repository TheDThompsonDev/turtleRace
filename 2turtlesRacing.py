import turtle              # 1. import the modules
import random
wn = turtle.Screen()       # 2. Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3. Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4. Move the turtles to their starting point
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)

# your code goes here
for distance in range(0, 50):
    length1 = random.randrange (0, 10)
    length2 = random.randrange (0, 10)
    
    lance.forward(length1)
    andy.forward(length2)
    
wn.exitonclick()
