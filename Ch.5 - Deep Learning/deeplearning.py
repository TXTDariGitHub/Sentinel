def remove_stopwords(word, stopword):
    word = word.lower()
    words = word.split()
    temp = [word for word in words if word not in stopword]
    sequences = " ".join(temp)
    return sequences