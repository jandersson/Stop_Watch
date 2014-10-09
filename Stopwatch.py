import simpleguitk as simplegui

# Global State
button_width = 100
interval = 100  #100 millisecond interval for timer
time = 0
stop_counter = 0
stop_hits = 0
deci_seconds = 0

def format(t):
    """ Takes the time and returns a formatted time string A:BC.D"""
    global deci_seconds
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

def button_start():
    """Starts the stopwatch if it is not already started"""
    if not(stopwatch.is_running()):
        stopwatch.start()

def button_stop():
    """
    Stops the stopwatch if it is running and increments the stop counter
    If the stop occurs on a whole number then the hit counter is increased
    """
    global stop_counter, stop_hits
    if stopwatch.is_running():
        stopwatch.stop()
        stop_counter += 1
        if deci_seconds == 0:
            stop_hits += 1

def button_reset():
    """Resets the stopwatch by setting the time to 0 and the stopwatch counters to 0"""
    global time, stop_counter, stop_hits
    stopwatch.stop()
    time = 0
    stop_counter = 0
    stop_hits = 0

def tick():
    """Timer handler which simply increments the time variable by one"""
    global time
    time += 1

def draw(canvas):
    """Draw handler which draws the formatted value of time and the score using the stopwatch counters"""
    canvas.draw_text(format(time), [100, 100], 24, "White")
    canvas.draw_text(str(stop_hits) + "/" + str(stop_counter), [250, 50], 24, "Green")

#Register event handlers, create frame and timers, and start the frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
stopwatch = simplegui.create_timer(interval, tick)
frame.set_draw_handler(draw)
frame.add_button("Start", button_start, button_width)
frame.add_button("Stop", button_stop, button_width)
frame.add_button("Reset", button_reset, button_width)
frame.start()
