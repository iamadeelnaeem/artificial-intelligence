
def is_move(move):
    if move == 'u' or move == 'd' or move == 'l' or move == 'r':
        return True
    else:
        return False


def can_move(move, current_location, world_size):
    if move == 'u' and current_location[0] == 0:
        return False
    if move == 'l' and current_location[1] == 0:
        return False
    if move == 'r' and current_location[1] == (world_size - 1):
        return False
    if move == 'd' and current_location[0] == (world_size - 1):
        return False

    return True


def new_location(current_location):
    if move == 'u':
        return [current_location[0]-1,current_location[1]]
    if move == 'l':
        return [current_location[0],current_location[1]-1]
    if move == 'r':
        return [current_location[0],current_location[1]+1]
    if move == 'd':
        return [current_location[0]+1, current_location[1]]


def is_gold(wampus_world, current_location):
    if wampus_world[current_location[0]][current_location[1]] == 'g':
        return True
    else:
        return False


def is_hurdle(wampus_world, current_location):
    block = wampus_world[current_location[0]][current_location[1]]
    if block == 'w' or block == 'p':
        return True
    else:
        return False

def check_enviornment(world_size, wampus_world, current_location, move):
    up = None
    down = None
    left = None
    right = None

    if can_move('u',current_location,world_size):
        up = wampus_world[current_location[0]-1][current_location[1]]
    if can_move('d', current_location, world_size):
        down = wampus_world[current_location[0]+1][current_location[1]]
    if can_move('l', current_location, world_size):
        left = wampus_world[current_location[0]][current_location[1]-1]
    if can_move('r', current_location, world_size):
        right = wampus_world[current_location[0]][current_location[1]+1]

    if up == 'w' or down == 'w' or left == 'w' or right == 'w':
        print("There is smell around")

    if up == 'p' or down == 'p' or left == 'p' or right == 'p':
        print("There is breeze around")


def shoot_arrow(world_size, wampus_world, current_location, direction):
    if direction == 'u' and current_location[0]!=0 and wampus_world[current_location[0] - 1][current_location[1]] == 'w':
        return True
    if direction == 'd' and current_location[0] != (world_size - 1) and wampus_world[current_location[0] + 1][current_location[1]] == 'w':
        return True
    if direction == 'l' and current_location[1] != 0 and wampus_world[current_location[0]][current_location[1]-1] == 'w':
        return True
    if direction == 'r' and current_location[1] != (world_size - 1) and wampus_world[current_location[0]][current_location[1]+1] == 'w':
        return True

    return False

wampus_world = []
world_size = None
no_of_arrows = None

with open('env1.txt') as rf:
    world_size = int(rf.readline())
    for i in range(int(world_size)):
        wampus_world.append(['-' for j in range(world_size)])

    no_of_arrows = int(rf.readline())

    lines = rf.readlines()
    for line in lines:
        tokens = line.split(' ')
        wampus_world[int(tokens[1])][int(tokens[2])] = tokens[0]

    for row in wampus_world:
        print(row)

current_location = [0, 0]


flag = False
while True:
    for i, row in enumerate(wampus_world):
        for j, val in enumerate(row):
            if i == current_location[0] and j == current_location[1]:
                print('A ', end='')
            else:
                print('- ', end='')
        print()

    print("Press : ")
    print("u for Up")
    print("d for down")
    print("l for left")
    print("r for right")

    move = input("Move the agent : ")

    if is_move(move):
        if can_move(move, current_location, world_size):
            current_location = new_location(current_location)
            if is_gold(wampus_world, current_location):
                flag = True
                break
            elif is_hurdle(wampus_world, current_location):
                break
            else:
                check_enviornment(world_size, wampus_world, current_location, move)
                if no_of_arrows > 0:
                    option = input("Do you want to shoot and arrow : (y/n) ")
                    if option == 'y':
                        print("Press : ")
                        print("u for Up")
                        print("d for down")
                        print("l for left")
                        print("r for right")

                        direction = input("Enter direction of arrow : ")
                        is_killed = shoot_arrow(world_size, wampus_world, current_location, direction)
                        if is_killed:
                            no_of_arrows = no_of_arrows - 1
                    if option == 'n':
                        print("OK")
        else:
            print("can't move to this location")
    else:
        print("Invalid input!")


if flag:
    print("You win!!")
else:
    print("You lose!!")
