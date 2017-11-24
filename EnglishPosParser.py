import Document
import Parser
class EnglishPosParser(Parser):
    def read(self, content: str) -> Document:
        """Reads the content of a NER/POS data file and returns one document instance per document it finds."""
        documents = []

        # Split the text in documents using string '-DOCSTART- -X- O O' and loop over it
        #     Slit lines and loop over
        #         Make vectors of tokens and labels (column 2) and at the '\n\n' make a sentence.
        #     Create a Document object and append it to list of documents

        return documents