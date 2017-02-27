import time
import Robot
import Tkinter as tk

LEFT_TRIM = 0
RIGHT_TRIM = -7

speed = 50
keys_pressed = {"w": False, "s": False}

robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

def key_input(event):
    global speed
    global keys_pressed
    key_press = event.keysym.lower()
    print(key_press)

    if key_press == 'w':
        keys_pressed["w"] = True
        robot.forward(speed)
    elif key_press == 's':
        keys_pressed["s"] = True
        robot.backward(speed)
    elif key_press == 'a':
        robot.left(speed)
    elif key_press == 'd':
        robot.right(speed)
    elif key_press == 'space':
        robot.stop()
    elif key_press == 'up':
        if(speed < 255):
            speed += 1
        if(keys_pressed["w"]):
            robot.forward(speed)
        elif(keys_pressed["s"]):
            robot.backward(speed)
    elif key_press == 'down':
        if(speed > 120):
            speed -= 1
        if(keys_pressed["w"]):
            robot.forward(speed)
        elif(keys_pressed["s"]):
            robot.backward(speed)
    print(keys_pressed)
    print(speed)
    # elif key_press == 'q':
    #     robot.backward(150)
    # elif key_press == 'e':
    #     robot.backward(150)

def key_up(event):
    robot.stop()
    
def w_key_up(event):
    global keys_pressed
    keys_pressed["w"] = False
    robot.stop()

def s_key_up(event):
    global keys_pressed
    keys_pressed["s"] = False
    robot.stop()

command = tk.Tk()
command.bind_all('<Key>', key_input)
# command.bind_all('<KeyRelease>', key_up)
command.bind_all('<KeyRelease-w>', w_key_up)
command.bind_all('<KeyRelease-s>', s_key_up)
command.bind_all('<KeyRelease-a>', key_up)
command.bind_all('<KeyRelease-d>', key_up)
command.mainloop()

# robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

# robot.forward(150, 1.0)
# robot.forward(200, 1.0)
# robot.forward(150, 0.5)
# robot.backward(150, 1.0)
# robot.backward(200, 1.0)
# robot.backward(150, 0.5)
