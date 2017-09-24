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
        print(self.posw.issuperset({text}))
        print(self.negw.issuperset({text}))
        return 0
