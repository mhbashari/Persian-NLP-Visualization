from bidi.algorithm import get_display
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from gensim.models.word2vec import Word2Vec

import arabic_reshaper
from sklearn.manifold import TSNE

matplotlib.rc('font', family='KacstOne')


class WordVisualizationBase2d:
    class Config:
        pass

    def __init__(self, word_dict=None, **kwargs):
        if word_dict is not None:
            self.word_dict = word_dict
            data = [item for key, item in word_dict.items()]
            self.labels = list(self.words_arabic_reshape(word_dict.keys()))
            # print(data)
            self.X = [elem[0] for elem in data]
            self.Y = [elem[1] for elem in data]
            self.colors = [index / 1000 for index in range(len(self.X))]
            self.size = 50
        elif kwargs is not None:
            print("You did not set as list")
            self.labels = self.words_arabic_reshape(kwargs["labels"])

            self.X = kwargs["X"]
            # print(self.X)
            self.Y = kwargs["Y"]

    def get_X(self):
        print("get_X->", self.X)
        return self.X

    def get_Y(self):
        return self.Y

    def get_labels(self):
        return self.labels

    def words_arabic_reshape(self, words):
        return map(lambda x: self.word_process(x), words)

    def show_plot(self):
        fig = plt.figure()
        fig.suptitle(self.word_process('مصورسازی کلمات براساس بردار عددی'), fontsize=14, fontweight='bold')
        ax = fig.add_subplot(111)
        fig.subplots_adjust(top=0.85)
        for label, x, y in zip(self.labels, self.X, self.Y):
            ax.text(x, y, label, fontsize=8, fontweight='regular')
        ax.axis([0, 10, 0, 10])
        plt.show()

    def word_process(self, x):
        reshaped_text = arabic_reshaper.reshape(x)
        return get_display(reshaped_text)


class W2VPersianVis:
    def __init__(self, w2v_model_path, selected_words=None):
        self.model_path = w2v_model_path
        self.model = Word2Vec.load(self.model_path)
        self.selected_words = selected_words

    def show_plot(self):
        self.reduce_dimentionality()
        if self.selected_words is None:
            self.plt = WordVisualizationBase2d(X=self.reduced_vectors[:, 0], Y=self.reduced_vectors[:, 1],
                                               labels=self.model.vocab.keys())
        else:
            self.plt = WordVisualizationBase2d(X=self.reduced_vectors[:, 0], Y=self.reduced_vectors[:, 1],
                                               labels=self.selected_words)
        self.plt.show_plot()

    def reduce_dimentionality(self):
        self.vectors = []
        for key in self.selected_words:
            self.vectors.append(self.model[key])
        tnse_model = TSNE(n_components=2, random_state=0)
        np.set_printoptions(suppress=True)
        self.reduced_vectors = tnse_model.fit_transform(self.vectors)
