from Interval import Interval
import re

class Token(Interval):
    """ A Interval representing word like units of text with a dictionary of features """

    def __init__(self, document, start: int, end: int, pos: str, shape: int, text: str):
        """
        Note that a token has 2 text representations.
        1) How the text appears in the original document e.g. doc.text[token.start:token.end]
        2) How the tokeniser represents the token e.g. nltk.word_tokenize('"') == ['``']
        :param document: the document object containing the token
        :param start: start of token in document text
        :param end: end of token in document text
        :param pos: part of speach of the token
        :param shape: integer label describing the shape of the token
        :param text: this is the text representation of token
        """

        Interval.__init__(self, start, end)
        self._doc = document
        # TODO: To be implemented


    @property
    def text(self):
        """ TODO: To be implemented"""
        return self.text

    @property
    def pos(self):
        """ TODO: To be implemented"""
        return self.pos

    @property
    def shape(self):
        """ TODO: To be implemented"""
        return self.shape
    def __getitem__(self, item):
        """ TODO: To be implemented"""

    def __repr__(self):
        return 'Token({}, {}, {})'.format(self.text, self.start, self.end)


class Sentence(Interval):
    """ Interval corresponding to a Sentence"""

    def __init__(self, document, start: int, end: int):
        Interval.__init__(self, start, end)
        self._doc = document

    def __repr__(self):
        return 'Sentence({}, {})'.format(self.start, self.end)

    @property
    def tokens(self):
        """Returns the list of tokens contained in a sentence"""
        # TODO: To be implemented (tip: use Interval.overlap)


def get_shape_category_simple(word):
    if word.islower():
        return 'ALL-LOWER'
    elif word.isupper():
        return 'ALL-UPPER'
    elif re.fullmatch('[A-Z][a-z]+', word):
        return 'FIRST-UPPER'
    else:
        return 'MISC'