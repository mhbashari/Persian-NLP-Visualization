def test_word_visualization():
    print("++")
    import BaseTools
    wv = BaseTools.WordVisualization({"apple": (1, 2), "banana": (1, 3), "cat": (4, 7)})
    wv.show_plot()


test_word_visualization()
