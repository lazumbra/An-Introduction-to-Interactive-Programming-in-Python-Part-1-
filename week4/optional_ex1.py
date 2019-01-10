# Print to canvas

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Draw handler
def draw(canvas):
    canvas.draw_text("It works!",[120, 112], 48, "Red")
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("It works", 400, 200)

# register the handler
frame.set_draw_handler(draw)

# start frame
frame.start()

