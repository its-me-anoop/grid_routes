import turtle
import random
import time

t = turtle.Turtle()
t.speed(0)
t.shape("circle")
colors = ["red", "blue", "green", "purple", "magenta", "orange"]
grid_size = 20
count = 20
n = 0
x = 0
y = 0
paths = []
new_path = ""
timeout = 15  # Specify the timeout period (in seconds)


def initial_position(count):
    """
    Set the initial position of the turtle to the top left corner of the grid.
    """
    t.penup()
    t.goto(t.xcor() - (count * grid_size) / 2, t.ycor() + (count * grid_size) / 2)
    t.pendown()


def path_starting_point(count):
    """
    Move the turtle back to the starting point of the grid and set a new random color for the path.
    """
    t.penup()
    t.color(random.choice(colors))
    t.width(5)
    t.goto(t.xcor() - count * grid_size, t.ycor() + count * grid_size)
    t.pendown()


def draw_grid(count):
    """
    Draw a square grid with each cell being a square of side length grid_size.
    The grid contains count*count cells.
    """
    initial_position(count)
    for row in range(count):
        t.pendown()
        for column in range(count):
            for side in range(4):
                t.forward(grid_size)
                t.right(90)
            t.penup()
            t.forward(grid_size)
            t.pendown()
        t.penup()
        t.goto(t.xcor() - count * grid_size, t.ycor() - grid_size)
    t.goto(t.xcor(), t.ycor() + count * grid_size)


def move_forward():
    """
    Move the turtle forward by grid_size units.
    """
    t.forward(grid_size)
    global x
    x += 1


def move_down():
    """
    Move the turtle down by grid_size units.
    """
    t.right(90)
    t.forward(grid_size)
    t.left(90)
    global y
    y += 1


def random_move():
    """
    Move the turtle either forward or down, randomly.
    The movement decision is made randomly with a higher chance of moving down.
    """
    global x, y, new_path

    # Define possible moves
    moves = []
    if x < count:  # Check if moving forward is possible
        moves.append("forward")
        moves.append("forward")
        moves.append("forward")
    if y < count:  # Check if moving down is possible
        moves.append("down")
        moves.append("down")
        moves.append("down")

    # Randomly select a move
    move = random.choice(moves)
    if move == "forward":
        move_forward()
    else:  # move == "down"
        move_down()

    # Add the new position to the path
    new_path += str(x) + str(y)


draw_grid(count)
t.pendown()
t.width(5)
t.color("red")


start_time = time.time()  # Start the timer

while y < count or x < count:
    # Check if the timeout has been reached
    if time.time() - start_time >= timeout:
        print("Timeout reached. Stopping search for new paths.")
        break
    random_move()
    if x == count and y == count:
        if new_path not in paths:
            paths.append(new_path)
            new_path = ""
            print(
                f"New path found: {len(paths)} : {paths[-1]}. Time taken: {time.time() - start_time} seconds."
            )
            start_time = time.time()  # Reset the timer for the next path
        else:
            new_path = ""

        path_starting_point(count)
        x = 0
        y = 0

# Print total number of paths
print(f"Total number of paths: {len(paths)}")

# Find and print the shortest path
if paths:  # Check if the paths list is not empty
    shortest_path = min(
        paths, key=lambda path: len(path) // 2
    )  # Each step is represented by two characters in the string
    t.penup()
    t.goto(0, -(count * grid_size) / 2 - 50)
    t.write(
        "Shortest path: "
        + shortest_path
        + " with "
        + str(len(shortest_path) // 2)
        + " steps",
        align="center",
        font=("Arial", 16, "normal"),
    )
    t.penup()
    t.goto(0, -(count * grid_size) / 2 - 75)
    t.write(
        "Total number of paths found : " + str(len(paths)),
        align="center",
        font=("Arial", 16, "normal"),
    )
    t.hideturtle()
    print(f"Shortest path: {shortest_path} with {len(shortest_path)//2} steps")
else:
    print("No paths were found.")


turtle.done()
