from utils import *
import numpy as np

class Tiler:
    def __init__(self, env, num_tilings, num_tiles):
        self.env = env
        self.num_tilings = num_tilings
        self.num_tiles = num_tiles
        self.max_values = env.observation_space.high
        self.min_values = env.observation_space.low
        self.high = self.max_values - self.min_values
        self.low = self.min_values - self.min_values
        self.dim = len(self.max_values)
        self.actions = env.action_space
        self.num_actions = 3

        self.orientation = "flat"
        self.layout = Layout()

    def calculate_hex_size(self):
        pass