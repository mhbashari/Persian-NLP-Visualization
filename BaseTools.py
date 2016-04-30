import numpy as np
import matplotlib.pyplot as plt


class WordVisualization:
    class Config:
        pass

    def __init__(self, word_dict: dict):
        self.word_dict = word_dict
        data = [item for key, item in word_dict.items()]
        self.labels = list(word_dict.keys())
        print(data)
        self.X = [elem[0] for elem in data]
        self.Y = [elem[1] for elem in data]
        self.colors = [index / 1000 for index in range(len(self.X))]
        self.size = 50
        # self.col

    # def save_plot(self, path):
    #     plt.savefig(path)

    def show_plot(self):
        fig = plt.figure()
        fig.suptitle('Word Vector Visualization', fontsize=14, fontweight='bold')

        ax = fig.add_subplot(111)
        fig.subplots_adjust(top=0.85)
        # ax.set_title('axes title')
        #
        # ax.set_xlabel('xlabel')
        # ax.set_ylabel('ylabel')
        #

        # ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)
        #
        ax.text(3, 2, u'سلام')
        #
        # ax.text(0.95, 0.01, 'colored text in axes coords',
        #         verticalalignment='bottom', horizontalalignment='right',
        #         transform=ax.transAxes,
        #         color='green', fontsize=15)


        # ax.plot([2], [1], 'o')
        # ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
        #             arrowprops=dict(facecolor='black', shrink=0.05))

        ax.axis([0, 10, 0, 10])

        plt.show()
