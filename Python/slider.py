import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.animation import FuncAnimation

# Parameters
t_start = -100
t_end = 100
t_spacing = 10000
t = np.arange(t_start, t_end, 1 / t_spacing)

slope = 0
intercept = 10
y = slope * t + intercept

t_limits = [-15, 15]
y_limits = [-15, 15]

# Create figure and plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
line, = ax.plot(t, y, lw=2)

ax.set_xlim(t_limits)
ax.set_ylim(y_limits)

[slider_min, slider_max] = [0.0, 5.0]

# Update function for the slider
def update(val):
    slope = slider.val  # Get current slider value
    y = slope * t + intercept
    line.set_ydata(y)
    fig.canvas.draw_idle()

# Play function to gradually change slope (using FuncAnimation)
def play(event):
    def animate(i):
        slope = slider_min + i * (slider_max - slider_min) / 100  # Gradual increase of slope
        slider.set_val(slope)  # Update slider value
        y = slope * t + intercept
        line.set_ydata(y)  # Update line data
        fig.canvas.draw_idle()  # Redraw plot
    global ani
    ani = FuncAnimation(fig, animate, frames=100, interval=50, repeat=False)

# Add a slider
ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Slope', slider_min, slider_max, valinit=slider_min)

# Add a button
ax_button = plt.axes([0.1, 0.1, 0.05, 0.04])
button = Button(ax_button, 'Play')

# Set the update function for slider change
slider.on_changed(update)

# Set the play function for button click
button.on_clicked(play)

plt.show()
