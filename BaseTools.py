import numpy as np
from bidi.algorithm import get_display
import matplotlib.pyplot as plt
import arabic_reshaper


class WordVisualization:
    class Config:
        pass

    def __init__(self, word_dict: dict):
        self.word_dict = word_dict
        data = [item for key, item in word_dict.items()]
        self.labels = list(self.words_process(word_dict.keys()))
        print(data)
        self.X = [elem[0] for elem in data]
        self.Y = [elem[1] for elem in data]
        self.colors = [index / 1000 for index in range(len(self.X))]
        self.size = 50
    def words_process(self, words):
        return map(lambda x: self.word_process(x), words)

    def show_plot(self):
        fig = plt.figure()
        fig.suptitle(self.word_process('مصورسازی کلمات براساس بردار عددی'), fontsize=14, fontweight='bold')
        ax = fig.add_subplot(111)
        fig.subplots_adjust(top=0.85)
        for label, x, y in zip(self.labels, self.X, self.Y):
            ax.text(x, y, label)
        ax.axis([0, 10, 0, 10])
        plt.show()

    def word_process(self, x):
        reshaped_text = arabic_reshaper.reshape(x)
        return get_display(reshaped_text)