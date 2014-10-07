import simpleguitk as simplegui

# define global variables
button_width = 100
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass

# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start():
    pass

def button_stop():
    pass

def button_reset():
    pass
# define event handler for timer with 0.1 sec interval


# define draw handler
def draw(canvas):
    canvas.draw_text("00:00", [100,100], 24, "White")

# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", button_start(), button_width)
frame.add_button("Stop", button_stop(), button_width)
frame.add_button("Reset", button_reset(), button_width)
# start frame
frame.start()

# Please remember to review the grading rubric