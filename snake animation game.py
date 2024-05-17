import curses 
import random
# Print the instructions for the user  
print("Instructions:")
print("Use the arrow keys to move the snake [up-arrow,dow-arrow ,right-arrow, left-arrow ."]
print("The snake will move in the direction of the arrow key you press.")
print("If the snake eats the food which is (π), it will grow longer.")
print("If the snake hits the border or itself, the game will end.")
print("Enjoy the game!")

# Initialize the screen of the game
s = curses.initscr()

# Set the cursor to 0 for initializing it
curses.curs_set(0)

# Get the height and the width of the screen
sh, sw = s.getmaxyx()

# Create a new window using screen height and width
w = curses.newwin(sh, sw, 0, 0)

# Accept keypad input by preparing the environment for the user 
w.keypad(1)

# Refresh screen every 100 millisecs for each touch from the user in the live screen
w.timeout(100)

# Create the snake initial position by using the cordinate of the graph (x and y)
snk_x = sw//4
snk_y = sh//2

# Initial snake body parts
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2] 
]
# Create the snake food which
food = [sh//2, sw//2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI) used to similate live screen

# Initial snake direction is to the right
key = curses.KEY_RIGHT

# Infinite loop for game execution( as long as the user play very well by respecting the instructions,the game can continue)
while True:
    # Get the next key
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Check if snake runs over the border or itself(the area is limited, if the user bite the borders, the loop stop)
    if snake[0][0] in [0, sh] or \
        snake[0][1]  in [0, sw] or \
        snake[0] in snake[1:]:
        # End the window
        curses.endwin()
        quit()

    # Determine the new head of the snake after the user got the previous one
    new_head = [snake[0][0], snake[0][1]]

    # Update the head based on the direction
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Insert the new head of the snake
    snake.insert(0, new_head)

    # Determine what happens when the snake eats the food( the food is defined as pie symbol)
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    # Add the head of the snake to the screen( to refresh the game if the user find the food)
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
