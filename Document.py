from Interval import Interval
from Tokens import Token, get_shape_category_simple
from typing import List

class Document:
    @classmethod
    def create_from_vectors(cls, words: List[str], sentences: List[Interval]=None, labels: List[str]=None):
        doc = Document()
        text = []
        offset = 0
        doc.sentences = []
        for sentence in sentences:
            text.append(' '.join(words[sentence.start:sentence.end + 1]) + ' ')
            doc.sentences.append(Interval(offset, offset + len(text[-1])))
            offset += len(text[-1])
        doc.text = ''.join(text)

        offset = 0
        doc.tokens = []
        for word, label in zip(words, labels):
            pos = doc.text.find(word, offset)
            if pos >= 0:
                offset = pos + len(word)
                doc.tokens.append(Token(doc, pos, offset, None, get_shape_category_simple(word), word, label=label))
        return doc