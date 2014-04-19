# template for "Stopwatch: The Game"
import simplegui
# define global variables

the_time = 0
x = 0
y = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    D = t % 10
    C = (t / 10) % 10
    B = (t / 100) % 6
    A = (t / 100) / 6 
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    

# define event handlers for buttons; "Start", "Stop", "Reset"

    
def start():
    global timer
    timer.start()

    
def stop():
    global timer, x, y, the_time
    timer.stop()
    y += 1
    if (the_time % 10 == 0):
        x += 1
def reset():
    global the_time, x, y
    the_time = 0
    x = 0
    y = 0

# define event handler for timer with 0.1 sec interval
def update_time():
    global the_time
    the_time += 1

# define draw handler

def draw(canvas):
    canvas.draw_text(format(the_time), [100, 120], 40, "Red")
    canvas.draw_text(str(x) + "/" + str(y), [250, 30], 20, "Yellow")
# create frame
frame = simplegui.create_frame("Home", 300, 200)

timer = simplegui.create_timer(100, update_time);
frame.set_draw_handler(draw)

# register event handlers

frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()

# Please remember to review the grading rubric
