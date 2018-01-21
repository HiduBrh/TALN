from parsers.Parse import EnglishPosParser
from vect.Vectorize import Vectorizer

parser = EnglishPosParser()
documents = parser.read_file("eng.train")
assert (len(documents) == 946)
assert (len(documents[0].sentences)== 20)
assert (len(documents[0].tokens)== 469)

vectorizer = Vectorizer("glove.6B.50d.w2v.txt")
features, shapes = vectorizer.encode_features(documents)
labels = vectorizer.encode_annotations(documents)
assert (len(documents == 20))