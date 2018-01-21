from gensim.models import KeyedVectors
from typing import List
from Tokenize import Document
import numpy as np

class Vectorizer:
    """ Transform a string into a vector representation"""

    def __init__(self, word_embedding_path: str):
        """
        :param word_embedding_path: path to gensim embedding file
        """
        # nltk.help.upenn_tagset()
        # Load word embeddings from file
        self._word_embeddings = KeyedVectors.load_word2vec_format(word_embedding_path)
        # Create shape to index dictionary
        self.shape_to_index = {'NL': 0, 'NUMBER': 1, 'SPECIAL': 2, 'ALL-CAPS': 3, '1ST-CAP': 4, 'LOWER': 5, 'MISC': 6}
        # Create labels to index
        self.pos_to_index = {"$":37,"''": 45,'"':38,"(":39,")":40,",":41,"--":42,".":43,":":44,"CC":0,"CD":1,"DT":2,"EX":3,"FW":4,
                          "IN":5,"JJ":6,"JJR":7,"JJS":8,"LS":9,"MD":10,"NN":11,"NNP":12,"NNPS":13,"NNS":14,"PDT":15,
                          "POS":16,"PRP":17,"PRP$":18,"RB":19,"RBR":20,"RBS":21,"RP":22,"SYM":23,"TO":24,"UH":25,
                          "VB":26,"VBD":27,"VBG":28,"VBN":29,"VBP":30,"VBZ":31,"WDT":32,"WP":33,"WP$":34,"WRB":35,
                          "``":36,"NN|SYM":46}
        self.labels_to_index= {'o':0, 'PER':1, 'I-PER':1, 'B-PER':1, 'LOC':2, 'I-LOC':2, 'B-LOC':2, 'ORG':3, 'I-ORG':3,
                               'B-ORG':3, 'MISC':4, 'I-MISC':4, 'B-MISC':4}
        self.labels = ['o','PER','LOC','ORG','MISC']


    def encode_features(self, documents: List[Document]):
        """
        Creates a feature matrix for all documents in the sample list
        :param documents: list of all samples as document objects
        :return: lists of numpy arrays for word, pos and shape features.
                 Each item in the list is a sentence, i.e. a list of indices (one per token)
        """
        words=[]
        shapes=[]
        # Loop over documents
        for doc in documents:
        #    Loop over sentences
            for sentence in doc.sentences:
                sentence_words=[]
                sentence_shapes=[]
        #        Loop over tokens
                for token in sentence.tokens:
        #           Convert features to indices
        #           Append to sentence
                    if token.text.lower() in self._word_embeddings.vocab:
                        sentence_words.append(self._word_embeddings.index2word.index(token.text.lower()))
                        sentence_shapes.append(self.shape_to_index[token.shape])
                words.append(sentence_words)
                shapes.append(sentence_shapes)
        return np.array(words), np.array(shapes)

    def encode_annotations(self, documents: List[Document]):
        """
        Creates the Y matrix representing the annotations (or true positives) of a list of documents
        :param documents: list of documents to be converted in annotations vector
        :return: numpy array. Each item in the list is a sentence, i.e. a list of labels (one per token)
        """
        labels = []
        # Loop over documents
        for doc in documents:
            #    Loop over sentences
            for sentence in doc.sentences:
                sentence_labels = []
                #        Loop over tokens
                for token in sentence.tokens:
                    #           Convert features to indices
                    #           Append to sentence
                    if token.text.lower() in self._word_embeddings.vocab:
                        sentence_labels.append(self.pos_to_index[token.label])
                labels.append(sentence_labels)
        return np.array(labels)