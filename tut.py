from PersianTNSE import WordVisulizationTSNE
def test_word_visualization():
    print("++")
    # wv = BaseTools.WordVisualizationBase2d({"سیب": (1, 2), "موز": (1, 3), "گربه": (4, 7)})
    wv = WordVisulizationTSNE(["سیب", "گلابی", "هلو"], [(1, 1), (2, 2), (2, 2)], [1, 2, 3])
    wv.show_plot()


test_word_visualization()
