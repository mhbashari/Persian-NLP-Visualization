def test_word_visualization():
    print("++")
    import BaseTools
    wv = BaseTools.WordVisualization({"سیب": (1, 2), "موز": (1, 3), "گربه": (4, 7)})
    wv.show_plot()


test_word_visualization()
