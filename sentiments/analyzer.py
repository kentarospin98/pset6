import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        posf = open(positives, "r")
        negf = open(negatives, "r")
        self.posw = set()
        self.negw = set()
        for line in posf.readlines():
            if line[0] == ';':
                continue
            else:
                self.posw.add(line.strip("\n"))
                #print(line.strip("\n"))
        for line in negf.readlines():
            if line[0] == ';':
                continue
            else:
                self.negw.add(line.strip("\n"))
                #print(line.strip("\n"))
        posf.close()
        negf.close()
        

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        score = 0
        tokens = nltk.word_tokenize(text)
        for word in tokens:
            if word in self.posw: score+=1
            if word in self.negw: score-=1
        print(score)
        return score
