#Defining turning right direction function
def right():
    turn_left()
    turn_left()
    turn_left()

#This function will perform operation of the required task
def perform():
    move()
    turn_left()
    move()
    right()
    move()
    right()
    move()
    turn_left()

for i in range(1,7):
    perform()
    
#using while loop
# hurdles=6
# while hurdles>0:
#     perform()
#     hurdles-=1
