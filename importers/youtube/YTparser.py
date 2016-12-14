import nltk
import csv

class YouTubeParser():

    def __init__(self):
        pass

    def parse(self, text):
        allWords = nltk.tokenize.word_tokenize(text)
        allWordDist = nltk.FreqDist(w.lower() for w in allWords)

        stopwords = nltk.corpus.stopwords.words('english')
        allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allWords if w not in stopwords)

        mostCommon = allWordExceptStopDist.most_common(50)

        for word, occurrences in mostCommon:
            print(word)
            print(occurrences)


        with open('output/out.csv', 'w', newline='') as fp:
            a = csv.writer(fp, delimiter=',')
            data = mostCommon
            a.writerows(data)
