import nltk
import csv
from nltk.tokenize import RegexpTokenizer


class YouTubeParser():

    def __init__(self):
        pass

    def parse(self, text, fname):
        tokenizer = RegexpTokenizer(r'\w+')
        allWords = tokenizer.tokenize(text)
        allWordDist = nltk.FreqDist(w.lower() for w in allWords)

        stopwords = nltk.corpus.stopwords.words('english')
        allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allWords if w not in stopwords)

        mostCommon = allWordExceptStopDist.most_common(50)

        for word, occurrences in mostCommon:
            print(word)
            print(occurrences)


        with open(fname, 'w', newline='') as fp:
            a = csv.writer(fp, delimiter=',')
            data = mostCommon
            a.writerows(data)
