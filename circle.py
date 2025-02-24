from manim import *

# Set the resolution for Instagram Reels (1080x1920)
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16
config.frame_width = 9

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen