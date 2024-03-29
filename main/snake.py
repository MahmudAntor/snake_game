import random
import curses

def game():
    s = curses.initscr()
    curses.curs_set(0)
    sh, sw = s.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    snk_x = int(sw / 4)
    snk_y = int(sh / 2)
    snake = [
        [snk_y, snk_x],
        [snk_y, int(snk_x - 1)],
        [snk_y, int(snk_x - 2)]
    ]

    food = [int(sh / 2), int(sw / 2)]
    w.addch(food[0], food[1], curses.ACS_PI)

    key = curses.KEY_RIGHT

    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
            # dbg
            curses.endwin()
            break
            # quit()

            # decide = input("Press Y to continue and N to exit ;)")
            # if decide == "Y":
            #     continue
            #
            # else:
            #     curses.endwin()
            #     quit()

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        if snake[0] == food:
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh - 1),
                    random.randint(1, sw - 1)
                ]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        w.addch(snake[0][0], snake[0][1], curses.ACS_PI)


print('Press Y or y to start game and N or n to exit')
command = input()
while command == 'Y' or command == 'y':
    game()
    print('Press Y or y to start over and N or n to exit')
    command = input()


