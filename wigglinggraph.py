import networkx as nx
import numpy as np
from manim import *

# Set resolution for Instagram Reels (1080x1920)
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16
config.frame_width = 9

class WigglingGraph(Scene):
    def graph_configure(self, graph, **kwargs):
        for submob in graph.vertices.values():
            submob.jiggling_direction = rotate_vector(
                RIGHT, np.random.random() * TAU * 1.5
            )
            submob.jiggling_phase = np.random.random() * TAU * 1.5
        for key, value in kwargs.items():
            setattr(graph, key, value)

    def set_graph_stroke(self, graph, **kwargs):
        for e in graph.edges.values():
            e.set_stroke(**kwargs)

    def construct(self):
        def wiggle_graph_updater(graph, dt):
            # Define two colors for interpolation
            color_1 = RED
            color_2 = BLUE

            for key in graph.edges:
                edge = graph.edges[key]
                edge.start = graph.vertices[key[0]].get_center()
                edge.end = graph.vertices[key[1]].get_center()

            for submob in graph.vertices.values():
                submob.jiggling_phase += graph.jiggles_per_second * TAU * dt
                submob.shift(
                    graph.jiggle_amplitude *
                    submob.jiggling_direction *
                    np.sin(submob.jiggling_phase) * dt
                )

                # Smooth color transition using sine function
                color_factor = (np.sin(submob.jiggling_phase) + 1) / 2  # Normalize between 0 and 1
                submob.set_color(interpolate_color(color_1, color_2, color_factor))

            for edge in graph.edges.values():
                edge.set_stroke(color=interpolate_color(color_1, color_2, np.random.random()), width=0.6)

        graph = nx.newman_watts_strogatz_graph(50, 6, 0.1, seed=248)
        graph_mob = Graph.from_networkx(graph, layout="kamada_kawai", layout_scale=4, labels=False)
        self.graph_configure(graph_mob, jiggle_amplitude=0.3, jiggles_per_second=0.3)
        graph_mob.add_updater(wiggle_graph_updater)
        self.set_graph_stroke(graph_mob, width=0.35)
        self.add(graph_mob)
        self.wait(14)
