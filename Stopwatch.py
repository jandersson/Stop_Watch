import simpleguitk as simplegui

# define global variables
button_width = 100
interval = 100  #100 millisecond interval for timer
time = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    time_string = str(t)
    return time_string

# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start():
    stopwatch.start()

def button_stop():
    stopwatch.stop()

def button_reset():
    global time
    time = 0
# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time = time + 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [100, 100], 24, "White")

# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
stopwatch = simplegui.create_timer(interval, tick)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", button_start, button_width)
frame.add_button("Stop", button_stop, button_width)
frame.add_button("Reset", button_reset, button_width)

# start frame
frame.start()
