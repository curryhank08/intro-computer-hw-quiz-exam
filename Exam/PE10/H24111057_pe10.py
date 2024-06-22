""" 
author: H24111057 姚博瀚
"""
import curses
import random

# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(200)  # Increase the timeout to slow down the snake

# Initial position and size of the snake
snk_x = sw // 4
snk_y = sh // 2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]

# Initialize food
food = [sh // 2, sw // 2]
w.addch(food[0], food[1], curses.ACS_PI)

# Calculate the number of obstacle cells needed to cover 5% of the screen
total_cells = sh * sw
obstacle_cells = total_cells // 20
obstacles = []

while len(obstacles) < obstacle_cells:
    obs_y = random.randint(1, sh - 2)
    obs_x = random.randint(1, sw - 2)
    obs_orientation = random.choice(['h', 'v'])
    if obs_orientation == 'h' and obs_x + 5 < sw:
        new_obstacle = [[obs_y, obs_x + i] for i in range(5)]
    elif obs_orientation == 'v' and obs_y + 5 < sh:
        new_obstacle = [[obs_y + i, obs_x] for i in range(5)]
    else:
        continue
    if not any(part in snake for part in new_obstacle) and not any(part in obstacles for part in new_obstacle):
        obstacles.extend(new_obstacle)

for obstacle in obstacles:
    w.addch(obstacle[0], obstacle[1], curses.ACS_CKBOARD, curses.A_REVERSE)

key = curses.KEY_RIGHT
food_eaten = {'normal': 0, 'special': 0}

paused = False

while True:
    next_key = w.getch()
    
    if next_key == ord(' '):
        paused = not paused
        if paused:
            w.addstr(sh // 2, sw // 2 - 7, "Game Paused")
            w.refresh()
        else:
            w.addstr(sh // 2, sw // 2 - 7, "            ")  # Clear pause message
            w.refresh()
    
    if paused:
        continue
    
    key = key if next_key == -1 or next_key == ord(' ') else next_key

    # Calculate the next coordinates of the snake's head
    if key == curses.KEY_DOWN:
        new_head = [snake[0][0] + 1, snake[0][1]]
    elif key == curses.KEY_UP:
        new_head = [snake[0][0] - 1, snake[0][1]]
    elif key == curses.KEY_LEFT:
        new_head = [snake[0][0], snake[0][1] - 1]
    elif key == curses.KEY_RIGHT:
        new_head = [snake[0][0], snake[0][1] + 1]
    else:
        new_head = snake[0]

    # Wrap around the screen boundaries
    new_head[0] = new_head[0] % sh
    new_head[1] = new_head[1] % sw

    # Check for collisions
    if new_head in snake:
        reason = "Hit itself"
        break
    if new_head in obstacles:
        reason = "Hit an obstacle"
        break

    # Insert new head and check for food
    snake.insert(0, new_head)
    if snake[0] == food:
        if w.inch(food[0], food[1]) == curses.ACS_PI:
            food_eaten['normal'] += 1
            snake.append(snake[-1])
        elif w.inch(food[0], food[1]) == ord('X'):
            food_eaten['special'] += 1
            if len(snake) > 1:
                snake.pop()
        while food in snake or food in obstacles:
            food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
        w.addch(food[0], food[1], curses.ACS_PI if random.choice([True, False]) else ord('X'))
    else:
        # Remove the tail
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    # Render the snake
    for segment in snake:
        w.addch(segment[0], segment[1], curses.ACS_CKBOARD)

curses.endwin()
print(f"Game Over because {reason}!")
print(f"Normal food eaten: {food_eaten['normal']}, Special food eaten: {food_eaten['special']}")
