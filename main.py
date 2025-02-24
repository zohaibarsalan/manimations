from manim import *

# Set the resolution for Instagram Reels (1080x1920)
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16
config.frame_width = 9

class WelcomeScene(Scene):
    def construct(self):
        # Create the text object with blue color
        welcome_text = Text("Welcome to Visium", color="#d9d9d9") 

        # Position the text in the center
        welcome_text.move_to(ORIGIN)
        
        # Add the text to the scene
        self.play(Write(welcome_text))
        
        # Keep the text on screen for a while
        self.wait(1)
