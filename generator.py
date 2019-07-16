from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.train_from_file('titles-and-es-discuss-thread-titles.txt', num_epochs=1)
textgen.generate()
