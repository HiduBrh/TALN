from Parse import EnglishPosParser
from Vectorize import Vectorizer
parser = EnglishPosParser()
documents = parser.read_file("eng.train")
vectorizer = Vectorizer("glove.6B.50d.w2v.txt")
#features = vectorizer.encode_features(documents)
annotations = vectorizer.encode_annotations(documents)
print(documents[0].text)

