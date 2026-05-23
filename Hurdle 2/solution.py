def right():
    turn_left()
    turn_left()
    turn_left()
    
def perform():
    move()
    turn_left()
    move()
    right()
    move()
    right()
    move()
    turn_left()

while not at_goal():
    perform()




