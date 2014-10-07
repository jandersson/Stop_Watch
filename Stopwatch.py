import simpleguitk as simplegui

# define global variables
button_width = 100
interval = 100  #100 millisecond interval for timer
time = 0
stop_counter = 0
stop_hits = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    seconds = (t/10)
    seconds_string = str(seconds % 60)
    if (seconds%60) < 10:
        seconds_string = "0"+seconds_string
    minutes = seconds / 60
    minutes_string = str(minutes)
    deci_seconds = t % 10
    deci_seconds_string = str(deci_seconds)
    time_string = minutes_string + ":" + seconds_string + "." + deci_seconds_string
    return time_string

# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start():
    stopwatch.start()

def button_stop():
    global stop_counter
    stopwatch.stop()
    stop_counter += 1

def button_reset():
    global time, stop_counter, stop_hits
    stopwatch.stop()
    time = 0
    stop_counter = 0
    stop_hits = 0

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
