import math
import matplotlib.pyplot as plt
from Generaldistribution import Distribution

class Geometric(Distribution):
    def __init__(self, prob):
        self.p = prob
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
    def calculate_mean(self):
        self.mean = (1-self.p)/self.p
        return self.mean
    def calculate_stdev(self):
        self.stdev = (1-self.p)/(self.p**2)
        return self.stdev