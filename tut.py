from gensim.models.word2vec import LineSentence
from hazm import Normalizer, sent_tokenize, word_tokenize
from gensim.models import word2vec

from BaseTools import W2VPersianVis


def sentences(file="simple_text"):
    normalizer = Normalizer()
    for line in open(file, "r", encoding="utf-8").readlines():
        for sent in sent_tokenize(line):
            yield word_tokenize(line)


def create_word2vec(plain_text):
    model = word2vec.Word2Vec(sentences=list(sentences()), size=50, window=5, min_count=0)
    model.save("basica_persian_model.model")


def test_word_visualization(model_path, some_words):
    normalizer = Normalizer()
    model = word2vec.Word2Vec.load(model_path)
    vectors = [model[normalizer.normalize(word)] for word in some_words if
               normalizer.normalize(word) in model.vocab.keys()]
    # print(model[normalizer.normalize('فرهنگ')])
    # print(model.similarity('فرهنگ', 'تمدن'))
    # print(vectors)
    rd = W2VPersianVis(model_path, selected_words=some_words)
    rd.show_plot()


# create_word2vec(open("simple_text", "r", encoding="utf-8").read())
test_word_visualization("basica_persian_model.model", ["حقوق", "قائل", "علامه", "تمدن"])
