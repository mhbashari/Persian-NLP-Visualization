from BaseTools import WordVisualizationBase2d
from tsne import tsne
import numpy as np


class WordVisulizationTSNE:
    def __init__(self, labels, X, Y):
        super().__init__()
        self.n_components = 2
        self.vix = None
        self.labels = labels
        self.X = X
        self.Y = Y
        # self.check_type()
        self.reduce_dimention()

    def check_type(self):
        if type(self.X) == list:
            self.X = np.array(self.X)
        if type(self.Y) == list:
            self.Y = np.array(self.Y)

    def reduce_dimention(self):
        # Y = tsne(self.X, 2, 50, 20.0)
        self.viz = WordVisualizationBase2d(labels=self.labels,X=self.X, Y=self.Y)
        # self.viz.show_plot()

    def show_plot(self):
        self.viz.show_plot()
