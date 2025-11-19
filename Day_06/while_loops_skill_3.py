# using while loops with if-else statements

def elevator_floor(enter, exit):
    floor = enter
    elevator_direction = " "

    if enter > exit:
        elevator_direction = "Going down: "

    while floor >= exit:
        elevator_direction += str(floor)

        if floor > exit:
            elevator_direction += " | "
        floor -= 1

    else:
        elevator_direction = "Going up: "

        while floor <= exit:
            elevator_direction += str(floor)
        if floor < exit:
            elevator_direction += " | "
    
        floor += 1
    return elevator_direction

print(elevator_floor(1,4))
print(elevator_floor(6,2))
